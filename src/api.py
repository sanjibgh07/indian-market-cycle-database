"""Optional FastAPI data layer over the Celestial Indices dataset.

Run with::

    uvicorn src.api:app --reload

The API is read-only and serves the same artefacts the Streamlit UI uses:
the aligned master, the detected events and the event-study results.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

from .db.session import latest_pipeline_run, table_counts
from .utils import (
    CORRELATIONS_CSV,
    EFFECTS_JSON,
    EVENTS_CSV,
    PROCESSED_DIR,
    Settings,
    get_logger,
    read_json,
)

logger = get_logger(__name__)

app = FastAPI(
    title="Celestial Indices API",
    description=(
        "Date-aligned Indian index OHLCV joined with Lahiri ayanamsa planetary "
        "positions, plus the forward-return event studies derived from them."
    ),
    version="1.0.0",
)

SETTINGS = Settings.from_env()


def _read_parquet_or_csv(stem: str) -> list[dict[str, Any]]:
    """Load a processed dataset as a list of dictionaries."""
    import pandas as pd

    parquet = PROCESSED_DIR / f"{stem}.parquet"
    csv = PROCESSED_DIR / f"{stem}.csv"
    if parquet.exists():
        frame = pd.read_parquet(parquet)
    elif csv.exists():
        frame = pd.read_csv(csv)
    else:
        return []
    for column in frame.columns:
        if frame[column].dtype == object:
            frame[column] = frame[column].astype(str)
    return frame.to_dict(orient="records")


@app.get("/health", tags=["meta"])
def health() -> dict[str, Any]:
    """Return a simple health payload."""
    return {"status": "ok", "version": app.version}


@app.get("/update-status", tags=["meta"])
def update_status() -> dict[str, Any]:
    """Return the last automatic market/ephemeris refresh attempt."""
    from .live_update import read_status

    return read_status()


@app.get("/stats", tags=["meta"])
def stats() -> dict[str, Any]:
    """Return row counts per table and the last pipeline run."""
    try:
        counts = table_counts(SETTINGS)
    except Exception as exc:  # pragma: no cover - database may be absent
        counts = {}
        logger.warning("table counts unavailable: %s", exc)
    return {"tables": counts, "last_run": latest_pipeline_run(SETTINGS)}


@app.get("/alignment", tags=["meta"])
def alignment() -> dict[str, Any]:
    """Return the alignment validation report and its verdict."""
    from .utils import ALIGNMENT_REPORT

    if not ALIGNMENT_REPORT.exists():
        raise HTTPException(status_code=404, detail="No alignment report found")
    text = ALIGNMENT_REPORT.read_text(encoding="utf-8")
    return {
        "passed": "✓ ALIGNMENT PASSED" in text,
        "report": text,
    }


@app.get("/aligned", tags=["data"])
def aligned(
    index_name: str | None = Query(default=None, description="Filter by index name"),
    start: date | None = Query(default=None, description="Inclusive start date"),
    end: date | None = Query(default=None, description="Inclusive end date"),
    limit: int = Query(default=500, ge=1, le=50_000),
) -> list[dict[str, Any]]:
    """Return rows of the aligned master (one row per date x index)."""
    rows = _read_parquet_or_csv("aligned_master")
    if index_name:
        rows = [r for r in rows if r.get("index_name") == index_name]
    if start:
        rows = [r for r in rows if str(r.get("date"))[:10] >= start.isoformat()]
    if end:
        rows = [r for r in rows if str(r.get("date"))[:10] <= end.isoformat()]
    return rows[:limit]


@app.get("/events", tags=["data"])
def events(
    event_type: str | None = Query(default=None),
    category: str | None = Query(default=None),
    limit: int = Query(default=500, ge=1, le=50_000),
) -> list[dict[str, Any]]:
    """Return the detected planetary events."""
    import pandas as pd

    if not EVENTS_CSV.exists():
        return []
    frame = pd.read_csv(EVENTS_CSV)
    if event_type:
        frame = frame.loc[frame["event_type"] == event_type]
    if category:
        frame = frame.loc[frame["category"] == category]
    frame = frame.head(limit)
    for column in frame.columns:
        if frame[column].dtype == object:
            frame[column] = frame[column].astype(str)
    return frame.to_dict(orient="records")


@app.get("/correlations", tags=["data"])
def correlations(
    event_type: str | None = Query(default=None),
    index_name: str | None = Query(default=None),
    limit: int = Query(default=1000, ge=1, le=50_000),
) -> list[dict[str, Any]]:
    """Return the forward-return event-study results."""
    import pandas as pd

    if not CORRELATIONS_CSV.exists():
        return []
    frame = pd.read_csv(CORRELATIONS_CSV)
    if event_type:
        frame = frame.loc[frame["event_type"] == event_type]
    if index_name:
        frame = frame.loc[frame["index_name"] == index_name]
    frame = frame.head(limit)
    for column in frame.columns:
        if frame[column].dtype == object:
            frame[column] = frame[column].astype(str)
    return frame.to_dict(orient="records")


@app.get("/effects", tags=["data"])
def effects() -> dict[str, Any]:
    """Return the machine-readable effects summary."""
    if not EFFECTS_JSON.exists():
        raise HTTPException(status_code=404, detail="No effects summary found")
    return read_json(EFFECTS_JSON)


@app.get("/", tags=["meta"])
def root() -> JSONResponse:
    """Return a short index of the available endpoints."""
    return JSONResponse({
        "name": app.title,
        "version": app.version,
        "endpoints": [
            "/health", "/stats", "/alignment", "/aligned", "/events",
            "/correlations", "/effects", "/update-status", "/docs",
        ],
    })


__all__ = ["app"]
