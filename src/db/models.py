"""SQLAlchemy ORM models for the Celestial Indices dataset.

The schema is written so that it runs unchanged on SQLite (development) and
PostgreSQL (production): only portable column types are used, every table has
an explicit primary key, and the two composite-key tables declare their keys
as real ``PrimaryKeyConstraint`` objects rather than relying on
``autoincrement``.
"""

from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Float,
    Index as SAIndex,
    Integer,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Declarative base shared by every model."""


class TradingCalendar(Base):
    """One row per weekday in the covered range.

    ``is_trading_day`` is ``False`` for official NSE holidays; ``holiday_reason``
    then carries the published reason for the closure.
    """

    __tablename__ = "trading_calendar"

    date: Mapped[date] = mapped_column(Date, primary_key=True, nullable=False)
    is_trading_day: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    holiday_reason: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return (
            f"<TradingCalendar {self.date} trading={self.is_trading_day} "
            f"reason={self.holiday_reason!r}>"
        )


class IndexOHLCV(Base):
    """Daily OHLCV for one index on one trading day."""

    __tablename__ = "indices"

    date: Mapped[date] = mapped_column(Date, primary_key=True, nullable=False)
    index_name: Mapped[str] = mapped_column(String(64), primary_key=True, nullable=False)
    open: Mapped[float] = mapped_column(Float, nullable=False)
    high: Mapped[float] = mapped_column(Float, nullable=False)
    low: Mapped[float] = mapped_column(Float, nullable=False)
    close: Mapped[float] = mapped_column(Float, nullable=False)
    volume: Mapped[float | None] = mapped_column(Float, nullable=True)
    pct_change: Mapped[float | None] = mapped_column(Float, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<IndexOHLCV {self.index_name} {self.date} close={self.close}>"


class PlanetaryPosition(Base):
    """Sidereal (Lahiri) position of one planet on one calendar day at 15:30 IST."""

    __tablename__ = "planetary_positions"

    date: Mapped[date] = mapped_column(Date, primary_key=True, nullable=False)
    planet: Mapped[str] = mapped_column(String(16), primary_key=True, nullable=False)
    sign: Mapped[int] = mapped_column(Integer, nullable=False)
    degree: Mapped[float] = mapped_column(Float, nullable=False)
    is_retrograde: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return (
            f"<PlanetaryPosition {self.date} {self.planet} sign={self.sign} "
            f"deg={self.degree:.2f} retro={self.is_retrograde}>"
        )


class PlanetaryEvent(Base):
    """A detected astrological event (ingress, station, conjunction, aspect)."""

    __tablename__ = "planetary_events"

    event_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    event_type: Mapped[str] = mapped_column(String(48), nullable=False)
    planets: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    orb: Mapped[float | None] = mapped_column(Float, nullable=True)

    __table_args__ = (
        SAIndex("ix_planetary_events_date", "date"),
        SAIndex("ix_planetary_events_type", "event_type"),
        UniqueConstraint("date", "event_type", "planets", name="uq_event_identity"),
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<PlanetaryEvent {self.date} {self.event_type} {self.planets}>"


class CorrelationResult(Base):
    """Outcome of one forward-return event study (event type x index x window)."""

    __tablename__ = "correlation_results"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_type: Mapped[str] = mapped_column(String(48), nullable=False)
    index_name: Mapped[str] = mapped_column(String(64), nullable=False)
    forward_window: Mapped[int] = mapped_column(Integer, nullable=False)
    mean_return: Mapped[float | None] = mapped_column(Float, nullable=True)
    median_return: Mapped[float | None] = mapped_column(Float, nullable=True)
    win_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    sample_size: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    t_stat: Mapped[float | None] = mapped_column(Float, nullable=True)
    p_value: Mapped[float | None] = mapped_column(Float, nullable=True)
    base_rate: Mapped[float | None] = mapped_column(Float, nullable=True)

    __table_args__ = (
        UniqueConstraint(
            "event_type", "index_name", "forward_window", name="uq_correlation_identity"
        ),
        SAIndex("ix_correlation_event", "event_type"),
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return (
            f"<CorrelationResult {self.event_type} {self.index_name} "
            f"w={self.forward_window} n={self.sample_size}>"
        )


class EventStudyCache(Base):
    """Serialised full result payload for a (event_type, index) study."""

    __tablename__ = "event_study_cache"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_type: Mapped[str] = mapped_column(String(48), nullable=False)
    index_name: Mapped[str] = mapped_column(String(64), nullable=False)
    computed_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    result_json: Mapped[str] = mapped_column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint("event_type", "index_name", name="uq_cache_identity"),
    )

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<EventStudyCache {self.event_type} {self.index_name}>"


class PipelineRun(Base):
    """Bookkeeping row describing the most recent pipeline execution."""

    __tablename__ = "pipeline_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    started_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    finished_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    alignment_passed: Mapped[bool | None] = mapped_column(Boolean, nullable=True)
    aligned_rows: Mapped[int | None] = mapped_column(Integer, nullable=True)
    first_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    last_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover - debug helper
        return f"<PipelineRun {self.id} passed={self.alignment_passed}>"


__all__ = [
    "Base",
    "CorrelationResult",
    "EventStudyCache",
    "IndexOHLCV",
    "PipelineRun",
    "PlanetaryEvent",
    "PlanetaryPosition",
    "TradingCalendar",
]
