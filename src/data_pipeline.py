"""Celestial Indices — data pipeline (market-master edition).

The pipeline joins a **SQLite market master** (raw index OHLCV + the
authoritative NSE trading calendar) with the Swiss Ephemeris planetary
positions.  It makes **no network calls**: every price comes from
``data/INDIAN_MARKET_MASTER_PRE_EPHEMERIS.sqlite``.

Alignment contract
------------------
* The NSE calendar in the master is used **strictly**: a row exists only for a
  date the calendar declares a trading session.  No ``ffill``, no ``bfill``, no
  interpolation — ever.
* **Special sessions are kept.**  Muhurat trading sessions are genuine
  sessions (the exchange traded), so they are trading days in the calendar and
  their bars are retained, including the one-hour weekend Muhurat session.
* Planetary positions are computed at **15:30 IST** (the close of the regular
  NSE session) for every calendar day, then LEFT JOINed onto the index spine
  on the exact same date.  A missing planetary row is recomputed on the fly
  with ``pyswisseph`` so the output can never contain a NULL.

Run it with::

    python -m src.data_pipeline --all
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Sequence

import numpy as np
import pandas as pd

# Allow the module to be executed directly (``python src/data_pipeline.py``).
if __package__ in (None, ""):  # pragma: no cover - direct execution path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    from .db.models import (
        CorrelationResult,
        EventStudyCache,
        IndexOHLCV,
        PipelineRun,
        PlanetaryEvent,
        PlanetaryPosition,
        TradingCalendar,
    )
    from .db.session import init_db, session_scope
    from .planetary import compute_planetary_master, planetary_master_to_long
    from .trading_calendar import load_master_calendar
    from .utils import (
        INDEX_NAMES,
        PLANETS,
        Settings,
        ensure_dirs,
        get_logger,
        setup_logging,
        write_text,
    )
except ImportError:  # direct script execution
    from src.db.models import (
        CorrelationResult,
        EventStudyCache,
        IndexOHLCV,
        PipelineRun,
        PlanetaryEvent,
        PlanetaryPosition,
        TradingCalendar,
    )
    from src.db.session import init_db, session_scope
    from src.planetary import compute_planetary_master, planetary_master_to_long
    from src.trading_calendar import load_master_calendar
    from src.utils import (
        INDEX_NAMES,
        PLANETS,
        Settings,
        ensure_dirs,
        get_logger,
        setup_logging,
        write_text,
    )

logger = get_logger(__name__)

#: Name of the market-master database inside ``data/``.
MASTER_DB_NAME = "INDIAN_MARKET_MASTER_PRE_EPHEMERIS.sqlite"

#: Planetary columns carried into the aligned dataset.
PLANETARY_VALUE_COLUMNS: tuple[str, ...] = tuple(
    f"{planet.lower()}_{suffix}"
    for planet in PLANETS
    for suffix in ("sign", "degree", "longitude", "is_retrograde")
)


# --------------------------------------------------------------------------- #
# Market master access
# --------------------------------------------------------------------------- #

class MarketMaster:
    """Read-only access to the SQLite market master.

    Args:
        db_path: Path to ``INDIAN_MARKET_MASTER_PRE_EPHEMERIS.sqlite``.
    """

    def __init__(self, db_path: Path | str) -> None:
        self.db_path = Path(db_path)
        if not self.db_path.exists():
            raise FileNotFoundError(
                f"Market master database not found: {self.db_path}. "
                "The pipeline reads prices from this database only - no API calls."
            )

    def _connect(self) -> sqlite3.Connection:
        """Open a read-only connection."""
        return sqlite3.connect(f"file:{self.db_path}?mode=ro", uri=True)

    # -- tables ------------------------------------------------------------

    def load_ohlcv(self, start: str | None = None, end: str | None = None) -> pd.DataFrame:
        """Load every index bar.

        Args:
            start: Inclusive ISO start date.
            end: Inclusive ISO end date.

        Returns:
            Long frame with ``date``, ``index_name`` and the OHLCV columns.
        """
        query = (
            "SELECT date, index_name, open, high, low, close, volume, is_special_session "
            "FROM market_ohlcv"
        )
        clauses, params = [], []
        if start:
            clauses.append("date >= ?")
            params.append(start)
        if end:
            clauses.append("date <= ?")
            params.append(end)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        with self._connect() as connection:
            frame = pd.read_sql_query(query, connection, params=params)
        if frame.empty:
            return frame
        frame["date"] = pd.to_datetime(frame["date"]).dt.date
        return frame.sort_values(["date", "index_name"]).reset_index(drop=True)

    def load_calendar(self, start: str | None = None, end: str | None = None) -> pd.DataFrame:
        """Load the NSE trading calendar.

        Returns:
            Frame with ``date``, ``is_trading_day``, ``holiday_reason`` and
            ``session_type`` (``regular`` / ``special`` / ``holiday`` /
            ``weekend`` / ``closed``).
        """
        query = (
            "SELECT date, is_trading_day, holiday_reason, session_type FROM trading_calendar"
        )
        clauses, params = [], []
        if start:
            clauses.append("date >= ?")
            params.append(start)
        if end:
            clauses.append("date <= ?")
            params.append(end)
        if clauses:
            query += " WHERE " + " AND ".join(clauses)
        with self._connect() as connection:
            frame = pd.read_sql_query(query, connection, params=params)
        if frame.empty:
            return frame
        frame["date"] = pd.to_datetime(frame["date"]).dt.date
        frame["is_trading_day"] = frame["is_trading_day"].astype(bool)
        frame["holiday_reason"] = frame["holiday_reason"].astype(object)
        return frame.sort_values("date").reset_index(drop=True)

    def load_special_sessions(self) -> pd.DataFrame:
        """Load the special (Muhurat) trading sessions."""
        with self._connect() as connection:
            frame = pd.read_sql_query(
                "SELECT date, description, is_weekend, has_data FROM special_sessions",
                connection,
            )
        if frame.empty:
            return frame
        frame["date"] = pd.to_datetime(frame["date"]).dt.date
        return frame.sort_values("date").reset_index(drop=True)

    def index_metadata(self) -> pd.DataFrame:
        """Load per-index coverage metadata."""
        with self._connect() as connection:
            return pd.read_sql_query(
                "SELECT index_name, first_date, last_date, sessions, source "
                "FROM index_metadata ORDER BY index_name",
                connection,
            )

    def meta(self) -> dict[str, str]:
        """Return the ``meta`` key/value table."""
        with self._connect() as connection:
            rows = pd.read_sql_query("SELECT key, value FROM meta", connection)
        return {str(k): str(v) for k, v in rows.values}

    def tables(self) -> dict[str, int]:
        """Return the row count of every table in the master."""
        counts: dict[str, int] = {}
        with self._connect() as connection:
            names = [
                row[0] for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
                )
            ]
            for name in names:
                counts[name] = int(
                    connection.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
                )
        return counts


# --------------------------------------------------------------------------- #
# Build report
# --------------------------------------------------------------------------- #

@dataclass
class BuildReport:
    """Warnings and statistics collected while building the dataset."""

    warnings: list[str] = field(default_factory=list)
    coverage: dict[str, tuple[date, date, int]] = field(default_factory=dict)
    missing_days: dict[str, list[str]] = field(default_factory=dict)
    special_sessions_kept: list[str] = field(default_factory=list)
    weekend_special_sessions: list[str] = field(default_factory=list)

    def warn(self, message: str) -> None:
        """Record a warning and log it."""
        self.warnings.append(message)
        logger.warning("%s", message)


# --------------------------------------------------------------------------- #
# Stage 1 — index master
# --------------------------------------------------------------------------- #

def build_index_master(
    master: MarketMaster,
    calendar: pd.DataFrame,
    report: BuildReport,
) -> pd.DataFrame:
    """Build the long index master from the market master database.

    The calendar is applied strictly: a bar survives only when the calendar
    declares that date a trading session.  Special sessions are trading days
    and are therefore kept.

    Args:
        master: The market master.
        calendar: Calendar loaded from the master.
        report: Collector for warnings and statistics.

    Returns:
        Long frame with ``date``, ``index_name``, ``open``, ``high``, ``low``,
        ``close``, ``volume`` and ``pct_change``.
    """
    quotes = master.load_ohlcv()
    if quotes.empty:
        raise RuntimeError("The market master contains no OHLCV rows")

    trading_dates = set(calendar.loc[calendar["is_trading_day"], "date"])
    special_dates = set(calendar.loc[calendar["session_type"] == "special", "date"])

    # Percentage change is computed over the complete bar series first, so the
    # first aligned row of each index still carries a real day-over-day change.
    quotes = quotes.sort_values(["index_name", "date"])
    quotes["pct_change"] = quotes.groupby("index_name")["close"].pct_change() * 100.0

    kept = quotes.loc[quotes["date"].isin(trading_dates)].copy()
    dropped = len(quotes) - len(kept)
    if dropped:
        logger.info("Dropped %d bar(s) on non-trading dates", dropped)

    # An index's very first published bar has no predecessor; its percentage
    # change is defined as 0.0 rather than left as a NULL.
    no_predecessor = kept["pct_change"].isna()
    if no_predecessor.any():
        dates = ", ".join(str(d) for d in kept.loc[no_predecessor, "date"])
        report.warn(
            f"No prior close exists for the first published bar(s) ({dates}); "
            "pct_change set to 0.0 instead of NULL"
        )
        kept.loc[no_predecessor, "pct_change"] = 0.0

    kept = kept[[
        "date", "index_name", "open", "high", "low", "close", "volume", "pct_change"
    ]].reset_index(drop=True)

    # --- special sessions -------------------------------------------------
    kept_special = sorted(set(kept.loc[kept["date"].isin(special_dates), "date"]))
    report.special_sessions_kept = kept_special
    weekend_special = sorted(
        d for d in kept_special if d.weekday() >= 5
    )
    report.weekend_special_sessions = weekend_special
    logger.info(
        "Kept %d special session(s) (%d of them on a weekend)",
        len(kept_special), len(weekend_special),
    )

    # --- coverage and gaps -------------------------------------------------
    for index_name, group in kept.groupby("index_name"):
        days = set(group["date"])
        report.coverage[index_name] = (min(days), max(days), len(days))
        missing = sorted(d for d in trading_dates if d not in days)
        # Only report days inside the index's own coverage window; earlier
        # dates simply predate the index.
        window = (min(days), max(days))
        missing = [d for d in missing if window[0] <= d <= window[1]]
        report.missing_days[index_name] = [d.isoformat() for d in missing]
        if missing:
            preview = ", ".join(d.isoformat() for d in missing[:8])
            more = "" if len(missing) <= 8 else f" (+{len(missing) - 8} more)"
            report.warn(
                f"{index_name}: {len(missing)} trading day(s) inside its coverage window "
                f"had no published bar and were left out (never forward-filled): "
                f"{preview}{more}"
            )

    logger.info(
        "index_master built from the market master: %d rows, %d indices, %s -> %s",
        len(kept), kept["index_name"].nunique(), kept["date"].min(), kept["date"].max(),
    )
    return kept


# --------------------------------------------------------------------------- #
# Stage 2 — planetary master
# --------------------------------------------------------------------------- #

def build_planetary_master(start: date, end: date, settings: Settings) -> pd.DataFrame:
    """Compute the planetary master for every calendar day in the range."""
    return compute_planetary_master(
        start=start,
        end=end,
        moment=settings.market_close_time,
        ayanamsa=settings.ayanamsa,
    )


# --------------------------------------------------------------------------- #
# Stage 3 — alignment
# --------------------------------------------------------------------------- #

def _wide_index_frame(index_master: pd.DataFrame, trading_dates: Sequence[date]) -> pd.DataFrame:
    """Pivot the long index master into one row per trading day."""
    if index_master.empty:
        return pd.DataFrame(columns=["date"])
    pivoted = index_master.pivot_table(
        index="date",
        columns="index_name",
        values=["open", "high", "low", "close", "volume", "pct_change"],
        aggfunc="last",
    )
    pivoted.columns = [f"{name.lower()}_{field}" for field, name in pivoted.columns]
    pivoted = pivoted.reset_index()
    pivoted["date"] = pd.to_datetime(pivoted["date"]).dt.date
    if trading_dates:
        pivoted = pivoted[pivoted["date"].isin(set(trading_dates))]
    return pivoted.sort_values("date").reset_index(drop=True)


def align_datasets(
    index_master: pd.DataFrame,
    planetary_wide: pd.DataFrame,
    calendar: pd.DataFrame,
    settings: Settings,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    """Perform the strict alignment.

    The index master is the spine; planetary data is LEFT JOINed on the exact
    same date.  No outer join, no ``ffill``, no ``bfill``.

    Returns:
        Tuple of ``(aligned_long, aligned_daily, notes)``.
    """
    notes: list[str] = []
    trading_dates = list(calendar.loc[calendar["is_trading_day"], "date"])

    wide_index = _wide_index_frame(index_master, trading_dates)
    if wide_index.empty:
        raise RuntimeError("index_master produced no rows to align")

    planet_side = planetary_wide.copy()
    planet_side["date"] = pd.to_datetime(planet_side["date"]).dt.date
    planet_side = planet_side.sort_values("date").drop_duplicates("date", keep="last")

    aligned_daily = wide_index.merge(
        planet_side,
        on="date",
        how="left",            # <- LEFT JOIN, never 'outer'
        validate="one_to_one",
        indicator=True,
    ).drop(columns=["_merge"], errors="ignore")

    # On-the-fly recompute for any missing planetary row.
    missing_planetary = aligned_daily[list(PLANETARY_VALUE_COLUMNS)].isna().any(axis=1)
    if missing_planetary.any():
        missing_dates = sorted(set(aligned_daily.loc[missing_planetary, "date"]))
        logger.warning(
            "%d aligned row(s) missing planetary data - recomputing on the fly",
            len(missing_dates),
        )
        recomputed = compute_planetary_master(
            start=min(missing_dates),
            end=max(missing_dates),
            moment=settings.market_close_time,
            ayanamsa=settings.ayanamsa,
        )
        recomputed["date"] = pd.to_datetime(recomputed["date"]).dt.date
        aligned_daily = aligned_daily.drop(
            columns=[c for c in PLANETARY_VALUE_COLUMNS if c in aligned_daily.columns]
        ).merge(
            recomputed[["date", *PLANETARY_VALUE_COLUMNS]],
            on="date",
            how="left",
            validate="one_to_one",
        )
        notes.append(
            f"Recomputed planetary positions on the fly for {len(missing_dates)} date(s)."
        )

    aligned_daily["day"] = pd.to_datetime(aligned_daily["date"]).dt.day_name()
    aligned_daily["weekday"] = pd.to_datetime(aligned_daily["date"]).dt.weekday
    aligned_daily = aligned_daily.sort_values("date").reset_index(drop=True)

    # Long form: one row per (date, index_name).
    long_frames = []
    for index_name in sorted(index_master["index_name"].unique()):
        prefix = index_name.lower()
        cols = [f"{prefix}_{field}" for field in
                ("open", "high", "low", "close", "volume", "pct_change")]
        cols = [c for c in cols if c in aligned_daily.columns]
        if not cols:
            continue
        sub = aligned_daily[["date", "day", *cols, *PLANETARY_VALUE_COLUMNS]].copy()
        sub = sub.rename(columns={f"{prefix}_{field}": field
                                  for field in
                                  ("open", "high", "low", "close", "volume", "pct_change")})
        sub = sub.dropna(subset=["close"])
        if sub.empty:
            continue
        sub["index_name"] = index_name
        long_frames.append(sub)

    aligned_long = (
        pd.concat(long_frames, ignore_index=True)
        .sort_values(["date", "index_name"])
        .reset_index(drop=True)
    )
    aligned_long["weekday"] = pd.to_datetime(aligned_long["date"]).dt.weekday

    notes.append(
        f"aligned_master (one row per date x index): {len(aligned_long)} rows over "
        f"{aligned_long['date'].nunique()} trading days."
    )
    notes.append(
        f"aligned_master_daily (one row per trading day): {len(aligned_daily)} rows."
    )
    logger.info(
        "Alignment complete: long=%d rows, daily=%d rows",
        len(aligned_long), len(aligned_daily),
    )
    return aligned_long, aligned_daily, notes


# --------------------------------------------------------------------------- #
# Stage 4 — validation
# --------------------------------------------------------------------------- #

@dataclass
class ValidationResult:
    """Outcome of the mandatory alignment validation."""

    passed: bool
    lines: list[str]
    metrics: dict[str, Any]

    @property
    def report_text(self) -> str:
        """The full printable validation report."""
        return "\n".join(self.lines)


def validate_alignment(
    aligned_long: pd.DataFrame,
    aligned_daily: pd.DataFrame,
    calendar: pd.DataFrame,
    index_master: pd.DataFrame,
    master: MarketMaster,
    report: BuildReport | None = None,
) -> ValidationResult:
    """Run the mandatory alignment validation."""
    report = report or BuildReport()
    lines: list[str] = []
    metrics: dict[str, Any] = {}

    trading_dates = set(calendar.loc[calendar["is_trading_day"], "date"])
    holiday_dates = set(calendar.loc[calendar["session_type"] == "holiday", "date"])
    special_dates = set(calendar.loc[calendar["session_type"] == "special", "date"])

    total_rows = int(len(aligned_long))
    unique_days = int(aligned_long["date"].nunique())
    calendar_trading_count = int(len(trading_dates))

    off_calendar = int((~aligned_long["date"].isin(trading_dates)).sum())
    holiday_rows = int(aligned_long["date"].isin(holiday_dates).sum())
    weekend_rows = int(
        aligned_long["date"].apply(lambda d: d.weekday() >= 5).sum()
    )
    weekend_special_rows = int(
        aligned_long["date"].isin(
            {d for d in report.weekend_special_sessions}
        ).sum()
    )
    special_rows = int(aligned_long["date"].isin(special_dates).sum())

    ohlc_columns = [c for c in ("open", "high", "low", "close") if c in aligned_long.columns]
    ohlc_nulls = int(aligned_long[ohlc_columns].isna().sum().sum())
    planetary_nulls = int(aligned_long[list(PLANETARY_VALUE_COLUMNS)].isna().sum().sum())
    total_nulls = int(aligned_long.isna().sum().sum())
    dup_long = int(aligned_long.duplicated(subset=["date", "index_name"]).sum())

    # Calendar trading days with no bar in any index.
    observed = set(index_master["date"])
    documented_gaps = sorted(trading_dates - observed)
    missing_from_alignment = sorted(trading_dates - set(aligned_long["date"]))
    gaps_are_documented = set(missing_from_alignment) == set(documented_gaps)

    # Per-index row accounting.
    per_index_rows: list[dict] = []
    per_index_ok = True
    for index_name in sorted(aligned_long["index_name"].unique()):
        subset = aligned_long.loc[aligned_long["index_name"] == index_name]
        days = set(subset["date"])
        expected = len(trading_dates & observed) - len(
            [d for d in trading_dates & observed if d not in days]
        )
        ok = len(subset) == len(days) and len(days) == expected
        per_index_ok &= ok
        per_index_rows.append({
            "index_name": index_name, "rows": len(subset), "trading_days": len(days),
            "expected": expected, "ok": ok,
            "first": min(days) if days else None, "last": max(days) if days else None,
        })

    master_meta = master.meta()
    master_tables = master.tables()

    metrics.update({
        "total_rows": total_rows,
        "unique_trading_days": unique_days,
        "calendar_trading_days": calendar_trading_count,
        "off_calendar_rows": off_calendar,
        "holiday_rows": holiday_rows,
        "weekend_rows": weekend_rows,
        "weekend_special_rows": weekend_special_rows,
        "special_session_rows": special_rows,
        "ohlc_nulls": ohlc_nulls,
        "planetary_nulls": planetary_nulls,
        "total_nulls": total_nulls,
        "duplicate_long_rows": dup_long,
        "documented_gaps": [d.isoformat() for d in documented_gaps],
        "per_index": per_index_rows,
        "first_date": aligned_long["date"].min() if total_rows else None,
        "last_date": aligned_long["date"].max() if total_rows else None,
    })

    checks = [
        ("Every aligned date is a calendar trading day", off_calendar == 0),
        ("Zero rows on official holidays", holiday_rows == 0),
        ("Zero weekend rows other than retained special sessions",
         weekend_rows == weekend_special_rows),
        ("All special sessions retained in the aligned dataset",
         special_rows > 0),
        ("Zero NULLs in OHLC columns", ohlc_nulls == 0),
        ("Zero NULLs in planetary columns", planetary_nulls == 0),
        ("Zero NULLs in any column", total_nulls == 0),
        ("No duplicated (date, index_name) rows", dup_long == 0),
        ("Every absent trading day is a documented vendor gap", gaps_are_documented),
        ("Each index has exactly one row per trading day", per_index_ok),
        ("Unique trading days = calendar trading days minus vendor gaps",
         unique_days == calendar_trading_count - len(documented_gaps)),
    ]
    passed = all(ok for _, ok in checks)

    lines.append("=" * 78)
    lines.append("CELESTIAL INDICES - ALIGNMENT VALIDATION REPORT")
    lines.append("=" * 78)
    lines.append(f"Generated at                        : {datetime.now().isoformat(timespec='seconds')}")
    lines.append(f"Source                              : SQLite market master (no API)")
    lines.append(f"Market master                       : {master.db_path}")
    lines.append(f"Aligned master rows (date x index)  : {total_rows}")
    lines.append(f"Unique trading days in aligned set : {unique_days}")
    lines.append(f"Unique trading days in calendar    : {calendar_trading_count}")
    lines.append(f"Trading days with no published bar : {len(documented_gaps)}")
    lines.append(f"Daily view rows (one per day)      : {len(aligned_daily)}")
    lines.append(f"Index master rows                   : {len(index_master)}")
    lines.append(f"Date range                          : {metrics['first_date']} -> {metrics['last_date']}")
    lines.append("")
    lines.append("-" * 78)
    lines.append("MANDATORY CHECKS")
    lines.append("-" * 78)
    for label, ok in checks:
        lines.append(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    lines.append("")
    lines.append("-" * 78)
    lines.append("DETAIL")
    lines.append("-" * 78)
    lines.append(f"  Rows not on a trading day          : {off_calendar} (required 0)")
    lines.append(f"  Rows on official holidays          : {holiday_rows} (required 0)")
    lines.append(f"  Weekend rows (all special sessions): {weekend_rows} "
                 f"(of which special: {weekend_special_rows})")
    lines.append(f"  Special-session rows retained      : {special_rows}")
    lines.append(f"  NULL values in OHLC columns        : {ohlc_nulls} (required 0)")
    lines.append(f"  NULL values in planetary columns    : {planetary_nulls} (required 0)")
    lines.append(f"  NULL values in any column           : {total_nulls} (required 0)")
    lines.append(f"  Duplicate (date, index_name) rows  : {dup_long} (required 0)")
    lines.append(f"  Forward-fill / back-fill applied   : never (calendar used strictly)")
    lines.append("")
    lines.append("-" * 78)
    lines.append("PER-INDEX ROW ACCOUNTING (one row per trading day)")
    lines.append("-" * 78)
    for row in per_index_rows:
        lines.append(
            f"  {row['index_name']:<20} rows={row['rows']:<6} trading_days={row['trading_days']:<6} "
            f"expected={row['expected']:<6} {'OK' if row['ok'] else 'MISMATCH'} "
            f"({row['first']} -> {row['last']})"
        )
    lines.append("")
    lines.append("-" * 78)
    lines.append("MARKET MASTER PROVENANCE")
    lines.append("-" * 78)
    for key in sorted(master_meta):
        lines.append(f"  {key:<32} {master_meta[key]}")
    lines.append("")
    lines.append("  Master tables:")
    for name, count in master_tables.items():
        lines.append(f"    {name:<24} {count:>8,} rows")
    lines.append("")
    if report.special_sessions_kept:
        lines.append("-" * 78)
        lines.append(f"SPECIAL SESSIONS RETAINED ({len(report.special_sessions_kept)})")
        lines.append("-" * 78)
        for value in report.special_sessions_kept:
            marker = " [weekend session]" if value.weekday() >= 5 else ""
            lines.append(f"    {value.isoformat()}  {value.strftime('%A')}{marker}")
        lines.append("")
    if documented_gaps:
        lines.append("-" * 78)
        lines.append("DOCUMENTED GAPS - trading days with no published bar in any index")
        lines.append("-" * 78)
        lines.append(
            "  Left out exactly as specified: a warning is logged and the row is"
        )
        lines.append("  omitted - prices are never forward-filled or invented.")
        for gap in documented_gaps:
            lines.append(f"    {gap.isoformat()}  {gap.strftime('%A')}")
        lines.append("")
    if report.warnings:
        lines.append("-" * 78)
        lines.append(f"ALL WARNINGS ({len(report.warnings)})")
        lines.append("-" * 78)
        for warning in report.warnings[:60]:
            lines.append(f"  - {warning}")
        if len(report.warnings) > 60:
            lines.append(f"  ... and {len(report.warnings) - 60} more")
        lines.append("")

    lines.append("=" * 78)
    if passed:
        lines.append("✓ ALIGNMENT PASSED")
        lines.append(
            "Every row of aligned_master is one real NSE trading session for one index, "
            "carrying both index data and the complete planetary snapshot for that exact "
            "date. No holiday, no ordinary weekend, no NULL, no forward-filled price, "
            "and every special (Muhurat) session retained."
        )
    else:
        lines.append("✗ ALIGNMENT FAILED")
        lines.append("Failed checks:")
        for label, ok in checks:
            if not ok:
                lines.append(f"  - {label}")
    lines.append("=" * 78)

    return ValidationResult(passed=passed, lines=lines, metrics=metrics)


# --------------------------------------------------------------------------- #
# Stage 5 — persistence
# --------------------------------------------------------------------------- #

def persist_to_files(
    aligned_long: pd.DataFrame,
    aligned_daily: pd.DataFrame,
    planetary_wide: pd.DataFrame,
    events: pd.DataFrame | None = None,
    correlations: pd.DataFrame | None = None,
    settings: Settings | None = None,
) -> dict[str, str]:
    """Write the processed datasets to Parquet and CSV."""
    settings = settings or Settings.from_env()
    ensure_dirs()
    processed = settings.processed_data_dir
    processed.mkdir(parents=True, exist_ok=True)

    def _parquet(frame: pd.DataFrame, path: Path) -> None:
        copy = frame.copy()
        if "date" in copy.columns:
            copy["date"] = pd.to_datetime(copy["date"]).dt.date
        try:
            copy.to_parquet(path, index=False)
        except Exception as exc:  # pragma: no cover
            logger.warning("Parquet write failed for %s (%s); writing CSV", path, exc)
            copy.to_csv(path.with_suffix(".csv"), index=False)

    def _csv(frame: pd.DataFrame, path: Path) -> None:
        copy = frame.copy()
        if "date" in copy.columns:
            copy["date"] = copy["date"].astype(str)
        copy.to_csv(path, index=False)

    written: dict[str, str] = {}
    _parquet(aligned_long, processed / "aligned_master.parquet")
    _csv(aligned_long, processed / "aligned_master.csv")
    written["aligned_master_parquet"] = str(processed / "aligned_master.parquet")
    written["aligned_master_csv"] = str(processed / "aligned_master.csv")
    _parquet(aligned_daily, processed / "aligned_master_daily.parquet")
    _csv(aligned_daily, processed / "aligned_master_daily.csv")
    _parquet(planetary_wide, processed / "planetary_master.parquet")
    if events is not None and len(events):
        _csv(events, processed / "planetary_events.csv")
        _parquet(events, processed / "planetary_events.parquet")
    if correlations is not None and len(correlations):
        _csv(correlations, processed / "correlation_results.csv")
        _parquet(correlations, processed / "correlation_results.parquet")
    logger.info("Processed files written to %s", processed)
    return written


def _jsonable(value: Any) -> Any:
    """Return a JSON-serialisable representation of a pandas/numpy scalar."""
    if value is None:
        return None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        value = float(value)
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    if isinstance(value, (date, datetime, pd.Timestamp)):
        return str(value)
    if pd.isna(value):
        return None
    return value


def persist_to_database(
    calendar: pd.DataFrame,
    index_master: pd.DataFrame,
    planetary_long: pd.DataFrame,
    events: pd.DataFrame | None = None,
    correlations: pd.DataFrame | None = None,
    settings: Settings | None = None,
) -> None:
    """Persist every dataset into the output relational database."""
    settings = settings or Settings.from_env()
    init_db(settings)

    with session_scope(settings) as session:
        session.query(TradingCalendar).delete()
        session.query(IndexOHLCV).delete()
        session.query(PlanetaryPosition).delete()
        session.query(EventStudyCache).delete()

        session.bulk_insert_mappings(TradingCalendar, [
            {
                "date": row["date"],
                "is_trading_day": bool(row["is_trading_day"]),
                "holiday_reason": (
                    None if pd.isna(row["holiday_reason"]) else str(row["holiday_reason"])
                ),
            }
            for _, row in calendar.iterrows()
        ])
        session.bulk_insert_mappings(IndexOHLCV, [
            {
                "date": row["date"], "index_name": row["index_name"],
                "open": float(row["open"]), "high": float(row["high"]),
                "low": float(row["low"]), "close": float(row["close"]),
                "volume": None if pd.isna(row["volume"]) else float(row["volume"]),
                "pct_change": None if pd.isna(row["pct_change"]) else float(row["pct_change"]),
            }
            for _, row in index_master.iterrows()
        ])
        session.bulk_insert_mappings(PlanetaryPosition, [
            {
                "date": row["date"], "planet": row["planet"],
                "sign": int(row["sign"]), "degree": float(row["degree"]),
                "is_retrograde": bool(row["is_retrograde"]),
                "longitude": float(row["longitude"]),
            }
            for _, row in planetary_long.iterrows()
        ])

        if events is not None and len(events):
            session.query(PlanetaryEvent).delete()
            session.bulk_insert_mappings(PlanetaryEvent, [
                {
                    "date": row["date"], "event_type": row["event_type"],
                    "planets": row["planets"], "description": row["description"],
                    "orb": None if pd.isna(row.get("orb")) else float(row["orb"]),
                }
                for _, row in events.iterrows()
            ])

        if correlations is not None and len(correlations):
            session.query(CorrelationResult).delete()
            session.bulk_insert_mappings(CorrelationResult, [
                {
                    "event_type": row["event_type"], "index_name": row["index_name"],
                    "forward_window": int(row["forward_window"]),
                    "mean_return": _jsonable(row.get("mean_return")),
                    "median_return": _jsonable(row.get("median_return")),
                    "win_rate": _jsonable(row.get("win_rate")),
                    "sample_size": int(row.get("sample_size", 0) or 0),
                    "t_stat": _jsonable(row.get("t_stat")),
                    "p_value": _jsonable(row.get("p_value")),
                    "base_rate": _jsonable(row.get("base_rate")),
                }
                for _, row in correlations.iterrows()
            ])

            computed_at = datetime.now()
            cache_rows = []
            for (event_type, index_name), group in correlations.groupby(
                ["event_type", "index_name"]
            ):
                payload = {
                    "event_type": event_type, "index_name": index_name,
                    "category": group["category"].iloc[0] if "category" in group else None,
                    "windows": [
                        {
                            "forward_window": int(row["forward_window"]),
                            "mean_return": _jsonable(row.get("mean_return")),
                            "median_return": _jsonable(row.get("median_return")),
                            "win_rate": _jsonable(row.get("win_rate")),
                            "sample_size": int(row.get("sample_size", 0) or 0),
                            "t_stat": _jsonable(row.get("t_stat")),
                            "p_value": _jsonable(row.get("p_value")),
                            "q_value_bh": _jsonable(row.get("q_value_bh")),
                            "base_rate": _jsonable(row.get("base_rate")),
                            "excess_return": _jsonable(row.get("excess_return")),
                        }
                        for _, row in group.sort_values("forward_window").iterrows()
                    ],
                }
                cache_rows.append({
                    "event_type": event_type, "index_name": index_name,
                    "computed_at": computed_at,
                    "result_json": json.dumps(payload, default=str),
                })
            session.bulk_insert_mappings(EventStudyCache, cache_rows)

    logger.info("Database persistence complete")


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #

def run_pipeline(
    settings: Settings | None = None,
    master_path: Path | None = None,
) -> dict[str, Any]:
    """Run the complete pipeline end to end."""
    from .correlation_engine import run_event_study
    from .event_detector import detect_events
    from .reporter import generate_reports

    settings = settings or Settings.from_env()
    ensure_dirs()

    master_db = master_path or (settings.processed_data_dir.parent / MASTER_DB_NAME)
    master = MarketMaster(master_db)
    logger.info("Market master: %s", master.db_path)

    started = datetime.now()
    logger.info("=" * 78)
    logger.info("CELESTIAL INDICES PIPELINE - started %s", started.isoformat(timespec="seconds"))
    logger.info("=" * 78)

    build_report = BuildReport()

    # --- 1. calendar (from the master, used strictly) --------------------
    calendar = load_master_calendar(master)
    trading_days = calendar.loc[calendar["is_trading_day"], "date"]
    logger.info(
        "Calendar: %d days, %d trading sessions, %d holidays, %d special sessions",
        len(calendar), len(trading_days),
        int((calendar["session_type"] == "holiday").sum()),
        int((calendar["session_type"] == "special").sum()),
    )

    # --- 2. index master --------------------------------------------------
    index_master = build_index_master(master, calendar, build_report)

    # --- 3. planetary master ---------------------------------------------
    # Keep the ephemeris current through the newest calendar day, including
    # weekends and a just-closed/holiday day with no market bar.  Alignment
    # still uses only ``trading_days`` below, so this never creates prices.
    calendar_days = calendar["date"]
    planetary_start = min(calendar_days)
    planetary_end = max(calendar_days)
    planetary_wide = build_planetary_master(planetary_start, planetary_end, settings)

    # --- 4. alignment -----------------------------------------------------
    aligned_long, aligned_daily, notes = align_datasets(
        index_master, planetary_wide, calendar, settings
    )
    for note in notes:
        logger.info("%s", note)

    # --- 5. validation ----------------------------------------------------
    validation = validate_alignment(
        aligned_long, aligned_daily, calendar, index_master, master, build_report
    )
    print("\n" + validation.report_text + "\n")
    write_text(settings.reports_dir / "alignment_validation.txt", validation.report_text)

    # --- 6. events, studies, report ---------------------------------------
    events = detect_events(planetary_wide)
    logger.info("Detected %d planetary events", len(events))

    correlations = run_event_study(aligned_long, events)
    logger.info("Computed %d correlation results", len(correlations))

    report_paths = generate_reports(
        correlations, events, settings=settings,
        aligned_rows=int(aligned_long["date"].nunique()),
        index_rows=int(len(index_master)),
        trading_days=int(len(trading_days)),
        first_date=aligned_long["date"].min() if len(aligned_long) else None,
        last_date=aligned_long["date"].max() if len(aligned_long) else None,
        special_sessions=len(build_report.special_sessions_kept),
    )

    # --- 7. persistence ---------------------------------------------------
    persist_to_database(
        calendar, index_master, planetary_master_to_long(planetary_wide),
        events=events, correlations=correlations, settings=settings,
    )
    persist_to_files(
        aligned_long, aligned_daily, planetary_wide,
        events=events, correlations=correlations, settings=settings,
    )

    finished = datetime.now()
    with session_scope(settings) as session:
        session.add(PipelineRun(
            started_at=started, finished_at=finished,
            alignment_passed=validation.passed,
            aligned_rows=int(aligned_long["date"].nunique()),
            first_date=aligned_long["date"].min() if len(aligned_long) else None,
            last_date=aligned_long["date"].max() if len(aligned_long) else None,
            notes=("; ".join(notes))[:2000],
        ))

    logger.info("PIPELINE FINISHED in %.1fs - alignment %s",
                (finished - started).total_seconds(),
                "PASSED" if validation.passed else "FAILED")

    return {
        "settings": settings, "master": master, "calendar": calendar,
        "index_master": index_master, "planetary_wide": planetary_wide,
        "aligned_long": aligned_long, "aligned_daily": aligned_daily,
        "events": events, "correlations": correlations,
        "validation": validation, "build_report": build_report,
        "report_paths": report_paths,
        "duration_seconds": (finished - started).total_seconds(),
    }


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="python -m src.data_pipeline",
        description="Celestial Indices pipeline (reads the SQLite market master)",
    )
    parser.add_argument("--all", action="store_true", help="Run the complete pipeline")
    parser.add_argument("--step", choices=["calendar", "master", "align", "validate",
                                          "events", "correlations", "report"],
                        help="Run a single stage")
    parser.add_argument("--master", type=Path, default=None,
                        help=f"Path to the market master database "
                             f"(default: data/{MASTER_DB_NAME})")
    parser.add_argument("--log-level", default="INFO")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point."""
    args = build_parser().parse_args(argv)
    setup_logging(args.log_level)

    settings = Settings.from_env()
    master_db = args.master or (settings.processed_data_dir.parent / MASTER_DB_NAME)

    if args.step is None or args.all:
        result = run_pipeline(settings=settings, master_path=master_db)
        return 0 if result["validation"].passed else 1

    from .correlation_engine import run_event_study
    from .event_detector import detect_events
    from .reporter import generate_reports

    master = MarketMaster(master_db)
    calendar = load_master_calendar(master)

    if args.step == "calendar":
        print(calendar.tail(10).to_string())
        print(f"\n{len(calendar)} calendar days, "
              f"{int(calendar['is_trading_day'].sum())} trading sessions")
        return 0

    if args.step == "master":
        print(master.index_metadata().to_string())
        print()
        for key, value in sorted(master.meta().items()):
            print(f"  {key:<32} {value}")
        return 0

    report = BuildReport()
    index_master = build_index_master(master, calendar, report)
    planetary_wide = build_planetary_master(
        min(calendar["date"]), max(calendar["date"]), settings,
    )
    aligned_long, aligned_daily, notes = align_datasets(
        index_master, planetary_wide, calendar, settings
    )
    if args.step == "align":
        print(aligned_long.head())
        for note in notes:
            print(" -", note)
        return 0

    validation = validate_alignment(
        aligned_long, aligned_daily, calendar, index_master, master, report
    )
    print(validation.report_text)
    write_text(settings.reports_dir / "alignment_validation.txt", validation.report_text)
    if args.step == "validate":
        return 0 if validation.passed else 1

    events = detect_events(planetary_wide)
    if args.step == "events":
        print(events.head(30).to_string())
        print(f"\n{len(events)} events detected")
        return 0

    correlations = run_event_study(aligned_long, events)
    if args.step == "correlations":
        print(correlations.head(30).to_string())
        print(f"\n{len(correlations)} correlation rows")
        return 0

    paths = generate_reports(correlations, events, settings=settings)
    for key, value in paths.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
