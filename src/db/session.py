"""Database engine and session management.

SQLite is used for development; the same code works against PostgreSQL by
changing ``DATABASE_URL``.  A relative SQLite URL is resolved against the
project root so the database always lands next to the data directory, and the
parent folder is created if needed.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from sqlalchemy import create_engine, event, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from ..utils import PROJECT_ROOT, Settings, get_logger
from .models import Base

logger = get_logger(__name__)

_ENGINE: Engine | None = None
_SESSION_FACTORY: sessionmaker[Session] | None = None


def _resolve_url(url: str) -> str:
    """Turn a relative SQLite path into an absolute one rooted at the project."""
    if not url.startswith("sqlite:///"):
        return url
    raw = url[len("sqlite:///"):]
    if raw == ":memory:":
        return url
    path = Path(raw)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    return f"sqlite:///{path}"


def get_engine(settings: Settings | None = None, url: str | None = None) -> Engine:
    """Return the process-wide SQLAlchemy engine, creating it on first use."""
    global _ENGINE, _SESSION_FACTORY
    if _ENGINE is not None and url is None:
        return _ENGINE

    resolved = url or (settings or Settings.from_env()).database_url
    resolved = _resolve_url(resolved)

    if resolved.startswith("sqlite"):
        engine = create_engine(
            resolved,
            future=True,
            connect_args={"check_same_thread": False},
        )

        @event.listens_for(engine, "connect")
        def _sqlite_pragmas(dbapi_connection, _record):  # pragma: no cover - driver hook
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.close()

    else:
        engine = create_engine(resolved, future=True, pool_pre_ping=True)

    if url is None:
        _ENGINE = engine
        _SESSION_FACTORY = sessionmaker(bind=engine, expire_on_commit=False, future=True)
    return engine


def get_session_factory(settings: Settings | None = None) -> sessionmaker[Session]:
    """Return the process-wide session factory."""
    if _SESSION_FACTORY is None:
        get_engine(settings)
    assert _SESSION_FACTORY is not None
    return _SESSION_FACTORY


@contextmanager
def session_scope(settings: Settings | None = None) -> Iterator[Session]:
    """Context manager providing a transactional session."""
    factory = get_session_factory(settings)
    session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db(settings: Settings | None = None) -> Engine:
    """Create all tables if they do not exist yet and return the engine."""
    engine = get_engine(settings)
    Base.metadata.create_all(engine)
    logger.info("Database schema ready at %s", engine.url)
    return engine


def drop_db(settings: Settings | None = None) -> None:
    """Drop every table (used by the pipeline's ``--reset`` flag)."""
    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    logger.warning("Database schema dropped")


def table_counts(settings: Settings | None = None) -> dict[str, int]:
    """Return the row count of each table, for the UI sidebar and the API."""
    engine = get_engine(settings)
    counts: dict[str, int] = {}
    with engine.connect() as conn:
        for table in Base.metadata.sorted_tables:
            count = conn.exec_driver_sql(f"SELECT COUNT(*) FROM {table.name}").scalar()
            counts[table.name] = int(count or 0)
    return counts


def latest_pipeline_run(settings: Settings | None = None) -> dict[str, object] | None:
    """Return the most recent pipeline run as a plain dictionary."""
    from .models import PipelineRun

    with session_scope(settings) as session:
        row = session.scalars(
            select(PipelineRun).order_by(PipelineRun.id.desc()).limit(1)
        ).first()
        if row is None:
            return None
        return {
            "id": row.id,
            "started_at": row.started_at,
            "finished_at": row.finished_at,
            "alignment_passed": row.alignment_passed,
            "aligned_rows": row.aligned_rows,
            "first_date": row.first_date,
            "last_date": row.last_date,
            "notes": row.notes,
        }


__all__ = [
    "drop_db",
    "get_engine",
    "get_session_factory",
    "init_db",
    "latest_pipeline_run",
    "session_scope",
    "table_counts",
]
