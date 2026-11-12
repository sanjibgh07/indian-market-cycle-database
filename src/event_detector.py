"""Detection of astrological events in the planetary master.

Five families of events are detected:

``sign_ingress``
    A planet changes sidereal sign (rashi sankranti).
``retrograde_station`` / ``direct_station``
    A planet turns retrograde or direct (Vakra / Anuvakra).
``conjunction``
    Two bodies within 1 degree (yuti).
``trine`` / ``square`` / ``opposition``
    The classic major aspects within 1 degree of exactness.

Episodes are reported **once**, on the day the condition is tightest, rather
than once per day it happens to hold.  This keeps a three-day conjunction
window from being counted three times.

Every event carries a granular ``event_type`` label such as
``"Mercury Retrograde Station"`` or ``"Sun-Moon Conjunction"`` plus a coarse
``category`` used to roll results up in the report.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date
from itertools import combinations
from typing import Sequence

import numpy as np
import pandas as pd

from pathlib import Path



# Allow the module to be executed directly (``python src/<module>.py``) as
# well as through ``python -m src.<module>``.
if __package__ in (None, ""):  # pragma: no cover - direct execution path
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))

try:
    from .utils import PLANETS, SIGNS, get_logger
except ImportError:  # direct script execution
    from src.utils import PLANETS, SIGNS, get_logger

logger = get_logger(__name__)

#: Angular orb (degrees) allowed for conjunctions and major aspects.
DEFAULT_ORB = 1.0

#: Aspect definitions: name -> (exact angle, allowed orb).
ASPECTS: dict[str, tuple[float, float]] = {
    "Conjunction": (0.0, DEFAULT_ORB),
    "Trine": (120.0, DEFAULT_ORB),
    "Square": (90.0, DEFAULT_ORB),
    "Opposition": (180.0, DEFAULT_ORB),
}

#: Categories used for roll-ups.
CATEGORY_INGRESS = "sign_ingress"
CATEGORY_RETROGRADE = "retrograde_station"
CATEGORY_DIRECT = "direct_station"
CATEGORY_CONJUNCTION = "conjunction"
CATEGORY_ASPECT = "aspect"

EVENT_COLUMNS: tuple[str, ...] = (
    "event_id", "date", "event_type", "category", "planets",
    "description", "orb", "primary_planet", "secondary_planet",
    "sign_before", "sign_after",
)


def _separation(longitudes_a: np.ndarray, longitudes_b: np.ndarray) -> np.ndarray:
    """Return the 0-180 degree separation between two longitude series."""
    diff = np.abs(longitudes_a - longitudes_b) % 360.0
    return np.minimum(diff, 360.0 - diff)


def _episodes(mask: np.ndarray) -> list[tuple[int, int]]:
    """Return ``(start, end)`` index pairs of contiguous ``True`` runs."""
    if mask.size == 0:
        return []
    padded = np.concatenate(([False], mask, [False]))
    changes = np.flatnonzero(padded[1:] != padded[:-1])
    return list(zip(changes[0::2].tolist(), changes[1::2].tolist()))


@dataclass
class EventDetector:
    """Detect ingress, station, conjunction and aspect events.

    Args:
        orb: Angular tolerance for conjunctions and aspects, in degrees.
    """

    orb: float = DEFAULT_ORB

    def detect(self, planetary: pd.DataFrame) -> pd.DataFrame:
        """Detect every event in a wide planetary frame.

        Args:
            planetary: Frame produced by
                :func:`src.planetary.compute_planetary_master`.

        Returns:
            DataFrame with one row per event, ordered by date.
        """
        if planetary is None or len(planetary) == 0:
            return pd.DataFrame(columns=list(EVENT_COLUMNS))

        frame = planetary.sort_values("date").reset_index(drop=True)
        days = list(frame["date"])
        events: list[dict] = []

        events.extend(self._detect_ingresses(frame, days))
        events.extend(self._detect_stations(frame, days))
        events.extend(self._detect_pair_events(frame, days))

        result = pd.DataFrame(events)
        if result.empty:
            return pd.DataFrame(columns=list(EVENT_COLUMNS))

        result = result.sort_values(["date", "event_type"]).reset_index(drop=True)
        result["event_id"] = np.arange(1, len(result) + 1)
        result = result[list(EVENT_COLUMNS)]
        logger.info(
            "Detected %d events (%d ingress, %d stations, %d conjunctions/aspects)",
            len(result),
            int((result["category"] == CATEGORY_INGRESS).sum()),
            int(result["category"].isin([CATEGORY_RETROGRADE, CATEGORY_DIRECT]).sum()),
            int(result["category"].isin([CATEGORY_CONJUNCTION, CATEGORY_ASPECT]).sum()),
        )
        return result

    # ------------------------------------------------------------------ #
    # Ingresses
    # ------------------------------------------------------------------ #

    def _detect_ingresses(self, frame: pd.DataFrame, days: Sequence[date]) -> list[dict]:
        """Detect sign changes (rashi sankranti) for every planet."""
        found: list[dict] = []
        for planet in PLANETS:
            column = f"{planet.lower()}_sign"
            if column not in frame.columns:
                continue
            signs = frame[column].to_numpy()
            changed = np.flatnonzero(np.diff(signs) != 0) + 1
            for index in changed:
                before = int(signs[index - 1])
                after = int(signs[index])
                degree = float(frame.iloc[index][f"{planet.lower()}_degree"])
                found.append({
                    "date": days[index],
                    "event_type": f"{planet} Sign Ingress",
                    "category": CATEGORY_INGRESS,
                    "planets": planet,
                    "description": (
                        f"{planet} entered {SIGNS[after]} at {degree:.2f} deg "
                        f"(sidereal, Lahiri) - rashi sankranti."
                    ),
                    "orb": None,
                    "primary_planet": planet,
                    "secondary_planet": None,
                    "sign_before": SIGNS[before],
                    "sign_after": SIGNS[after],
                })
        return found

    # ------------------------------------------------------------------ #
    # Retrograde / direct stations
    # ------------------------------------------------------------------ #

    def _detect_stations(self, frame: pd.DataFrame, days: Sequence[date]) -> list[dict]:
        """Detect retrograde and direct stations."""
        found: list[dict] = []
        for planet in PLANETS:
            column = f"{planet.lower()}_is_retrograde"
            if column not in frame.columns:
                continue
            retro = frame[column].to_numpy().astype(bool)
            flips = np.flatnonzero(np.diff(retro.astype(int)) != 0) + 1
            for index in flips:
                became_retro = bool(retro[index])
                sign = int(frame.iloc[index][f"{planet.lower()}_sign"])
                degree = float(frame.iloc[index][f"{planet.lower()}_degree"])
                if became_retro:
                    event_type = f"{planet} Retrograde Station"
                    category = CATEGORY_RETROGRADE
                    description = (
                        f"{planet} turned retrograde at {degree:.2f} deg "
                        f"{SIGNS[sign]} (Vakra) - planet is now moving backwards."
                    )
                else:
                    event_type = f"{planet} Direct Station"
                    category = CATEGORY_DIRECT
                    description = (
                        f"{planet} turned direct at {degree:.2f} deg "
                        f"{SIGNS[sign]} (Anuvakra) - planet is now moving forwards."
                    )
                found.append({
                    "date": days[index],
                    "event_type": event_type,
                    "category": category,
                    "planets": planet,
                    "description": description,
                    "orb": None,
                    "primary_planet": planet,
                    "secondary_planet": None,
                    "sign_before": None,
                    "sign_after": SIGNS[sign],
                })
        return found

    # ------------------------------------------------------------------ #
    # Conjunctions and aspects
    # ------------------------------------------------------------------ #

    def _detect_pair_events(self, frame: pd.DataFrame, days: Sequence[date]) -> list[dict]:
        """Detect conjunctions and major aspects between every pair of bodies."""
        found: list[dict] = []
        longitudes = {
            planet: frame[f"{planet.lower()}_longitude"].to_numpy(dtype=float)
            for planet in PLANETS
            if f"{planet.lower()}_longitude" in frame.columns
        }

        for planet_a, planet_b in combinations(sorted(longitudes), 2):
            separation = _separation(longitudes[planet_a], longitudes[planet_b])
            for aspect, (angle, tolerance) in ASPECTS.items():
                orb_series = np.abs(separation - angle)
                hits = orb_series <= tolerance
                for start, end in _episodes(hits):
                    window = orb_series[start:end]
                    tightest = int(np.argmin(window))
                    position = start + tightest
                    orb_value = float(orb_series[position])
                    if aspect == "Conjunction":
                        category = CATEGORY_CONJUNCTION
                    else:
                        category = CATEGORY_ASPECT
                    sign_a = int(frame.iloc[position][f"{planet_a.lower()}_sign"])
                    sign_b = int(frame.iloc[position][f"{planet_b.lower()}_sign"])
                    found.append({
                        "date": days[position],
                        "event_type": f"{planet_a}-{planet_b} {aspect}",
                        "category": category,
                        "planets": f"{planet_a},{planet_b}",
                        "description": (
                            f"{planet_a} ({sign_a} {SIGNS[sign_a]}) and "
                            f"{planet_b} ({sign_b} {SIGNS[sign_b]}) formed a "
                            f"{aspect} with an orb of {orb_value:.2f} deg "
                            f"(separation {separation[position]:.2f} deg)."
                        ),
                        "orb": orb_value,
                        "primary_planet": planet_a,
                        "secondary_planet": planet_b,
                        "sign_before": None,
                        "sign_after": None,
                    })
        return found


def detect_events(planetary: pd.DataFrame, orb: float = DEFAULT_ORB) -> pd.DataFrame:
    """Detect every astrological event in a wide planetary frame.

    Args:
        planetary: Frame produced by
            :func:`src.planetary.compute_planetary_master`.
        orb: Angular tolerance for conjunctions and aspects.

    Returns:
        DataFrame with one row per event.
    """
    return EventDetector(orb=orb).detect(planetary)


def events_summary(events: pd.DataFrame) -> pd.DataFrame:
    """Summarise event counts by category and event type."""
    if events is None or len(events) == 0:
        return pd.DataFrame(columns=["event_type", "category", "count", "first_date", "last_date"])
    grouped = (
        events.groupby(["category", "event_type"], as_index=False)
        .agg(count=("event_id", "count"),
             first_date=("date", "min"),
             last_date=("date", "max"))
        .sort_values(["category", "count"], ascending=[True, False])
        .reset_index(drop=True)
    )
    return grouped


def event_categories() -> dict[str, str]:
    """Return a mapping of event type to its category (for roll-ups)."""
    return {
        "sign_ingress": "Sign ingress (rashi sankranti)",
        "retrograde_station": "Retrograde station (Vakra)",
        "direct_station": "Direct station (Anuvakra)",
        "conjunction": "Conjunction (yuti)",
        "aspect": "Major aspect (trine / square / opposition)",
    }


__all__ = [
    "ASPECTS",
    "DEFAULT_ORB",
    "EVENT_COLUMNS",
    "EventDetector",
    "detect_events",
    "event_categories",
    "events_summary",
    "main",
]


# --------------------------------------------------------------------------- #
# Script entry point
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    """Detect events from the processed planetary master and save them.

    Usage::

        python src/event_detector.py
    """
    import argparse

    try:
        from .utils import PROCESSED_DIR, Settings, ensure_dirs, setup_logging
    except ImportError:  # direct script execution
        from src.utils import PROCESSED_DIR, Settings, ensure_dirs, setup_logging

    parser = argparse.ArgumentParser(description="Detect planetary events.")
    parser.add_argument("--planetary", default=None,
                        help="Path to planetary_master.parquet (default: data/processed)")
    parser.add_argument("--output", default=None,
                        help="Path for the events CSV (default: data/processed/planetary_events.csv)")
    parser.add_argument("--log-level", default="INFO")
    args = parser.parse_args(argv)

    setup_logging(args.log_level)
    settings = Settings.from_env()
    ensure_dirs()

    source = Path(args.planetary) if args.planetary else (settings.processed_data_dir / "planetary_master.parquet")
    if not Path(source).exists():
        print(f"Planetary master not found at {source}. Run the pipeline first.", file=sys.stderr)
        return 1

    frame = pd.read_parquet(source)
    frame["date"] = pd.to_datetime(frame["date"]).dt.date
    events = detect_events(frame)

    destination = Path(args.output) if args.output else (settings.processed_data_dir / "planetary_events.csv")
    destination.parent.mkdir(parents=True, exist_ok=True)
    copy = events.copy()
    copy["date"] = copy["date"].astype(str)
    copy.to_csv(destination, index=False)
    try:
        copy.to_parquet(destination.with_suffix(".parquet"), index=False)
    except Exception as exc:  # pragma: no cover
        logger.warning("Parquet write failed: %s", exc)

    print(f"Detected {len(events):,} events -> {destination}")
    if len(events):
        print(events.groupby("category").size().to_string())
    return 0


if __name__ == "__main__":
    sys.exit(main())
