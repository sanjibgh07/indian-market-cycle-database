"""NSE trading calendar construction.

The calendar is the backbone of the whole project: index data is only ever
kept for dates the calendar declares as trading days, and the validation
report proves that no weekend or holiday ever leaks into the aligned dataset.

``data/reference/nse_holidays.json`` holds the reconciled holiday list
(date + reason).  See the project README for the full provenance chain.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

from .utils import HOLIDAYS_FILE, Settings, get_logger, read_json

logger = get_logger(__name__)

CALENDAR_COLUMNS: tuple[str, ...] = ("date", "is_trading_day", "holiday_reason")


# --------------------------------------------------------------------------- #
# Holiday reference data
# --------------------------------------------------------------------------- #

def load_holidays(path: Path | None = None) -> pd.DataFrame:
    """Load the reconciled NSE holiday reference file.

    Args:
        path: Optional path override; defaults to ``data/reference/nse_holidays.json``.

    Returns:
        DataFrame with ``date`` (datetime.date), ``reason`` (str),
        ``is_weekend`` (bool) and ``has_special_session`` (bool).

    Raises:
        FileNotFoundError: When the reference file does not exist.
    """
    target = Path(path) if path is not None else HOLIDAYS_FILE
    if not target.exists():
        raise FileNotFoundError(
            f"NSE holiday reference file not found at {target}. "
            "It is required to build the trading calendar."
        )

    payload = read_json(target)
    records = payload["holidays"] if isinstance(payload, dict) else payload
    rows = [
        {
            "date": datetime.fromisoformat(item["date"]).date(),
            "reason": item.get("reason", "Trading Holiday"),
            "is_weekend": bool(item.get("is_weekend", False)),
            "has_special_session": bool(item.get("has_special_session", False)),
        }
        for item in records
    ]
    frame = pd.DataFrame(rows, columns=["date", "reason", "is_weekend", "has_special_session"])
    frame = frame.sort_values("date").reset_index(drop=True)
    logger.info("Loaded %d NSE holidays from %s", len(frame), target)
    return frame


def holiday_metadata(path: Path | None = None) -> dict:
    """Return the provenance metadata embedded in the holiday reference file."""
    target = Path(path) if path is not None else HOLIDAYS_FILE
    payload = read_json(target)
    if isinstance(payload, dict):
        return {k: v for k, v in payload.items() if k != "holidays"}
    return {}


def load_master_calendar(master: Any, start: date | None = None,
                         end: date | None = None) -> pd.DataFrame:
    """Load the authoritative NSE trading calendar from the market master.

    The master database is the single source of truth for which dates are
    trading sessions.  The returned frame carries the session type so that
    special (Muhurat) sessions can be told apart from ordinary trading days
    and from closures.

    Args:
        master: A :class:`src.data_pipeline.MarketMaster` instance.
        start: Optional inclusive start date.
        end: Optional inclusive end date.

    Returns:
        DataFrame with ``date``, ``is_trading_day``, ``holiday_reason`` and
        ``session_type``.
    """
    calendar = master.load_calendar(
        start.isoformat() if start else None,
        end.isoformat() if end else None,
    )
    if calendar.empty:
        raise ValueError("The market master contains no calendar rows")
    logger.info(
        "Loaded calendar from the market master: %d days, %d trading sessions",
        len(calendar), int(calendar["is_trading_day"].sum()),
    )
    return calendar


# --------------------------------------------------------------------------- #
# Calendar construction
# --------------------------------------------------------------------------- #

def build_trading_calendar(
    start: date,
    end: date,
    holidays: pd.DataFrame | None = None,
    holiday_path: Path | None = None,
) -> pd.DataFrame:
    """Build the master trading calendar.

    All weekdays in ``[start, end]`` are generated with
    :func:`pandas.bdate_range`; official NSE holidays are subtracted and the
    published reason is retained.

    Args:
        start: First calendar date to include.
        end: Last calendar date to include (inclusive).
        holidays: Pre-loaded holiday frame; loaded from disk when omitted.
        holiday_path: Optional override for the holiday reference file.

    Returns:
        DataFrame with columns ``date`` (datetime.date), ``is_trading_day``
        (bool) and ``holiday_reason`` (str | None).
    """
    if start > end:
        raise ValueError(f"start ({start}) must not be after end ({end})")

    if holidays is None:
        holidays = load_holidays(holiday_path)

    weekdays = pd.bdate_range(start=start, end=end, freq="C", weekmask="Mon Tue Wed Thu Fri")
    calendar = pd.DataFrame({"date": [d.date() for d in weekdays]})
    calendar["is_trading_day"] = True
    calendar["holiday_reason"] = pd.NA

    holiday_map: dict[date, str] = {}
    for _, row in holidays.iterrows():
        holiday_date = row["date"]
        if isinstance(holiday_date, datetime):
            holiday_date = holiday_date.date()
        if start <= holiday_date <= end:
            holiday_map[holiday_date] = str(row["reason"])

    mask = calendar["date"].isin(holiday_map.keys())
    calendar.loc[mask, "is_trading_day"] = False
    calendar.loc[mask, "holiday_reason"] = calendar.loc[mask, "date"].map(holiday_map)
    calendar["holiday_reason"] = calendar["holiday_reason"].astype("object")

    n_holidays = int(mask.sum())
    n_trading = int(calendar["is_trading_day"].sum())
    logger.info(
        "Trading calendar %s -> %s: %d weekdays, %d holidays, %d trading days",
        start, end, len(calendar), n_holidays, n_trading,
    )
    return calendar.reset_index(drop=True)


def get_trading_days(
    start: date,
    end: date,
    holidays: pd.DataFrame | None = None,
    holiday_path: Path | None = None,
) -> list[date]:
    """Return the list of trading days in ``[start, end]``."""
    calendar = build_trading_calendar(start, end, holidays=holidays, holiday_path=holiday_path)
    return list(calendar.loc[calendar["is_trading_day"], "date"])


def filter_to_trading_days(
    frame: pd.DataFrame,
    calendar: pd.DataFrame,
    date_column: str = "date",
) -> pd.DataFrame:
    """Keep only rows whose date is a trading day in ``calendar``.

    Rows are dropped rather than shifted; the caller is expected to log the
    number of removed rows.
    """
    if date_column not in frame.columns:
        raise KeyError(f"Column {date_column!r} not found in frame")
    trading = set(calendar.loc[calendar["is_trading_day"], "date"])
    mask = frame[date_column].isin(trading)
    return frame.loc[mask].copy()


def reconcile_with_sessions(
    calendar: pd.DataFrame,
    sessions: Iterable[date],
    date_column: str = "date",
) -> dict[str, list[str]]:
    """Cross-check the calendar against observed market sessions.

    Two classes of discrepancy are reported:

    ``calendar_trading_but_no_session``
        The calendar expects a session but the vendor published no bar
        (a data gap).  The pipeline logs a warning and leaves the row out.
    ``session_but_calendar_closed``
        A session was observed on a date the calendar calls a holiday.  This
        indicates a defect in the holiday reference file and must be fixed at
        the source, never silently ignored.

    Args:
        calendar: Calendar produced by :func:`build_trading_calendar`.
        sessions: Observed trading dates.
        date_column: Name of the date column in ``calendar``.

    Returns:
        Mapping of problem kind to the list of affected ISO date strings.
    """
    session_set = {d if isinstance(d, date) and not isinstance(d, datetime) else _as_date(d)
                   for d in sessions}
    calendar_dates = list(calendar[date_column])
    trading_set = set(calendar.loc[calendar["is_trading_day"], date_column])
    holiday_set = set(calendar_dates) - trading_set

    missing = sorted(d for d in trading_set if d not in session_set)
    unexpected = sorted(d for d in session_set if d in holiday_set)
    return {
        "calendar_trading_but_no_session": [d.isoformat() for d in missing],
        "session_but_calendar_closed": [d.isoformat() for d in unexpected],
    }


def _as_date(value: object) -> date:
    """Coerce a value into a :class:`datetime.date`."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return pd.Timestamp(value).date()


