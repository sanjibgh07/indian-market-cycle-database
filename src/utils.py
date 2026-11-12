"""Shared helpers: configuration, logging, paths and small pandas utilities.

Everything in this module is dependency-light on purpose — it is imported by
every other module in the project, including the Streamlit UI.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence

try:  # pragma: no cover - dotenv is optional at runtime
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover
    def load_dotenv(*_args: Any, **_kwargs: Any) -> bool:
        """Fallback no-op when python-dotenv is unavailable."""
        return False

# --------------------------------------------------------------------------- #
# Project paths
# --------------------------------------------------------------------------- #

PACKAGE_ROOT: Path = Path(__file__).resolve().parent
PROJECT_ROOT: Path = PACKAGE_ROOT.parent

DATA_DIR: Path = PROJECT_ROOT / "data"
RAW_DIR: Path = DATA_DIR / "raw"
PROCESSED_DIR: Path = DATA_DIR / "processed"
REFERENCE_DIR: Path = DATA_DIR / "reference"
REPORTS_DIR: Path = PROJECT_ROOT / "reports"
NOTEBOOKS_DIR: Path = PROJECT_ROOT / "notebooks"

HOLIDAYS_FILE: Path = REFERENCE_DIR / "nse_holidays.json"
MASTER_DB_NAME: str = "INDIAN_MARKET_MASTER_PRE_EPHEMERIS.sqlite"
MASTER_DB_PATH: Path = DATA_DIR / MASTER_DB_NAME
ALIGNED_PARQUET: Path = PROCESSED_DIR / "aligned_master.parquet"
ALIGNED_CSV: Path = PROCESSED_DIR / "aligned_master.csv"
PLANETARY_PARQUET: Path = PROCESSED_DIR / "planetary_master.parquet"
EVENTS_CSV: Path = PROCESSED_DIR / "planetary_events.csv"
CORRELATIONS_CSV: Path = PROCESSED_DIR / "correlation_results.csv"
ALIGNMENT_REPORT: Path = REPORTS_DIR / "alignment_validation.txt"
EFFECTS_MD: Path = REPORTS_DIR / "effects_summary.md"
EFFECTS_JSON: Path = REPORTS_DIR / "effects_summary.json"


def ensure_dirs() -> None:
    """Create every directory the project writes into."""
    for path in (DATA_DIR, RAW_DIR, PROCESSED_DIR, REFERENCE_DIR, REPORTS_DIR, NOTEBOOKS_DIR):
        path.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #

_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)-24s | %(message)s"


def setup_logging(level: int | str = logging.INFO, log_file: Path | None = None) -> None:
    """Configure root logging once, writing to stdout and optionally a file.

    Args:
        level: Logging level name or numeric value.
        log_file: Optional file that receives a copy of the records.
    """
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    root = logging.getLogger()
    if root.handlers:
        root.setLevel(level)
        return

    formatter = logging.Formatter(_LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(formatter)
    root.addHandler(stream)
    root.setLevel(level)

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        root.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """Return a module logger."""
    return logging.getLogger(name)


# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class Settings:
    """Runtime configuration resolved from the environment (with defaults)."""

    database_url: str = "sqlite:///data/celestial_indices.db"
    data_start_date: date = date(2000, 1, 1)
    market_data_source: str = "auto"
    raw_data_dir: Path = RAW_DIR
    market_close_time: time = time(15, 30)
    market_timezone: str = "Asia/Kolkata"
    ayanamsa: str = "lahiri"
    reports_dir: Path = REPORTS_DIR
    processed_data_dir: Path = PROCESSED_DIR
    holidays_file: Path = HOLIDAYS_FILE

    @property
    def master_db_path(self) -> Path:
        """Path of the SQLite market master the pipeline reads prices from."""
        return DATA_DIR / MASTER_DB_NAME

    @property
    def database_path(self) -> Path:
        """Absolute path of the SQLite file when the dev database is in use."""
        if self.database_url.startswith("sqlite:///"):
            raw = self.database_url.replace("sqlite:///", "", 1)
            candidate = Path(raw)
            if not candidate.is_absolute():
                candidate = PROJECT_ROOT / candidate
            return candidate
        return Path(self.database_url)

    @classmethod
    def from_env(cls, env_file: Path | None = None) -> "Settings":
        """Build settings from a ``.env`` file plus the process environment."""
        load_dotenv(env_file if env_file and env_file.exists() else PROJECT_ROOT / ".env")

        start_raw = os.getenv("DATA_START_DATE", "2000-01-01").strip()
        try:
            start = date.fromisoformat(start_raw)
        except ValueError:
            start = date(2000, 1, 1)

        close_raw = os.getenv("MARKET_CLOSE_LOCAL_TIME", "15:30").strip()
        try:
            hh, _, mm = close_raw.partition(":")
            close_time = time(int(hh), int(mm))
        except ValueError:
            close_time = time(15, 30)

        raw_dir = Path(os.getenv("RAW_DATA_DIR", str(RAW_DIR)))
        if not raw_dir.is_absolute():
            raw_dir = PROJECT_ROOT / raw_dir

        reports_dir = Path(os.getenv("REPORTS_DIR", str(REPORTS_DIR)))
        if not reports_dir.is_absolute():
            reports_dir = PROJECT_ROOT / reports_dir

        processed_dir = Path(os.getenv("PROCESSED_DATA_DIR", str(PROCESSED_DIR)))
        if not processed_dir.is_absolute():
            processed_dir = PROJECT_ROOT / processed_dir

        return cls(
            database_url=os.getenv("DATABASE_URL", cls.database_url),
            data_start_date=start,
            market_data_source=os.getenv("MARKET_DATA_SOURCE", "auto").strip().lower(),
            raw_data_dir=raw_dir,
            market_close_time=close_time,
            market_timezone=os.getenv("MARKET_TIMEZONE", "Asia/Kolkata"),
            ayanamsa=os.getenv("AYANAMSA", "lahiri").strip().lower(),
            reports_dir=reports_dir,
            processed_data_dir=processed_dir,
        )


# --------------------------------------------------------------------------- #
# Domain constants
# --------------------------------------------------------------------------- #

PLANETS: tuple[str, ...] = (
    "Sun", "Moon", "Mercury", "Venus", "Mars",
    "Jupiter", "Saturn", "Rahu", "Ketu",
)

SIGNS: tuple[str, ...] = (
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
)

SIGN_ABBR: tuple[str, ...] = (
    "Ari", "Tau", "Gem", "Cnc", "Leo", "Vir",
    "Lib", "Sco", "Sag", "Cap", "Aqu", "Psc",
)

INDEX_NAMES: tuple[str, ...] = (
    "SENSEX", "NIFTY_50", "NIFTY_BANK", "NIFTY_MIDCAP_100", "NIFTY_MIDCAP_150",
)

INDEX_LABELS: dict[str, str] = {
    "SENSEX": "BSE Sensex",
    "NIFTY_50": "Nifty 50",
    "NIFTY_BANK": "Nifty Bank",
    "NIFTY_MIDCAP_100": "Nifty Midcap 100",
    "NIFTY_MIDCAP_150": "Nifty Midcap 150",
}

FORWARD_WINDOWS: tuple[int, ...] = (1, 3, 5, 10, 20)

IST_OFFSET = timedelta(hours=5, minutes=30)


def utc_now() -> datetime:
    """Timezone-aware current UTC timestamp."""
    return datetime.now(timezone.utc)


def to_utc(local_naive: datetime, offset: timedelta = IST_OFFSET) -> datetime:
    """Convert a naive IST wall-clock timestamp into an aware UTC timestamp."""
    return local_naive.replace(tzinfo=timezone(offset)).astimezone(timezone.utc)


# --------------------------------------------------------------------------- #
# Small utilities
# --------------------------------------------------------------------------- #

def read_json(path: Path) -> Any:
    """Load a UTF-8 JSON document."""
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: Path, payload: Any, indent: int = 2) -> None:
    """Write a UTF-8 JSON document, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=indent, ensure_ascii=False, default=str)
        fh.write("\n")


