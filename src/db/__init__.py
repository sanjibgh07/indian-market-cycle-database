"""Database layer for Celestial Indices.

Exposes the SQLAlchemy ORM models and the session helpers.
"""

from __future__ import annotations

from .models import (
    Base,
    CorrelationResult,
    EventStudyCache,
    IndexOHLCV,
    PipelineRun,
    PlanetaryEvent,
    PlanetaryPosition,
    TradingCalendar,
)
from .session import (
    drop_db,
    get_engine,
    get_session_factory,
    init_db,
    latest_pipeline_run,
    session_scope,
    table_counts,
)

__all__ = [
    "Base",
    "CorrelationResult",
    "EventStudyCache",
    "IndexOHLCV",
    "PipelineRun",
    "PlanetaryEvent",
    "PlanetaryPosition",
    "TradingCalendar",
    "drop_db",
    "get_engine",
    "get_session_factory",
    "init_db",
    "latest_pipeline_run",
    "session_scope",
    "table_counts",
]
