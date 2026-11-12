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
# D
