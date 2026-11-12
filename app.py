"""Celestial Indices — Streamlit application.

Six tabs:

1. **Index Explorer** — candlestick + volume with a date range.
2. **Planetary Timeline** — sign chart and event heatmap.
3. **Correlation Heatmap** — events x indices x win rate / excess return.
4. **Event Study** — forward-return bars for a selected event.
5. **Effects Report** — the markdown research report.
6. **Data Export** — download the aligned dataset, events and correlations.

Run with::

    streamlit run app.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.db.session import latest_pipeline_run, table_counts  # noqa: E402
from src.live_update import read_status, run_update  # noqa: E402
from src.utils import (  # noqa: E402
    ALIGNED_CSV,
    ALIGNMENT_REPORT,
    CORRELATIONS_CSV,
    EFFECTS_MD,
    EVENTS_CSV,
    INDEX_LABELS,
    INDEX_NAMES,
    PLANETS,
    PROCESSED_DIR,
    SIGN_ABBR,
    Settings,
    get_logger,
    setup_logging,
)

st.set_page_config(
    page_title="Celestial Indices",
    page_icon="*",
    layout="wide",
    initial_sidebar_state="expanded",
)

setup_logging("WARNING")
logger = get_logger("app")

SETTINGS = Settings.from_env()

# --------------------------------------------------------------------------- #
# Data loading
# --------------------------------------------------------------------------- #

@st.cache_data(show_spinner="Loading the aligned dataset ...")
def load_aligned() -> pd.DataFrame:
    """Load the aligned master (one row per date x index)."""
    parquet = PROCESSED_DIR / "aligned_master.parquet"
    if parquet.exists():
        frame = pd.read_parquet(parquet)
    elif ALIGNED_CSV.exists():
        frame = pd.read_csv(ALIGNED_CSV)
    else:
        return pd.DataFrame()
    frame["date"] = pd.to_datetime(frame["date"]).dt.date
    return frame


@st.cache_data(show_spinner="Loading the daily view ...")
def load_daily() -> pd.DataFrame:
    """Load the wide daily view (one row per trading day)."""
    parquet = PROCESSED_DIR / "aligned_master_daily.parquet"
    if parquet.exists():
        frame = pd.read_parquet(parquet)
    else:
        csv = PROCESSED_DIR / "aligned_master_daily.csv"
        if not csv.exists():
            return pd.DataFrame()
        frame = pd.read_csv(csv)
    frame["date"] = pd.to_datetime(frame["date"]).dt.date
    return frame


@st.cache_data(show_spinner="Loading events ...")
def load_events() -> pd.DataFrame:
    """Load the detected planetary events."""
    if EVENTS_CSV.exists():
        frame = pd.read_csv(EVENTS_CSV)
        frame["date"] = pd.to_datetime(frame["date"]).dt.date
        return frame
    return pd.DataFrame()


@st.cache_data(show_spinner="Loading correlations ...")
def load_correlations() -> pd.DataFrame:
    """Load the event-study results."""
    if CORRELATIONS_CSV.exists():
        return pd.read_csv(CORRELATIONS_CSV)
    return pd.DataFrame()


@st.cache_data(show_spinner="Loading the effects report ...")
def load_report() -> str:
    """Load the markdown effects report."""
    if EFFECTS_MD.exists():
        return EFFECTS_MD.read_text(encoding="utf-8")
    return ""


@st.cache_data(show_spinner="Reading validation status ...")
def load_validation_status() -> dict[str, Any]:
    """Parse the alignment validation report for the sidebar status."""
    if not ALIGNMENT_REPORT.exists():
        return {"available": False, "passed": None, "text": ""}
    text = ALIGNMENT_REPORT.read_text(encoding="utf-8")
    passed = "✓ ALIGNMENT PASSED" in text

    def _grab(label: str) -> str:
        match = re.search(rf"^\s*{re.escape(label)}\s*:\s*(.+)$", text, re.MULTILINE)
        return match.group(1).strip() if match else "n/a"

    return {
        "available": True,
        "passed": passed,
        "text": text,
        "rows": _grab("Aligned master rows (date x index)"),
        "days": _grab("Unique trading days in aligned set"),
        "calendar": _grab("Unique trading days in calendar"),
        "gaps": _grab("Vendor gaps (no bar in any index)"),
        "range": _grab("Date range"),
        "generated": _grab("Generated at"),
    }


# --------------------------------------------------------------------------- #
# Sidebar
# --------------------------------------------------------------------------- #

def render_sidebar() -> None:
    """Render the sidebar with database stats and alignment status."""
    with st.sidebar:
        st.title("Celestial Indices")
        st.caption("Indian Stock Market & Planetary Correlation Engine")

        st.subheader("Alignment status")
        status = load_validation_status()
        if not status["available"]:
            st.warning("No validation report found. Run the pipeline first.")
        else:
            if status["passed"]:
                st.success("✓ ALIGNMENT PASSED")
            else:
                st.error("✗ ALIGNMENT FAILED")
            st.markdown(
                f"""