def summarise_calendar(calendar: pd.DataFrame) -> str:
    """Return a multi-line human summary of a calendar."""
    n = len(calendar)
    trading = int(calendar["is_trading_day"].sum())
    holidays = n - trading
    reasons = (
        calendar.loc[~calendar["is_trading_day"], "holiday_reason"]
        .dropna()
        .value_counts()
        .head(8)
    )
    lines = [
        f"Calendar rows        : {n}",
        f"Trading days         : {trading}",
        f"Holiday days         : {holidays}",
    ]
    if len(reasons):
        lines.append("Top holiday reasons  :")
        for reason, count in reasons.items():
            lines.append(f"    {count:>3} x {reason}")
    return "\n".join(lines)


def default_end_date(settings: Settings | None = None) -> date:
    """Return today's date (the pipeline target)."""
    return date.today()


def date_range(start: date, end: date) -> list[date]:
    """Return every calendar date in ``[start, end]`` inclusive."""
    span = (end - start).days
    return [start + timedelta(days=offset) for offset in range(span + 1)]


__all__ = [
    "CALENDAR_COLUMNS",
    "load_master_calendar",
    "build_trading_calendar",
    "date_range",
    "default_end_date",
    "filter_to_trading_days",
    "get_trading_days",
    "holiday_metadata",
    "load_holidays",
    "reconcile_with_sessions",
    "summarise_calendar",
]