def write_text(path: Path, text: str) -> None:
    """Write a UTF-8 text file, creating parent directories."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def chunked(items: Sequence[Any], size: int) -> Iterable[Sequence[Any]]:
    """Yield successive ``size``-length chunks of ``items``."""
    if size <= 0:
        raise ValueError("size must be positive")
    for start in range(0, len(items), size):
        yield items[start:start + size]


def summarise_frame(frame: Any, name: str = "frame") -> str:
    """Return a one-line human summary of a pandas DataFrame."""
    if frame is None or len(frame) == 0:
        return f"{name}: empty"
    return f"{name}: {len(frame)} rows x {len(frame.columns)} cols"


def coerce_date(value: Any) -> date:
    """Best-effort conversion of many types into a :class:`datetime.date`."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if hasattr(value, "to_pydatime"):
        return value.to_pydatime().date()
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1]
    try:
        return date.fromisoformat(text[:10])
    except ValueError as exc:  # pragma: no cover - defensive
        raise ValueError(f"Cannot interpret {value!r} as a date") from exc


def iso_date(value: Any) -> str:
    """Return an ISO-8601 ``YYYY-MM-DD`` string for any date-like value."""
    return coerce_date(value).isoformat()


def format_pct(value: float | None, digits: int = 2) -> str:
    """Format a percentage value for human-readable reports."""
    if value is None:
        return "n/a"
    return f"{value:.{digits}f}%"


def format_p_value(value: float | None) -> str:
    """Format a p-value using standard academic thresholds."""
    if value is None:
        return "n/a"
    if value < 0.001:
        return "p<0.001"
    if value < 0.01:
        return "p=0.00{:.0f}".format(value * 100)
    if value < 0.05:
        return "p=0.0{:.0f}".format(value * 10)
    return f"p={value:.3f}"


def significance_label(p_value: float | None, alpha: float = 0.05) -> str:
    """Return a short statistical-significance phrase."""
    if p_value is None:
        return "not tested"
    if p_value < alpha:
        return f"statistically significant at p={p_value:.4f}"
    return f"not statistically significant (p={p_value:.4f})"


__all__ = [
    "ALIGNED_CSV",
    "ALIGNED_PARQUET",
    "ALIGNMENT_REPORT",
    "DATA_DIR",
    "EFFECTS_JSON",
    "EFFECTS_MD",
    "EVENTS_CSV",
    "FORWARD_WINDOWS",
    "HOLIDAYS_FILE",
    "INDEX_LABELS",
    "INDEX_NAMES",
    "MASTER_DB_NAME",
    "MASTER_DB_PATH",
    "IST_OFFSET",
    "NOTEBOOKS_DIR",
    "PACKAGE_ROOT",
    "PLANETARY_PARQUET",
    "PLANETS",
    "PROCESSED_DIR",
    "PROJECT_ROOT",
    "RAW_DIR",
    "REFERENCE_DIR",
    "REPORTS_DIR",
    "Settings",
    "SIGN_ABBR",
    "SIGNS",
    "chunked",
    "coerce_date",
    "ensure_dirs",
    "format_p_value",
    "format_pct",
    "get_logger",
    "iso_date",
    "read_json",
    "setup_logging",
    "significance_label",
    "summarise_frame",
    "to_utc",
    "utc_now",
    "write_json",
    "write_text",
]