- Aligned rows: **{status['rows']}**
- Trading days: **{status['days']}** (calendar: {status['calendar']})
- Vendor gaps: **{status['gaps']}**
- Range: **{status['range']}**
- Generated: {status['generated']}
"""
            )

        st.subheader("Database")
        try:
            counts = table_counts(SETTINGS)
            st.dataframe(
                pd.DataFrame(
                    [{"table": name, "rows": count} for name, count in counts.items()]
                ),
                hide_index=True,
                width="stretch",
            )
        except Exception as exc:  # pragma: no cover - hosted snapshot has no runtime DB
            st.info(
                "Hosted snapshot mode: the dashboard is reading the committed CSV " 
                "datasets. The local SQLite runtime database is not bundled with " 
                "the public deployment."
            )

        st.subheader("Last refresh")
        try:
            run = latest_pipeline_run(SETTINGS)
            if run:
                st.markdown(
                    f"""
- Finished: **{run['finished_at']}**
- Aligned rows: **{run['aligned_rows']}**
- Range: **{run['first_date']} → {run['last_date']}**
"""
                )
            else:
                st.info("No pipeline run recorded yet.")
        except Exception as exc:  # pragma: no cover - hosted snapshot has no runtime DB
            st.info(
                "No hosted pipeline history is available. The validation report " 
                "above describes the committed build."
            )

        st.subheader("Market master")
        master_path = SETTINGS.master_db_path
        if master_path.exists():
            st.success(f"{master_path.name}")
            st.caption(f"{master_path.stat().st_size / 1e6:.1f} MB — the pipeline reads prices from here (no API).")
        else:
            st.info(
                "Hosted snapshot mode: the market-master SQLite file is kept local " 
                "and is not uploaded to the public app."
            )

        st.subheader("Automatic updates")
        update_status = read_status()
        st.caption(
            f"Status: {update_status.get('status', 'unknown')} · "
            f"Finished: {update_status.get('finished_ist', 'never')}"
        )
        if master_path.exists():
            if st.button("Refresh data now", use_container_width=True):
                with st.spinner("Fetching new market bars and rebuilding the ephemeris..."):
                    try:
                        payload = run_update(rebuild=True)
                        st.cache_data.clear()
                        if payload.get("alignment_passed") is False:
                            st.error("Refresh finished, but alignment validation failed. Check data/update_status.json.")
                        elif payload.get("status") == "partial":
                            st.warning("Refresh completed partially. Unconfigured or unavailable feeds are shown in the status file.")
                        else:
                            st.success("Refresh completed successfully.")
                        st.rerun()
                    except Exception as exc:  # pragma: no cover - UI resilience
                        st.error(f"Refresh failed: {exc}")
        else:
            st.info(
                "Automatic refresh is configured for the local Windows installation. "
                "This public deployment is read-only; refresh locally to rebuild data."
            )
        st.caption("The Windows task can run this same update automatically every day.")

        st.divider()
        st.caption(
            "Sidereal longitudes (Lahiri ayanamsa) evaluated at 15:30 IST, the "
            "close of the regular NSE session."
        )


# --------------------------------------------------------------------------- #
# Tab 1 — Index Explorer
# --------------------------------------------------------------------------- #

def render_index_explorer(aligned: pd.DataFrame, daily: pd.DataFrame) -> None:
    """Candlestick and volume explorer."""
    st.header("Index Explorer")
    if aligned.empty:
        st.info("No data available.")
        return

    col1, col2 = st.columns([1, 1])
    with col1:
        index_name = st.selectbox(
            "Index", INDEX_NAMES,
            format_func=lambda n: INDEX_LABELS.get(n, n),
        )
    series = aligned.loc[aligned["index_name"] == index_name].sort_values("date")
    with col2:
        bounds = st.date_input(
            "Date range",
            value=(series["date"].min(), series["date"].max()),
            min_value=series["date"].min(),
            max_value=series["date"].max(),
        )
    if isinstance(bounds, (tuple, list)) and len(bounds) == 2:
        start, end = bounds
    else:
        start = end = bounds if not isinstance(bounds, (tuple, list)) else bounds[0]

    series = series[(series["date"] >= start) & (series["date"] <= end)]
    if series.empty:
        st.warning("No rows in the selected range.")
        return

    metrics = st.columns(5)
    last = series.iloc[-1]
    metrics[0].metric("Last close", f"{last['close']:,.2f}")
    metrics[1].metric("Change (period)", f"{last['close'] - series.iloc[0]['close']:,.2f}")
    metrics[2].metric("High", f"{series['high'].max():,.2f}")
    metrics[3].metric("Low", f"{series['low'].min():,.2f}")
    metrics[4].metric("Sessions", f"{len(series):,}")

    figure = make_subplots(
        rows=2, cols=1, shared_xaxes=True,
        row_heights=[0.75, 0.25], vertical_spacing=0.04,
        subplot_titles=(f"{INDEX_LABELS.get(index_name, index_name)} price", "Volume"),
    )
    figure.add_trace(
        go.Candlestick(
            x=series["date"], open=series["open"], high=series["high"],
            low=series["low"], close=series["close"], name="OHLC",
            increasing_line_color="#26a69a", decreasing_line_color="#ef5350",
        ),
        row=1, col=1,
    )
    colors = ["#26a69a" if c >= o else "#ef5350"
              for o, c in zip(series["open"], series["close"])]
    figure.add_trace(
        go.Bar(x=series["date"], y=series["volume"], name="Volume",
               marker_color=colors, opacity=0.6),
        row=2, col=1,
    )
    figure.update_layout(
        height=620, margin=dict(t=40, b=20, l=10, r=10),
        xaxis_rangeslider_visible=False, hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    st.plotly_chart(figure, width="stretch")

    with st.expander("Raw data"):
        st.dataframe(
            series[["date", "day", "open", "high", "low", "close", "volume", "pct_change"]],
            width="stretch",
        )


# --------------------------------------------------------------------------- #
# Tab 2 — Planetary timeline
# --------------------------------------------------------------------------- #

def render_planetary_timeline(aligned: pd.DataFrame, events: pd.DataFrame) -> None:
    """Planetary sign chart and event heatmap."""
    st.header("Planetary Timeline")
    if aligned.empty:
        st.info("No data available.")
        return

    series = aligned.loc[aligned["index_name"] == "NIFTY_50"].sort_values("date")
    if series.empty:
        series = aligned.sort_values("date").drop_duplicates("date")
    else:
        series = series.drop_duplicates("date")

    col1, col2 = st.columns([1, 2])
    with col1:
        index_name = st.selectbox(
            "Index for the price overlay", INDEX_NAMES,
            format_func=lambda n: INDEX_LABELS.get(n, n),
            key="tl_index",
        )
        show_price = st.checkbox("Overlay price", value=True)
    overlay = aligned.loc[aligned["index_name"] == index_name].sort_values("date")

    with col2:
        bounds = st.date_input(
            "Date range",
            value=(series["date"].min(), series["date"].max()),
            min_value=series["date"].min(),
            max_value=series["date"].max(),
            key="tl_range",
        )
    if isinstance(bounds, (tuple, list)) and len(bounds) == 2:
        start, end = bounds
    else:
        start = end = bounds

    window = series[(series["date"] >= start) & (series["date"] <= end)]
    if window.empty:
        st.warning("No rows in the selected range.")
        return

    # --- sign chart ------------------------------------------------------
    figure = go.Figure()
    for planet in PLANETS:
        column = f"{planet.lower()}_sign"
        if column not in window.columns:
            continue
        values = window[column].to_numpy()
        # plot the sign index as a step line
        figure.add_trace(go.Scatter(
            x=window["date"], y=values, name=planet, mode="lines",
            line_shape="hv", line=dict(width=1.6),
            hovertemplate=f"{planet}<br>sign %{{y}}<extra></extra>",
        ))
    figure.update_layout(
        title="Sidereal sign of each body (0 = Aries … 11 = Pisces)",
        height=420, xaxis_title="Date",
        yaxis=dict(tickmode="array", tickvals=list(range(12)),
                   ticktext=list(SIGN_ABBR), range=[-0.5, 11.5]),
        hovermode="x unified", margin=dict(t=50, b=20, l=10, r=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02,
                       entrywidth=120, entrywidthmode="pixels"),
    )
    st.plotly_chart(figure, width="stretch")

    # --- price with event markers ---------------------------------------
    if show_price and not overlay.empty:
        price = overlay[(overlay["date"] >= start) & (overlay["date"] <= end)]
        price_figure = go.Figure()
        price_figure.add_trace(go.Scatter(
            x=price["date"], y=price["close"], name="Close",
            mode="lines", line=dict(color="#1f77b4", width=1.4),
        ))
        if not events.empty:
            marked = events[
                (events["date"] >= start) & (events["date"] <= end)
            ]
            markers = {
                "retrograde_station": ("triangle-down", "#d62728"),
                "direct_station": ("triangle-up", "#2ca02c"),
                "conjunction": ("circle", "#ff7f0e"),
                "aspect": ("square", "#9467bd"),
                "sign_ingress": ("diamond", "#8c564b"),
            }
            for category, (symbol, colour) in markers.items():
                subset = marked.loc[marked["category"] == category]
                if subset.empty:
                    continue
                price_figure.add_trace(go.Scatter(
                    x=subset["date"], y=subset["date"].map(
                        dict(zip(price["date"], price["close"]))
                    ).fillna(price["close"].mean()),
                    mode="markers", name=category.replace("_", " ").title(),
                    marker=dict(symbol=symbol, size=7, color=colour, opacity=0.75),
                    hovertext=subset["event_type"], hoverinfo="text",
                ))
        price_figure.update_layout(
            title=f"{INDEX_LABELS.get(index_name, index_name)} with planetary events",
            height=420, xaxis_title="Date", yaxis_title="Index level",
            hovermode="x unified", margin=dict(t=50, b=20, l=10, r=10),
            legend=dict(orientation="h", yanchor="bottom", y=1.02,
                       entrywidth=150, entrywidthmode="pixels"),
        )
        st.plotly_chart(price_figure, width="stretch")

    # --- event heatmap ---------------------------------------------------
    if not events.empty:
        st.subheader("Event heatmap")
        marked = events[(events["date"] >= start) & (events["date"] <= end)].copy()
        if marked.empty:
            st.info("No events in the selected range.")
            return
        marked["year"] = pd.to_datetime(marked["date"]).dt.year
        pivot = (
            marked.pivot_table(index="event_type", columns="year",
                               values="event_id", aggfunc="count")
            .fillna(0)
        )
        heatmap = go.Figure(go.Heatmap(
            z=pivot.values, x=[str(c) for c in pivot.columns],
            y=list(pivot.index), colorscale="YlOrRd", colorbar=dict(title="events"),
            hovertemplate="%{y} in %{x}: %{z} event(s)<extra></extra>",
        ))
        heatmap.update_layout(
            title="Events per type per year", height=620,
            margin=dict(t=50, b=20, l=10, r=10),
            xaxis_title="Year", yaxis=dict(automargin=True),
        )
        st.plotly_chart(heatmap, width="stretch")
        with st.expander("Event list"):
            st.dataframe(
                marked[["date", "event_type", "category", "planets", "description", "orb"]]
                .sort_values("date"),
                width="stretch",
            )


# --------------------------------------------------------------------------- #
# Tab 3 — Correlation heatmap
# --------------------------------------------------------------------------- #

def render_correlation_heatmap(correlations: pd.DataFrame) -> None:
    """Events x indices heatmap."""
    st.header("Correlation Heatmap")
    if correlations.empty:
        st.info("No correlation results available.")
        return

    col1, col2, col3 = st.columns(3)
    with col1:
        window = st.selectbox("Forward window (trading days)",
                               sorted(correlations["forward_window"].unique()),
                               index=1 if 3 in sorted(correlations["forward_window"].unique()) else 0)
    with col2:
        metric = st.selectbox(
            "Metric",
            ["excess_return", "mean_return", "win_rate", "p_value", "q_value_bh", "base_rate"],
            format_func=lambda m: {
                "excess_return": "Excess return (pp)", "mean_return": "Mean return (%)",
                "win_rate": "Win rate (%)", "p_value": "p-value (raw)",
                "q_value_bh": "q-value (Benjamini-Hochberg)", "base_rate": "Base rate (%)",
            }[m],
        )
    with col3:
        category_filter = st.multiselect(
            "Event category",
            sorted(correlations["category"].unique()),
            default=sorted(correlations["category"].unique()),
        )

    subset = correlations.loc[
        (correlations["forward_window"] == window)
        & (correlations["category"].isin(category_filter))
    ].copy()
    if subset.empty:
        st.warning("Nothing to show for this selection.")
        return

    pivot = subset.pivot_table(
        index="event_type", columns="index_name", values=metric, aggfunc="mean"
    )
    pivot = pivot.reindex(columns=[c for c in INDEX_NAMES if c in pivot.columns])

    if metric in ("p_value", "q_value_bh"):
        values = -np.log10(pivot.to_numpy(dtype=float))
        colours = "Viridis_r"
        label = "p" if metric == "p_value" else "q"
        hovertemplate = f"%{{y}} / %{{x}}<br>-log10({label}) = %{{z:.2f}}<extra></extra>"
    else:
        values = pivot.to_numpy(dtype=float)
        colours = "RdBu_r"
        hovertemplate = "%{y} / %{x}<br>%{z:.3f}<extra></extra>"

    figure = go.Figure(go.Heatmap(
        z=values,
        x=[INDEX_LABELS.get(c, c) for c in pivot.columns],
        y=list(pivot.index),
        colorscale=colours, colorbar=dict(title=metric.replace("_", " ")),
        hovertemplate=hovertemplate,
    ))
    figure.update_layout(
        title=f"{metric.replace('_', ' ').title()} by event type — {window}-day window",
        height=max(500, 22 * len(pivot)), margin=dict(t=60, b=20, l=10, r=10),
        xaxis_title="Index", yaxis=dict(automargin=True),
    )
    st.plotly_chart(figure, width="stretch")

    st.subheader("Table")
    table = pivot.reset_index().rename(columns=INDEX_LABELS)
    st.dataframe(table, width="stretch", height=420)

    n_nominal = int((subset["p_value"] < 0.05).sum())
    n_bh = int(subset["is_significant_bh"].sum()) if "is_significant_bh" in subset else 0
    m1, m2, m3 = st.columns(3)
    m1.metric("Cells in view", f"{len(subset):,}")
    m2.metric("Significant at p<0.05", f"{n_nominal:,}")
    m3.metric("Survives BH correction", f"{n_bh:,}")

    best = subset.loc[subset["p_value"].idxmin()] if subset["p_value"].notna().any() else None
    if best is not None:
        q_text = (
            f", q={best['q_value_bh']:.4f}"
            if "q_value_bh" in best and pd.notna(best["q_value_bh"]) else ""
        )
        bh_text = (
            " — survives Benjamini-Hochberg correction"
            if bool(best.get("is_significant_bh")) else " — does not survive BH correction"
        )
        st.info(
            f"Strongest nominal signal in this view: **{best['event_type']}** on "
            f"**{INDEX_LABELS.get(best['index_name'], best['index_name'])}** — mean "
            f"{best['mean_return']:+.3f}% vs base {best['base_rate']:+.3f}% "
            f"(N={int(best['sample_size'])}, p={best['p_value']:.4f}{q_text}){bh_text}."
        )


# --------------------------------------------------------------------------- #
# Tab 4 — Event study
# --------------------------------------------------------------------------- #

def render_event_study(correlations: pd.DataFrame, aligned: pd.DataFrame,
                        events: pd.DataFrame) -> None:
    """Forward-return bars for a selected event."""
    st.header("Event Study")
    if correlations.empty:
        st.info("No correlation results available.")
        return

    col1, col2 = st.columns([2, 1])
    with col1:
        event_types = sorted(correlations["event_type"].unique())
        event_type = st.selectbox("Event type", event_types)
    with col2:
        indices = sorted(
            correlations.loc[correlations["event_type"] == event_type, "index_name"].unique()
        )
        index_name = st.selectbox(
            "Index", indices, format_func=lambda n: INDEX_LABELS.get(n, n)
        )

    subset = correlations.loc[
        (correlations["event_type"] == event_type)
        & (correlations["index_name"] == index_name)
    ].sort_values("forward_window")

    if subset.empty:
        st.info("Nothing to show.")
        return

    label = INDEX_LABELS.get(index_name, index_name)
    figure = go.Figure()
    figure.add_trace(go.Bar(
        x=subset["forward_window"].astype(str) + "d",
        y=subset["mean_return"],
        marker_color=[
            "#26a69a" if value >= 0 else "#ef5350" for value in subset["mean_return"]
        ],
        name="Mean forward return",
        text=[f"{v:+.2f}%" for v in subset["mean_return"]],
        textposition="outside",
    ))
    figure.add_trace(go.Scatter(
        x=subset["forward_window"].astype(str) + "d",
        y=subset["base_rate"], mode="lines+markers", name="Base rate",
        line=dict(color="#555", dash="dash"),
    ))
    figure.update_layout(
        title=f"{event_type} — {label}",
        yaxis_title="Forward return (%)", height=460,
        margin=dict(t=50, b=20, l=10, r=10), hovermode="x unified",
    )
    st.plotly_chart(figure, width="stretch")

    display = subset[[
        "forward_window", "sample_size", "mean_return", "median_return",
        "base_rate", "excess_return", "win_rate", "std_return",
        "t_stat", "p_value", "one_sample_p",
    ] + (["q_value_bh"] if "q_value_bh" in subset.columns else [])].rename(columns={
        "forward_window": "Window (d)", "sample_size": "N",
        "mean_return": "Mean %", "median_return": "Median %",
        "base_rate": "Base %", "excess_return": "Excess pp",
        "win_rate": "Win %", "std_return": "Std %",
        "t_stat": "t", "p_value": "p (Welch)", "one_sample_p": "p (vs base)",
        "q_value_bh": "q (BH)",
    })
    if "is_significant_bh" in subset.columns:
        display["BH significant"] = subset["is_significant_bh"].map({True: "yes", False: "no"}).values
    st.dataframe(display, width="stretch")

    # Event-by-event detail
    if not events.empty and not aligned.empty:
        st.subheader("Event-by-event")
        event_rows = events.loc[events["event_type"] == event_type].sort_values("date")
        if event_rows.empty:
            st.info("No events of this type.")
            return
        series = aligned.loc[aligned["index_name"] == index_name].sort_values("date")
        dates = list(series["date"])
        closes = series["close"].to_numpy(dtype=float)

        records = []
        for _, event in event_rows.iterrows():
            key = next((i for i, d in enumerate(dates) if d >= event["date"]), None)
            if key is None:
                continue
            record = {
                "event_date": event["date"],
                "session": dates[key],
                "close": closes[key],
                "description": event["description"],
            }
            for window in (1, 3, 5, 10, 20):
                target = key + window
                record[f"{window}d"] = (
                    float((closes[target] / closes[key] - 1.0) * 100.0)
                    if target < len(closes) else None
                )
            records.append(record)
        if records:
            st.dataframe(pd.DataFrame(records), width="stretch")


# --------------------------------------------------------------------------- #
# Tab 5 — Effects report
# --------------------------------------------------------------------------- #

def render_effects_report() -> None:
    """Render the markdown effects report section by section."""
    st.header("Effects Report")
    report = load_report()
    if not report:
        st.warning("No effects report found. Run `python -m src.data_pipeline --all`.")
        return

    parts = re.split(r"(?m)^(## .+)$", report)
    sections: list[tuple[str, str]] = []
    preamble = parts[0]
    for index in range(1, len(parts) - 1, 2):
        sections.append((parts[index].strip(), parts[index + 1]))

    if preamble.strip():
        with st.expander("Introduction", expanded=False):
            st.markdown(preamble)

    labels = [name for name, _ in sections]
    selected = st.multiselect(
        "Report sections", labels, default=labels,
        help="Render only the sections you need - the full report is long.",
    )
    for name, body in sections:
        if name in selected:
            st.markdown(body)


# --------------------------------------------------------------------------- #
# Tab 6 — Data export
# --------------------------------------------------------------------------- #

def render_data_export(aligned: pd.DataFrame, events: pd.DataFrame,
                       correlations: pd.DataFrame) -> None:
    """Download the datasets."""
    st.header("Data Export")
    st.write(
        "Every table below is the exact object the pipeline wrote. "
        "Downloads are UTF-8 CSV."
    )

    downloads = [
        ("aligned_master (one row per date x index)", aligned, "aligned_master.csv"),
        ("planetary events", events, "planetary_events.csv"),
        ("correlation results", correlations, "correlation_results.csv"),
    ]
    for label, frame, filename in downloads:
        st.subheader(label)
        if frame is None or frame.empty:
            st.info("No data available.")
            continue
        copy = frame.copy()
        for column in copy.columns:
            if copy[column].dtype == object:
                copy[column] = copy[column].astype(str)
        st.caption(f"{len(copy):,} rows x {len(copy.columns)} columns")
        st.download_button(
            f"Download {filename}",
            data=copy.to_csv(index=False).encode("utf-8"),
            file_name=filename,
            mime="text/csv",
            key=f"dl_{filename}",
        )
        with st.expander("Preview"):
            st.dataframe(copy.head(200), width="stretch")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> None:
    """Entry point for the Streamlit app."""
    render_sidebar()

    aligned = load_aligned()
    daily = load_daily()
    events = load_events()
    correlations = load_correlations()

    if aligned.empty and daily.empty:
        st.error(
            "No dataset found. Run the pipeline first:\n\n"
            "```bash\npython -m src.data_pipeline --all\n```"
        )
        return

    tabs = st.tabs([
        "Index Explorer", "Planetary Timeline", "Correlation Heatmap",
        "Event Study", "Effects Report", "Data Export",
    ])

    with tabs[0]:
        render_index_explorer(aligned, daily)
    with tabs[1]:
        render_planetary_timeline(aligned, events)
    with tabs[2]:
        render_correlation_heatmap(correlations)
    with tabs[3]:
        render_event_study(correlations, aligned, events)
    with tabs[4]:
        render_effects_report()
    with tabs[5]:
        render_data_export(aligned, events, correlations)


if __name__ == "__main__":
    main()
