"""Forward-return event studies.

For every detected event type and every index, this module measures what the
market did *after* the event and compares it with the unconditional baseline.

Methodology
-----------
* Forward returns are close-to-close over N **trading** days (1, 3, 5, 10, 20),
  so weekends and holidays never stretch a window.
* An event that falls on a non-trading day is attributed to the next trading
  session, which is the first session an investor could react to it.
* ``base_rate`` is the unconditional mean forward return for that index and
  window across all sessions.
* ``t_stat`` / ``p_value`` come from Welch's two-sample t-test comparing the
  event-window returns against the full unconditional distribution.  A
  one-sample test against the base rate is reported alongside as
  ``one_sample_p``.

Overlapping forward windows mean consecutive event observations are not fully
independent; the report states this caveat explicitly rather than hiding it.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Iterable, Sequence

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats



# Allow the module to be executed directly (``python src/<module>.py``) as
# well as through ``python -m src.<module>``.
if __package__ in (None, ""):  # pragma: no cover - direct execution path
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

try:
    from .utils import FORWARD_WINDOWS, INDEX_NAMES, get_logger
except ImportError:  # direct script execution
    from src.utils import FORWARD_WINDOWS, INDEX_NAMES, get_logger

logger = get_logger(__name__)

RESULT_COLUMNS: tuple[str, ...] = (
    "event_type", "category", "index_name", "forward_window",
    "mean_return", "median_return", "win_rate", "sample_size",
    "t_stat", "p_value", "base_rate",
    "std_return", "excess_return", "base_median_return", "base_win_rate",
    "one_sample_t", "one_sample_p", "first_event_date", "last_event_date",
    "q_value_bh", "is_significant_bh",
)


# --------------------------------------------------------------------------- #
# Forward returns
# --------------------------------------------------------------------------- #

def forward_returns(closes: Sequence[float], window: int) -> np.ndarray:
    """Return forward close-to-close returns (in percent) for each bar.

    Args:
        closes: Ordered closing prices.
        window: Number of trading days to look ahead.

    Returns:
        Array of length ``len(closes) - window`` holding percentage returns.
    """
    values = np.asarray(closes, dtype=float)
    if values.size <= window:
        return np.empty(0, dtype=float)
    future = values[window:]
    past = values[: values.size - window]
    with np.errstate(divide="ignore", invalid="ignore"):
        returns = (future / past - 1.0) * 100.0
    return returns[np.isfinite(returns)]


def _index_series(aligned_long: pd.DataFrame, index_name: str) -> pd.DataFrame:
    """Return the ordered bars of one index."""
    subset = aligned_long.loc[aligned_long["index_name"] == index_name]
    return subset.sort_values("date").reset_index(drop=True)


def _map_event_to_session(
    event_dates: Iterable[date],
    session_dates: Sequence[date],
) -> list[tuple[date, date]]:
    """Map calendar event dates onto the next available trading session.

    Args:
        event_dates: Calendar dates on which events occurred.
        session_dates: Ordered trading dates of the index.

    Returns:
        List of ``(event_date, session_date)`` pairs; events after the last
        usable session are dropped.
    """
    if not session_dates:
        return []
    sessions = list(session_dates)
    mapped: list[tuple[date, date]] = []
    for event_date in sorted(set(event_dates)):
        key = np.searchsorted(sessions, event_date, side="left")
        if key >= len(sessions):
            continue
        mapped.append((event_date, sessions[key]))
    return mapped


# --------------------------------------------------------------------------- #
# Statistical helpers
# --------------------------------------------------------------------------- #

@dataclass
class TTestResult:
    """Outcome of the two tests used for each (event, index, window) cell."""

    t_stat: float
    p_value: float
    one_sample_t: float
    one_sample_p: float


def compare_to_baseline(
    sample: np.ndarray,
    population: np.ndarray,
    base_rate: float,
) -> TTestResult:
    """Compare an event sample with the unconditional distribution.

    Args:
        sample: Forward returns observed around events.
        population: All forward returns for the index and window.
        base_rate: Unconditional mean forward return.

    Returns:
        :class:`TTestResult` with the Welch statistics and the one-sample
        statistics against the base rate.
    """
    empty = TTestResult(np.nan, np.nan, np.nan, np.nan)
    if sample.size < 2 or population.size < 2:
        return empty

    try:
        result = stats.ttest_ind(sample, population, equal_var=False)
        t_stat = float(result.statistic)
        p_value = float(result.pvalue)
    except Exception:  # pragma: no cover - degenerate input
        t_stat, p_value = np.nan, np.nan

    try:
        one = stats.ttest_1samp(sample, base_rate)
        one_t = float(one.statistic)
        one_p = float(one.pvalue)
    except Exception:  # pragma: no cover - degenerate input
        one_t, one_p = np.nan, np.nan

    if not np.isfinite(t_stat):
        t_stat = np.nan
    if not np.isfinite(p_value):
        p_value = np.nan
    return TTestResult(t_stat, p_value, one_t, one_p)


# --------------------------------------------------------------------------- #
# Multiple-testing correction
# --------------------------------------------------------------------------- #

def benjamini_hochberg(p_values: Sequence[float]) -> np.ndarray:
    """Return Benjamini-Hochberg adjusted q-values for a list of p-values.

    The procedure controls the false discovery rate: instead of asking
    "what is the probability this one test is a false positive?", it asks
    "what is the expected proportion of false positives among the tests I
    declare significant?".  With several thousand event/horizon/index
    combinations, the unadjusted p-value is badly optimistic, so the
    q-value is the honest summary.

    Args:
        p_values: Raw two-sided p-values; ``NaN`` entries are ignored.

    Returns:
        Array of q-values aligned with the input, in ``[0, 1]``.
    """
    values = np.asarray(p_values, dtype=float)
    q_values = np.full(values.shape, np.nan, dtype=float)
    valid = np.flatnonzero(np.isfinite(values))
    if valid.size == 0:
        return q_values

    order = valid[np.argsort(values[valid])]
    m = order.size
    ranked = values[order] * m / np.arange(1, m + 1)
    # Enforce monotonicity from the largest p-value downwards.
    ranked = np.minimum.accumulate(ranked[::-1])[::-1]
    q_values[order] = np.clip(ranked, 0.0, 1.0)
    return q_values


def apply_bh_correction(
    results: pd.DataFrame,
    alpha: float = 0.05,
    group_column: str | None = None,
) -> pd.DataFrame:
    """Add Benjamini-Hochberg q-values to an event-study result frame.

    Args:
        results: Frame with a ``p_value`` column.
        alpha: Significance level used for the boolean flag.
        group_column: Optional column to correct within (e.g. ``"category"``).
            When omitted, the correction is applied across every test at once.

    Returns:
        The frame with ``q_value_bh`` and ``is_significant_bh`` added.
    """
    if results is None or len(results) == 0:
        return results

    frame = results.copy()
    frame["q_value_bh"] = np.nan
    frame["is_significant_bh"] = False

    groups = (
        [frame[group_column].fillna("__all__")]
        if group_column and group_column in frame.columns
        else [pd.Series(["__all__"] * len(frame), index=frame.index)]
    )
    for keys in groups:
        mask = keys == keys.iloc[0] if group_column else pd.Series(True, index=frame.index)
        indices = frame.index[mask]
        if len(indices) == 0:
            continue
        q_values = benjamini_hochberg(frame.loc[indices, "p_value"].to_numpy(dtype=float))
        frame.loc[indices, "q_value_bh"] = q_values
        frame.loc[indices, "is_significant_bh"] = np.isfinite(q_values) & (q_values < alpha)

    return frame


# --------------------------------------------------------------------------- #
# Engine
# --------------------------------------------------------------------------- #

def run_event_study(
    aligned_long: pd.DataFrame,
    events: pd.DataFrame,
    windows: Sequence[int] = FORWARD_WINDOWS,
    index_names: Sequence[str] = INDEX_NAMES,
) -> pd.DataFrame:
    """Run the forward-return event study.

    Args:
        aligned_long: Long aligned dataset (one row per date x index).
        events: Event table produced by :func:`src.event_detector.detect_events`.
        windows: Forward windows in trading days.
        index_names: Indices to analyse.

    Returns:
        DataFrame with one row per ``(event_type, index_name, forward_window)``.
    """
    if aligned_long is None or len(aligned_long) == 0:
        return pd.DataFrame(columns=list(RESULT_COLUMNS))
    if events is None or len(events) == 0:
        return pd.DataFrame(columns=list(RESULT_COLUMNS))

    rows: list[dict] = []
    grouped_events = {
        (event_type, category): group
        for (event_type, category), group in events.groupby(["event_type", "category"])
    }

    for index_name in index_names:
        series = _index_series(aligned_long, index_name)
        if series.empty:
            logger.warning("No aligned rows for index %s", index_name)
            continue

        session_dates = list(series["date"])
        closes = series["close"].to_numpy(dtype=float)

        returns_by_window: dict[int, np.ndarray] = {
            window: forward_returns(closes, window) for window in windows
        }
        # A forward return at position i uses the close at i + window, so it is
        # only defined for i <= len(closes) - window - 1.
        usable = {window: len(closes) - window - 1 for window in windows}

        for (event_type, category), group in grouped_events.items():
            event_dates = list(group["date"])
            mapped = _map_event_to_session(event_dates, session_dates)
            if not mapped:
                continue

            positions: list[int] = []
            session_for_position: list[date] = []
            lookup = {value: position for position, value in enumerate(session_dates)}
            for _, session in mapped:
                position = lookup[session]
                if position >= usable[min(windows)]:
                    continue
                positions.append(position)
                session_for_position.append(session)
            if not positions:
                continue

            first_event = min(event_dates)
            last_event = max(event_dates)
            orbs = group["orb"].dropna()
            mean_orb = float(orbs.mean()) if len(orbs) else np.nan

            for window in windows:
                returns = returns_by_window[window]
                if returns.size == 0:
                    continue
                limit = usable[window]
                valid = [p for p in positions if p < limit]
                if len(valid) < 1:
                    continue
                sample = returns[np.asarray(valid, dtype=int)]

                population = returns
                base_rate = float(np.mean(population)) if population.size else np.nan
                stats_result = compare_to_baseline(sample, population, base_rate)

                mean_return = float(np.mean(sample))
                median_return = float(np.median(sample))
                win_rate = float(np.mean(sample > 0)) * 100.0

                rows.append({
                    "event_type": event_type,
                    "category": category,
                    "index_name": index_name,
                    "forward_window": window,
                    "mean_return": mean_return,
                    "median_return": median_return,
                    "win_rate": win_rate,
                    "sample_size": int(sample.size),
                    "t_stat": stats_result.t_stat,
                    "p_value": stats_result.p_value,
                    "base_rate": base_rate,
                    "std_return": float(np.std(sample, ddof=1)) if sample.size > 1 else np.nan,
                    "excess_return": (
                        mean_return - base_rate if np.isfinite(base_rate) else np.nan
                    ),
                    "base_median_return": (
                        float(np.median(population)) if population.size else np.nan
                    ),
                    "base_win_rate": (
                        float(np.mean(population > 0)) * 100.0 if population.size else np.nan
                    ),
                    "one_sample_t": stats_result.one_sample_t,
                    "one_sample_p": stats_result.one_sample_p,
                    "first_event_date": first_event,
                    "last_event_date": last_event,
                    "mean_orb": mean_orb,
                })

    results = pd.DataFrame(rows)
    if results.empty:
        return pd.DataFrame(columns=list(RESULT_COLUMNS))

    results = results.sort_values(
        ["category", "event_type", "index_name", "forward_window"]
    ).reset_index(drop=True)
    results = apply_bh_correction(results, alpha=0.05)

    significant = int((results["p_value"] < 0.05).sum())
    significant_bh = int(results["is_significant_bh"].sum())
    logger.info(
        "Event study complete: %d rows, %d cells at p<0.05, %d survive Benjamini-Hochberg",
        len(results), significant, significant_bh,
    )
    return results


def event_level_returns(
    aligned_long: pd.DataFrame,
    events: pd.DataFrame,
    windows: Sequence[int] = FORWARD_WINDOWS,
    index_names: Sequence[str] = INDEX_NAMES,
) -> pd.DataFrame:
    """Return the per-event forward returns used by the event-study tab.

    Args:
        aligned_long: Long aligned dataset.
        events: Event table.
        windows: Forward windows.
        index_names: Indices to analyse.

    Returns:
        DataFrame with one row per ``(event_id, index_name)``.
    """
    if aligned_long is None or len(aligned_long) == 0 or events is None or len(events) == 0:
        return pd.DataFrame()

    frames: list[pd.DataFrame] = []
    for index_name in index_names:
        series = _index_series(aligned_long, index_name)
        if series.empty:
            continue
        session_dates = list(series["date"])
        closes = series["close"].to_numpy(dtype=float)

        mapped = _map_event_to_session(events["date"], session_dates)
        if not mapped:
            continue
        lookup = {value: position for position, value in enumerate(session_dates)}

        event_dates = list(events["date"])
        sessions = [m[1] for m in mapped]
        positions = [lookup[s] for s in sessions]

        records = []
        for event_index, (event_date, session) in enumerate(zip(event_dates, sessions)):
            position = positions[event_index]
            record = {
                "event_id": int(events.iloc[event_index]["event_id"]),
                "event_date": event_date,
                "session_date": session,
                "event_type": events.iloc[event_index]["event_type"],
                "category": events.iloc[event_index]["category"],
                "planets": events.iloc[event_index]["planets"],
                "description": events.iloc[event_index]["description"],
                "orb": events.iloc[event_index].get("orb"),
                "index_name": index_name,
                "close_at_event": float(closes[position]) if position < len(closes) else np.nan,
            }
            for window in windows:
                target = position + window
                record[f"ret_{window}d"] = (
                    float((closes[target] / closes[position] - 1.0) * 100.0)
                    if target < len(closes) and closes[position] else np.nan
                )
            records.append(record)
        frames.append(pd.DataFrame(records))

    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def roll_up_by_category(results: pd.DataFrame) -> pd.DataFrame:
    """Aggregate event-type level results into category level results.

    Returns:
        DataFrame with one row per ``(category, index_name, forward_window)``.
    """
    if results is None or len(results) == 0:
        return pd.DataFrame()

    records = []
    for (category, index_name, window), group in results.groupby(
        ["category", "index_name", "forward_window"]
    ):
        total_n = int(group["sample_size"].sum())
        if total_n == 0:
            continue
        weighted_mean = float(
            np.average(
                group["mean_return"].fillna(0.0),
                weights=group["sample_size"].fillna(0.0),
            )
        )
        weighted_median = float(group["median_return"].fillna(0.0).mean())
        weighted_win = float(
            np.average(
                group["win_rate"].fillna(0.0),
                weights=group["sample_size"].fillna(0.0),
            )
        )
        best = group.loc[group["p_value"].idxmin()] if group["p_value"].notna().any() else None
        records.append({
            "category": category,
            "index_name": index_name,
            "forward_window": window,
            "mean_return": weighted_mean,
            "median_return": weighted_median,
            "win_rate": weighted_win,
            "sample_size": total_n,
            "base_rate": float(group["base_rate"].dropna().mean()) if group["base_rate"].notna().any() else np.nan,
            "excess_return": (
                weighted_mean - float(group["base_rate"].dropna().mean())
                if group["base_rate"].notna().any() else np.nan
            ),
            "best_event_type": best["event_type"] if best is not None else None,
            "best_p_value": float(best["p_value"]) if best is not None else np.nan,
        })
    return pd.DataFrame(records)


__all__ = [
    "RESULT_COLUMNS",
    "TTestResult",
    "apply_bh_correction",
    "benjamini_hochberg",
    "compare_to_baseline",
    "event_level_returns",
    "forward_returns",
    "main",
    "roll_up_by_category",
    "run_event_study",
]


# --------------------------------------------------------------------------- #
# Script entry point
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    """Run the event study from the processed artefacts and save the results.

    Usage::

        python src/correlation_engine.py
    """
    import argparse

    try:
        from .utils import Settings, ensure_dirs, setup_logging
    except ImportError:  # direct script execution
        from src.utils import Settings, ensure_dirs, setup_logging

    parser = argparse.ArgumentParser(description="Run the forward-return event study.")
    parser.add_argument("--aligned", default=None,
                        help="Path to aligned_master.parquet (default: data/processed)")
    parser.add_argument("--events", default=None,
                        help="Path to planetary_events.csv (default: data/processed)")
    parser.add_argument("--output", default=None,
                        help="Path for the correlation CSV (default: data/processed/correlation_results.csv)")
    parser.add_argument("--alpha", type=float, default=0.05,
                        help="Benjamini-Hochberg significance level")
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args(argv)

    setup_logging(args.log_level)
    settings = Settings.from_env()
    ensure_dirs()

    aligned_path = Path(args.aligned) if args.aligned else (settings.processed_data_dir / "aligned_master.parquet")
    events_path = Path(args.events) if args.events else (settings.processed_data_dir / "planetary_events.csv")
    if not aligned_path.exists():
        print(f"Aligned master not found at {aligned_path}. Run the pipeline first.", file=sys.stderr)
        return 1
    if not events_path.exists():
        print(f"Events not found at {events_path}. Run src/event_detector.py first.", file=sys.stderr)
        return 1

    aligned = pd.read_parquet(aligned_path)
    aligned["date"] = pd.to_datetime(aligned["date"]).dt.date
    events = pd.read_csv(events_path)
    events["date"] = pd.to_datetime(events["date"]).dt.date

    results = run_event_study(aligned, events)
    results = apply_bh_correction(results, alpha=args.alpha)

    destination = Path(args.output) if args.output else (settings.processed_data_dir / "correlation_results.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy = results.copy()
    for column in ("first_event_date", "last_event_date"):
        if column in copy.columns:
            copy[column] = copy[column].astype(str)
    copy.to_csv(destination, index=False)
    try:
        copy.to_parquet(destination.with_suffix(".parquet"), index=False)
    except Exception as exc:  # pragma: no cover
        logger.warning("Parquet write failed: %s", exc)

    print(f"Computed {len(results):,} correlation rows -> {destination}")
    print(f"  significant at p<{args.alpha}:            {int((results['p_value'] < args.alpha).sum()):,}")
    print(f"  significant after Benjamini-Hochberg: {int(results['is_significant_bh'].sum()):,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
