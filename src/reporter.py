"""Human-readable effects report — the primary research artifact.

Turns the raw correlation table into prose an analyst can read at a glance::

    When Mercury went retrograde (57 events since 2007), Nifty 50 averaged
    +0.42% over the next 5 trading days (base rate +0.11%). Win rate 54.4%.
    The effect is statistically significant at p=0.032.

Both positive *and* negative findings are reported, and null results are
reported too — a study that only prints what it likes is not a study.
Outputs are written to ``reports/effects_summary.md`` and
``reports/effects_summary.json``.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date, datetime
from typing import Mapping, Sequence

import numpy as np
import pandas as pd



# Allow the module to be executed directly (``python src/<module>.py``) as
# well as through ``python -m src.<module>``.
if __package__ in (None, ""):  # pragma: no cover - direct execution path
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

try:
    from .utils import (
        FORWARD_WINDOWS,
        INDEX_LABELS,
        INDEX_NAMES,
        Settings,
        get_logger,
        significance_label,
        write_json,
        write_text,
    )
except ImportError:  # direct script execution
    from src.utils import (
        FORWARD_WINDOWS,
        INDEX_LABELS,
        INDEX_NAMES,
        Settings,
        get_logger,
        significance_label,
        write_json,
        write_text,
    )

logger = get_logger(__name__)

#: The forward window used for the narrative sentences.
HEADLINE_WINDOW = 5

#: Significance threshold used throughout the report.
ALPHA = 0.05


# --------------------------------------------------------------------------- #
# Language
# --------------------------------------------------------------------------- #

def describe_event(event_type: str) -> str:
    """Turn an event label into a readable phrase.

    Args:
        event_type: For example ``"Mercury Retrograde Station"``.

    Returns:
        A phrase such as ``"Mercury went retrograde"``.
    """
    text = event_type.strip()

    if text.endswith("Retrograde Station"):
        return f"{text[: -len(' Retrograde Station')]} went retrograde"
    if text.endswith("Direct Station"):
        return f"{text[: -len(' Direct Station')]} turned direct"
    if text.endswith("Sign Ingress"):
        return f"{text[: -len(' Sign Ingress')]} changed sign"

    for aspect in ("Conjunction", "Trine", "Square", "Opposition"):
        if text.endswith(f" {aspect}") and "-" in text:
            first, second = text[: -len(f" {aspect}")].split("-", 1)
            verb = {
                "Conjunction": "conjoined", "Trine": "formed a trine with",
                "Square": "formed a square with", "Opposition": "opposed",
            }[aspect]
            return f"{first} {verb} {second}"
    return text


def _index_label(index_name: str) -> str:
    """Return a display name for an index."""
    return INDEX_LABELS.get(index_name, index_name.replace("_", " ").title())


def _fmt_pct(value: float | None, digits: int = 2, signed: bool = True) -> str:
    """Format a percentage."""
    if value is None or not np.isfinite(value):
        return "n/a"
    return f"{value:+.{digits}f}%" if signed else f"{value:.{digits}f}%"


def _fmt_pp(value: float | None, digits: int = 2) -> str:
    """Format a percentage-point difference."""
    if value is None or not np.isfinite(value):
        return "n/a"
    return f"{value:+.{digits}f} pp"


def _fmt_p(value: float | None) -> str:
    """Format a p-value."""
    if value is None or not np.isfinite(value):
        return "n/a"
    if value < 0.0001:
        return "p<0.0001"
    return f"p={value:.4f}"


# --------------------------------------------------------------------------- #
# Narrative
# --------------------------------------------------------------------------- #

def render_sentence(row: Mapping[str, object], since_year: int | None = None) -> str:
    """Render one human-readable finding sentence.

    Args:
        row: A row of the correlation results table.
        since_year: Optional year used in the "(N events since YYYY)" clause.

    Returns:
        A single-sentence description of the finding.
    """
    event_type = str(row.get("event_type", ""))
    index_name = str(row.get("index_name", ""))
    window = int(row.get("forward_window", HEADLINE_WINDOW))
    mean_return = row.get("mean_return")
    base_rate = row.get("base_rate")
    win_rate = row.get("win_rate")
    sample_size = int(row.get("sample_size", 0) or 0)
    p_value = row.get("p_value")

    since = f" since {since_year}" if since_year else ""
    plural = "" if sample_size == 1 else "s"
    phrase = describe_event(event_type)

    sentence = f"When {phrase} ({sample_size} event{plural}{since}), "
    sentence += (f"{_index_label(index_name)} averaged {_fmt_pct(mean_return)} over the next "
                 f"{window} trading day{'' if window == 1 else 's'} "
                 f"(base rate {_fmt_pct(base_rate)}).")

    if win_rate is not None and np.isfinite(win_rate):
        sentence += f" Win rate {_fmt_pct(win_rate, 1, signed=False)}."

    excess = row.get("excess_return")
    if excess is not None and np.isfinite(excess) and abs(excess) >= 0.01:
        direction = "above" if excess > 0 else "below"
        sentence += f" That is {_fmt_pp(excess)} {direction} the unconditional baseline."

    nominal = p_value is not None and np.isfinite(p_value) and p_value < ALPHA
    q_value = row.get("q_value_bh")
    has_q = q_value is not None and np.isfinite(q_value)

    if has_q and q_value < ALPHA:
        sentence += (
            f" Statistically significant at p={_fmt_p(p_value)} and after "
            f"Benjamini-Hochberg correction (q={q_value:.4g})."
        )
    elif has_q and nominal:
        sentence += (
            f" Nominally significant at p={_fmt_p(p_value)}, but it does not survive "
            f"Benjamini-Hochberg correction (q={q_value:.4g})."
        )
    elif has_q:
        sentence += (
            f" Not statistically significant (p={_fmt_p(p_value)}, "
            f"q={q_value:.4g} after Benjamini-Hochberg correction)."
        )
    else:
        sentence += f" {significance_label(p_value, ALPHA).capitalize()}."
    return sentence


def _category_heading(category: str) -> str:
    """Return a readable heading for an event category."""
    return {
        "sign_ingress": "Sign ingress (Rashi Sankranti)",
        "retrograde_station": "Retrograde stations (Vakra)",
        "direct_station": "Direct stations (Anuvakra)",
        "conjunction": "Conjunctions (Yuti)",
        "aspect": "Major aspects (Trine / Square / Opposition)",
    }.get(category, category.replace("_", " ").title())


# --------------------------------------------------------------------------- #
# Report assembly
# --------------------------------------------------------------------------- #

@dataclass
class ReportContext:
    """Dataset facts that the report needs but cannot derive on its own."""

    first_date: date | None = None
    last_date: date | None = None
    aligned_rows: int = 0
    index_rows: int = 0
    trading_days: int = 0
    event_count: int = 0
    special_sessions: int = 0
    index_names: Sequence[str] = INDEX_NAMES


def _fmt_p(p_value) -> str:
    """Render a p-value without the misleading "0.0000"."""
    if p_value is None:
        return "n/a"
    try:
        value = float(p_value)
    except (TypeError, ValueError):
        return "n/a"
    if not np.isfinite(value):
        return "n/a"
    if value < 0.0001:
        return "<0.0001"
    return f"{value:.4g}"


def _table(rows: Sequence[Mapping[str, object]], columns: Sequence[tuple[str, str]]) -> str:
    """Render a markdown table."""
    if not rows:
        return "_No data._"
    header = "| " + " | ".join(label for _, label in columns) + " |"
    divider = "| " + " | ".join("---" for _ in columns) + " |"
    body = []
    for row in rows:
        cells = []
        for key, _ in columns:
            value = row.get(key)
            if value is None or (isinstance(value, float) and not np.isfinite(value)):
                cells.append("n/a")
            elif isinstance(value, float):
                cells.append(f"{value:.4g}")
            else:
                cells.append(str(value))
        body.append("| " + " | ".join(cells) + " |")
    return "\n".join([header, divider, *body])


def build_markdown(
    correlations: pd.DataFrame,
    events: pd.DataFrame,
    context: ReportContext | None = None,
    headline_window: int = HEADLINE_WINDOW,
) -> str:
    """Build the full markdown effects report.

    Args:
        correlations: Output of :func:`src.correlation_engine.run_event_study`.
        events: Detected events.
        context: Dataset facts for the header.
        headline_window: Window used for the narrative sentences.

    Returns:
        The complete markdown document.
    """
    context = context or ReportContext()
    lines: list[str] = []
    generated = datetime.now().isoformat(timespec="seconds")

    lines.append("# Celestial Indices — Effects Summary")
    lines.append("")
    lines.append(f"*Generated {generated}*")
    lines.append("")
    lines.append(
        "Every finding below compares the market's forward return around an "
        "astrological event with the unconditional base rate for the same "
        "index and forward window."
    )
    lines.append("")

    # ---------------------------------------------------------------- header
    lines.append("## 1. Dataset")
    lines.append("")
    lines.append("| Item | Value |")
    lines.append("| --- | --- |")
    lines.append(f"| Aligned trading days | {context.aligned_rows:,} |")
    lines.append(f"| Index bars (date x index) | {context.index_rows:,} |")
    lines.append(f"| Calendar trading days | {context.trading_days:,} |")
    lines.append(f"| Planetary events detected | {context.event_count:,} |")
    lines.append(f"| Special (Muhurat) sessions retained | {context.special_sessions:,} |")
    lines.append(
        f"| Date range | {context.first_date} to {context.last_date} |"
    )
    lines.append(
        "| Indices | " + ", ".join(_index_label(n) for n in context.index_names) + " |"
    )
    lines.append("")
    if events is not None and len(events):
        lines.append("Events by category:")
        lines.append("")
        lines.append("| Category | Events | Distinct event types |")
        lines.append("| --- | --- | --- |")
        for category, group in events.groupby("category"):
            lines.append(
                f"| {_category_heading(category)} | {len(group):,} | {group['event_type'].nunique()} |"
            )
        lines.append("")

    # ------------------------------------------------------------- method
    lines.append("## 2. Method")
    lines.append("")
    lines.append(
        "* Forward returns are close-to-close over **trading** days, so "
        "weekends and holidays never stretch a window."
    )
    lines.append(
        "* Windows studied: " + ", ".join(f"{w}d" for w in FORWARD_WINDOWS) + "."
    )
    lines.append(
        "* An event falling on a non-trading day is attributed to the next "
        "trading session — the first session in which it could be traded."
    )
    lines.append(
        "* `base_rate` is the unconditional mean forward return for that index "
        "and window across every session."
    )
    lines.append(
        "* `p_value` comes from Welch's two-sample t-test comparing event "
        "windows against the full unconditional distribution; a one-sample test "
        "against the base rate is also computed and stored."
    )
    lines.append(
        "* **Multiple testing.** Several thousand event x index x window "
        "combinations are tested at once, so the nominal p-value is optimistic. "
        "Every result therefore also carries a **Benjamini-Hochberg q-value** "
        "that controls the false discovery rate across the whole study, and the "
        "headline sections are reported on the corrected basis."
    )
    lines.append(
        "* **Caveat:** overlapping forward windows make consecutive event "
        "observations correlated, so p-values are optimistic for densely "
        "clustered event types. Treat effect sizes and direction as the "
        "primary evidence, not the p-value alone."
    )
    lines.append("")

    if correlations is None or len(correlations) == 0:
        lines.append("## 3. Findings")
        lines.append("")
        lines.append("_No correlation results are available yet._")
        lines.append("")
        return "\n".join(lines)

    headline = correlations.loc[correlations["forward_window"] == headline_window].copy()
    since_years: dict[str, int] = {}
    if events is not None and len(events):
        since_years = {
            event_type: int(pd.to_datetime(group["date"]).min().year)
            for event_type, group in events.groupby("event_type")
        }

    # --------------------------------------------------------- headline table
    lines.append(f"## 3. Headline results ({headline_window}-day forward window)")
    lines.append("")
    lines.append(
        "Mean forward return around each event, the unconditional base rate, "
        "and the two-sided p-value."
    )
    lines.append("")
    category_order = {
        "sign_ingress": 0, "retrograde_station": 1, "direct_station": 2,
        "conjunction": 3, "aspect": 4,
    }
    headline = headline.assign(
        _order=headline["category"].map(category_order).fillna(99)
    ).sort_values(["_order", "event_type", "index_name"])
    headline_rows = []
    for _, row in headline.iterrows():
        headline_rows.append({
            "event": row["event_type"],
            "index": _index_label(row["index_name"]),
            "n": int(row["sample_size"]),
            "mean": row["mean_return"],
            "base": row["base_rate"],
            "excess": row["excess_return"],
            "win": row["win_rate"],
            "p": row["p_value"],
            "q": row.get("q_value_bh"),
            "bh": "yes" if bool(row.get("is_significant_bh")) else "no",
        })
    lines.append(_table(headline_rows, [
        ("event", "Event"), ("index", "Index"), ("n", "N"),
        ("mean", "Mean ret"), ("base", "Base rate"), ("excess", "Excess"),
        ("win", "Win %"), ("p", "p-value"), ("q", "q (BH)"), ("bh", "BH sig"),
    ]))
    lines.append("")

    # ---------------------------------------------------------- narrative
    lines.append(f"## 4. Findings in words ({headline_window}-day window)")
    lines.append("")
    for category in sorted(headline["category"].unique()):
        category_rows = headline.loc[headline["category"] == category]
        lines.append(f"### {_category_heading(category)}")
        lines.append("")
        for event_type in sorted(category_rows["event_type"].unique()):
            subset = category_rows.loc[category_rows["event_type"] == event_type]
            year = since_years.get(event_type)
            for _, row in subset.iterrows():
                lines.append(f"* {render_sentence(row.to_dict(), since_year=year)}")
            lines.append("")
        lines.append(f"**All windows — {_category_heading(category)}**")
        lines.append("")
        detail_rows = []
        for _, row in correlations.loc[correlations["category"] == category].sort_values(
            ["event_type", "index_name", "forward_window"]
        ).iterrows():
            detail_rows.append({
                "event": row["event_type"],
                "index": _index_label(row["index_name"]),
                "w": int(row["forward_window"]),
                "n": int(row["sample_size"]),
                "mean": row["mean_return"],
                "base": row["base_rate"],
                "excess": row["excess_return"],
                "win": row["win_rate"],
                "p": row["p_value"],
                "q": row.get("q_value_bh"),
            })
        lines.append(_table(detail_rows, [
            ("event", "Event"), ("index", "Index"), ("w", "Window"),
            ("n", "N"), ("mean", "Mean ret"), ("base", "Base rate"),
            ("excess", "Excess"), ("win", "Win %"), ("p", "p-value"),
            ("q", "q (BH)"),
        ]))
        lines.append("")

    # ------------------------------------------------------------ highlights
    lines.append("## 5. Highlights")
    lines.append("")
    MIN_HIGHLIGHT_N = 10
    has_bh = "is_significant_bh" in headline.columns
    if has_bh:
        significant = headline.loc[
            headline["is_significant_bh"] & (headline["sample_size"] >= MIN_HIGHLIGHT_N)
        ]
    else:
        significant = headline.loc[
            (headline["p_value"] < ALPHA) & (headline["sample_size"] >= MIN_HIGHLIGHT_N)
        ]
    positive = significant.loc[significant["excess_return"] > 0].sort_values(
        "excess_return", ascending=False
    )
    negative = significant.loc[significant["excess_return"] < 0].sort_values(
        "excess_return"
    )

    lines.append(
        f"Only combinations with at least {MIN_HIGHLIGHT_N} observations that survive "
        f"Benjamini-Hochberg correction at q<{ALPHA} are listed below."
    )
    lines.append("")
    lines.append("### Strongest positive findings")
    lines.append("")
    if len(positive):
        for _, row in positive.head(12).iterrows():
            lines.append(f"* {render_sentence(row.to_dict(), since_year=since_years.get(row['event_type']))}")
    else:
        lines.append("* No statistically significant positive effects were found.")
    lines.append("")

    lines.append("### Strongest negative findings")
    lines.append("")
    if len(negative):
        for _, row in negative.head(12).iterrows():
            lines.append(f"* {render_sentence(row.to_dict(), since_year=since_years.get(row['event_type']))}")
    else:
        lines.append("* No statistically significant negative effects were found.")
    lines.append("")

    lines.append("### Null results")
    lines.append("")
    null_mask = (
        ~headline["is_significant_bh"] if has_bh else (headline["p_value"] >= ALPHA)
    )
    null_rows = headline.loc[
        null_mask & (headline["sample_size"] >= 20)
    ].sort_values("excess_return", key=lambda s: s.abs(), ascending=False)
    if len(null_rows):
        lines.append(
            f"{len(null_rows)} event/index combinations with at least 20 observations "
            "showed no effect that survives multiple-testing correction. The largest "
            "absolute differences from the base rate were:"
        )
        lines.append("")
        null_table = []
        for _, row in null_rows.head(15).iterrows():
            q_value = row.get("q_value_bh")
            null_table.append({
                "event": row["event_type"],
                "index": _index_label(row["index_name"]),
                "n": int(row["sample_size"]),
                "mean": row["mean_return"],
                "base": row["base_rate"],
                "excess": row["excess_return"],
                "p": _fmt_p(row["p_value"]),
                "q": None if q_value is None or not np.isfinite(q_value)
                      else f"{q_value:.4g}",
            })
        lines.append(_table(null_table, [
            ("event", "Event"), ("index", "Index"), ("n", "N"),
            ("mean", "Mean ret"), ("base", "Base rate"),
            ("excess", "Excess"), ("p", "p-value"), ("q", "q-value (BH)"),
        ]))
    else:
        lines.append("* Every combination with at least 20 observations reached p<0.05.")
    lines.append("")

    # ----------------------------------------------------------- roll-ups
    lines.append("## 6. Category roll-ups")
    lines.append("")
    lines.append(
        "Every event type inside a category pooled together, weighted by "
        "sample size.  This is the broadest view of the dataset."
    )
    lines.append("")
    rollup_rows = []
    for (category, index_name, window), group in correlations.groupby(
        ["category", "index_name", "forward_window"]
    ):
        total_n = int(group["sample_size"].sum())
        if total_n == 0:
            continue
        weights = group["sample_size"].to_numpy(dtype=float)
        weighted_mean = float(np.average(group["mean_return"].to_numpy(dtype=float),
                                         weights=weights))
        base = float(group["base_rate"].dropna().mean())
        rollup_rows.append({
            "category": _category_heading(category),
            "index": _index_label(index_name),
            "w": int(window),
            "n": total_n,
            "mean": weighted_mean,
            "base": base,
            "excess": weighted_mean - base,
            "win": float(np.average(group["win_rate"].to_numpy(dtype=float),
                                    weights=weights)),
            "p": float(group["p_value"].min()),
            "q": float(group["q_value_bh"].min()) if "q_value_bh" in group else np.nan,
        })
    rollup_rows.sort(key=lambda r: (r["category"], r["index"], r["w"]))
    lines.append(_table(rollup_rows, [
        ("category", "Category"), ("index", "Index"), ("w", "Window"),
        ("n", "N"), ("mean", "Mean ret"), ("base", "Base rate"),
        ("excess", "Excess"), ("win", "Win %"), ("p", "Best p"),
        ("q", "Best q (BH)"),
    ]))
    lines.append("")
    lines.append(
        "The complete row-level table (every event type, every index, every "
        "window) is in `reports/effects_summary.json` and "
        "`data/processed/correlation_results.csv`."
    )
    lines.append("")

    lines.append("## 7. How to read this")
    lines.append("")
    lines.append(
        "* **Mean ret** is the average forward return over the sessions "
        "following the event."
    )
    lines.append(
        "* **Base rate** is the average forward return over all sessions, "
        "regardless of events."
    )
    lines.append("* **Excess** is the difference between the two, in percentage points.")
    lines.append("* **Win %** is the share of event windows with a positive return.")
    lines.append(
        "* **p-value** is the two-sided probability under the null hypothesis "
        "that event windows behave like any other window."
    )
    lines.append(
        "* A large sample with a small effect is still a small effect; a small "
        "sample with a large effect is suggestive but fragile."
    )
    lines.append("")
    lines.append(
        "_No claim is made that planetary positions cause price movement. This "
        "report quantifies what the historical data shows, including the cases "
        "where it shows nothing._"
    )
    lines.append("")
    return "\n".join(lines)


def build_payload(
    correlations: pd.DataFrame,
    events: pd.DataFrame,
    context: ReportContext | None = None,
    headline_window: int = HEADLINE_WINDOW,
) -> dict:
    """Build the machine-readable JSON companion to the markdown report."""
    context = context or ReportContext()
    payload: dict = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "headline_window": headline_window,
        "alpha": ALPHA,
        "dataset": {
            "aligned_rows": context.aligned_rows,
            "index_rows": context.index_rows,
            "trading_days": context.trading_days,
            "event_count": context.event_count,
            "special_sessions": context.special_sessions,
            "first_date": str(context.first_date) if context.first_date else None,
            "last_date": str(context.last_date) if context.last_date else None,
            "indices": list(context.index_names),
        },
        "findings": [],
        "results": [],
    }

    if correlations is not None and len(correlations):
        headline = correlations.loc[correlations["forward_window"] == headline_window]
        since_years: dict[str, int] = {}
        if events is not None and len(events):
            since_years = {
                event_type: int(pd.to_datetime(group["date"]).min().year)
                for event_type, group in events.groupby("event_type")
            }
        for _, row in headline.iterrows():
            record = row.to_dict()
            record["index_label"] = _index_label(row["index_name"])
            record["narrative"] = render_sentence(
                record, since_year=since_years.get(row["event_type"])
            )
            payload["findings"].append(record)

        for _, row in correlations.iterrows():
            record = row.to_dict()
            for key in ("first_event_date", "last_event_date"):
                value = record.get(key)
                if value is not None and not isinstance(value, str):
                    record[key] = str(value)
            payload["results"].append(record)

    return payload


def generate_reports(
    correlations: pd.DataFrame,
    events: pd.DataFrame,
    settings: Settings | None = None,
    aligned_rows: int = 0,
    index_rows: int = 0,
    trading_days: int = 0,
    first_date: date | None = None,
    last_date: date | None = None,
    special_sessions: int = 0,
    headline_window: int = HEADLINE_WINDOW,
) -> dict[str, str]:
    """Write ``effects_summary.md`` and ``effects_summary.json``.

    Args:
        correlations: Event-study results.
        events: Detected events.
        settings: Runtime settings (controls the output directory).
        aligned_rows: Number of aligned trading days.
        index_rows: Number of index bars.
        trading_days: Number of calendar trading days.
        first_date: First date in the dataset.
        last_date: Last date in the dataset.
        headline_window: Window used for the narrative.

    Returns:
        Mapping of report name to the written path.
    """
    settings = settings or Settings.from_env()
    reports_dir = settings.reports_dir
    reports_dir.mkdir(parents=True, exist_ok=True)

    context = ReportContext(
        first_date=first_date,
        last_date=last_date,
        aligned_rows=aligned_rows,
        index_rows=index_rows,
        trading_days=trading_days,
        event_count=int(len(events)) if events is not None else 0,
        special_sessions=special_sessions,
        index_names=sorted(
            set(correlations["index_name"]) if correlations is not None and len(correlations)
            else INDEX_NAMES
        ),
    )

    markdown = build_markdown(correlations, events, context, headline_window)
    payload = build_payload(correlations, events, context, headline_window)

    md_path = reports_dir / "effects_summary.md"
    json_path = reports_dir / "effects_summary.json"
    write_text(md_path, markdown)
    write_json(json_path, payload)

    logger.info("Effects report written: %s", md_path)
    logger.info("Effects payload written: %s", json_path)
    return {"markdown": str(md_path), "json": str(json_path)}


__all__ = [
    "ALPHA",
    "main",
    "HEADLINE_WINDOW",
    "ReportContext",
    "build_markdown",
    "build_payload",
    "describe_event",
    "generate_reports",
    "render_sentence",
]


# --------------------------------------------------------------------------- #
# Script entry point
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    """Render the effects report from the processed artefacts.

    Usage::

        python src/reporter.py
    """
    import argparse

    try:
        from .utils import PROCESSED_DIR, Settings, ensure_dirs, setup_logging
    except ImportError:  # direct script execution
        from src.utils import PROCESSED_DIR, Settings, ensure_dirs, setup_logging

    parser = argparse.ArgumentParser(description="Render the effects summary.")
    parser.add_argument("--correlations", default=None,
                        help="Path to correlation_results.csv")
    parser.add_argument("--events", default=None,
                        help="Path to planetary_events.csv")
    parser.add_argument("--aligned", default=None,
                        help="Path to aligned_master.parquet (for coverage facts)")
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args(argv)

    setup_logging(args.log_level)
    settings = Settings.from_env()
    ensure_dirs()

    correlations_path = (Path(args.correlations) if args.correlations
                         else settings.processed_data_dir / "correlation_results.csv")
    events_path = (Path(args.events) if args.events
                   else settings.processed_data_dir / "planetary_events.csv")
    aligned_path = (Path(args.aligned) if args.aligned
                    else settings.processed_data_dir / "aligned_master.parquet")
    if not correlations_path.exists():
        print(f"Correlation results not found at {correlations_path}. "
              "Run src/correlation_engine.py first.", file=sys.stderr)
        return 1

    correlations = pd.read_csv(correlations_path)
    events = (pd.read_csv(events_path) if events_path.exists() else pd.DataFrame())

    aligned_rows = index_rows = trading_days = 0
    first_date = last_date = None
    if aligned_path.exists():
        aligned = pd.read_parquet(aligned_path)
        aligned["date"] = pd.to_datetime(aligned["date"]).dt.date
        aligned_rows = int(aligned["date"].nunique())
        index_rows = int(len(aligned))
        first_date = aligned["date"].min()
        last_date = aligned["date"].max()
        trading_days = aligned_rows

    paths = generate_reports(
        correlations, events, settings=settings,
        aligned_rows=aligned_rows, index_rows=index_rows,
        trading_days=trading_days, first_date=first_date, last_date=last_date,
    )
    for key, value in paths.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
