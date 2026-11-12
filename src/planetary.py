"""Vedic planetary positions (Swiss Ephemeris, Lahiri ayanamsa).

Every position is evaluated at **15:30 IST** — the close of the regular NSE
session — on the *same calendar date* as the market bar it is paired with.

Design notes
------------
* Sidereal longitudes come from ``swe.FLG_SWIEPH | swe.FLG_SIDEREAL`` with
  the Lahiri (Chitrapaksha) ayanamsa selected via ``swe.set_sid_mode``.
* Retrograde status is taken from the ephemeris' own daily speed rather than
  from a day-over-day difference: a planet is retrograde when its apparent
  sidereal motion is negative.  The Moon is never retrograde; the mean lunar
  node (Rahu) and its opposite point (Ketu) are always retrograde, which is
  the standard Vedic convention.
* The module computes a whole range in one pass and caches nothing across
  processes, so a ~27-year daily series (roughly 10k days x 9 bodies) is
  produced in a few seconds.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from typing import Mapping, Sequence

import pandas as pd

from .utils import IST_OFFSET, PLANETS, SIGN_ABBR, SIGNS, get_logger

logger = get_logger(__name__)

# --------------------------------------------------------------------------- #
# Swiss Ephemeris bindings
# --------------------------------------------------------------------------- #

try:
    import swisseph as swe
except ImportError as exc:  # pragma: no cover - hard dependency
    raise ImportError(
        "pyswisseph is required for planetary computation. "
        "Install it with: pip install pyswisseph"
    ) from exc

#: Body id for each supported planet.  Ketu is derived from Rahu (mean node).
BODY_IDS: dict[str, int] = {
    "Sun": swe.SUN,
    "Moon": swe.MOON,
    "Mercury": swe.MERCURY,
    "Venus": swe.VENUS,
    "Mars": swe.MARS,
    "Jupiter": swe.JUPITER,
    "Saturn": swe.SATURN,
    "Rahu": swe.MEAN_NODE,
}

#: Ketu is always the point 180 degrees opposite the mean node.
KETU_OFFSET = 180.0

#: Ayanamsa identifiers supported by ``swe.set_sid_mode``.
AYANAMSA_MODES: dict[str, int] = {
    "lahiri": swe.SIDM_LAHIRI,
    "chitrapaksha": swe.SIDM_LAHIRI,
    "ram": swe.SIDM_RAMAN,
    "raman": swe.SIDM_RAMAN,
    "krishnamurti": swe.SIDM_KRISHNAMURTI,
    "fagan": swe.SIDM_FAGAN_BRADLEY,
}

#: Computation flags: Swiss Ephemeris, sidereal, and the daily speed vector.
CALC_FLAGS = swe.FLG_SWIEPH | swe.FLG_SIDEREAL | swe.FLG_SPEED

#: Bodies that are never retrograde.
ALWAYS_DIRECT: frozenset[str] = frozenset({"Moon"})


def configure_sidereal(ayanamsa: str = "lahiri") -> None:
    """Select the ayanamsa used for all subsequent calculations.

    Args:
        ayanamsa: One of ``lahiri`` (default), ``ram`` or ``krishnamurti``.

    Raises:
        ValueError: When the requested ayanamsa is unknown.
    """
    key = (ayanamsa or "lahiri").strip().lower()
    mode = AYANAMSA_MODES.get(key)
    if mode is None:
        raise ValueError(
            f"Unknown ayanamsa {ayanamsa!r}; choose one of {sorted(AYANAMSA_MODES)}"
        )
    swe.set_ephe_path(None)
    swe.set_sid_mode(mode, 0, 0)
    logger.info("Swiss Ephemeris configured with ayanamsa=%s", key)


def julian_day(day: date, moment: time = time(15, 30), offset: timedelta = IST_OFFSET) -> float:
    """Return the Julian day number for a local market-close instant.

    The default instant is 15:30 IST, i.e. 10:00 UTC.

    Args:
        day: Calendar date of the session.
        moment: Local wall-clock time of the evaluation instant.
        offset: Offset of the local zone from UTC (IST = +05:30).

    Returns:
        Julian day as a float.
    """
    local = datetime.combine(day, moment)
    utc = local - offset
    utc_hour = utc.hour + utc.minute / 60.0 + utc.second / 3600.0
    return swe.julday(utc.year, utc.month, utc.day, utc_hour, swe.GREG_CAL)


# --------------------------------------------------------------------------- #
# Position computation
# --------------------------------------------------------------------------- #

@dataclass(frozen=True)
class Position:
    """A single planet's position on a single day."""

    planet: str
    longitude: float
    speed: float
    sign: int
    degree: float
    is_retrograde: bool

    @property
    def sign_name(self) -> str:
        """Name of the sidereal sign the planet occupies."""
        return SIGNS[self.sign]

    @property
    def sign_abbr(self) -> str:
        """Three-letter abbreviation of the sidereal sign."""
        return SIGN_ABBR[self.sign]


def compute_position(day: date, planet: str, moment: time = time(15, 30),
                     ayanamsa: str = "lahiri") -> Position:
    """Compute one planet's sidereal position for one date.

    Args:
        day: Calendar date.
        planet: Name of the planet (see :data:`PLANETS`).
        moment: Local evaluation instant, default 15:30 IST.
        ayanamsa: Ayanamsa selection.

    Returns:
        The :class:`Position` of the planet.

    Raises:
        KeyError: When ``planet`` is not supported.
    """
    if planet not in PLANETS:
        raise KeyError(f"Unsupported planet {planet!r}; expected one of {PLANETS}")

    configure_sidereal(ayanamsa)
    jd = julian_day(day, moment)

    if planet == "Ketu":
        rahu = swe.calc_ut(jd, BODY_IDS["Rahu"], CALC_FLAGS)
        longitude = (rahu[0][0] + KETU_OFFSET) % 360.0
        speed = rahu[0][3]
    else:
        result = swe.calc_ut(jd, BODY_IDS[planet], CALC_FLAGS)
        longitude = result[0][0] % 360.0
        speed = result[0][3]

    sign = int(longitude // 30)
    degree = longitude - sign * 30
    is_retrograde = planet not in ALWAYS_DIRECT and speed < 0

    return Position(
        planet=planet,
        longitude=longitude,
        speed=speed,
        sign=sign,
        degree=degree,
        is_retrograde=is_retrograde,
    )


def compute_positions_for_date(day: date, moment: time = time(15, 30),
                               ayanamsa: str = "lahiri") -> dict[str, Position]:
    """Compute every planet's position for one date."""
    return {
        planet: compute_position(day, planet, moment=moment, ayanamsa=ayanamsa)
        for planet in PLANETS
    }


def compute_planetary_master(
    start: date,
    end: date,
    moment: time = time(15, 30),
    ayanamsa: str = "lahiri",
    planets: Sequence[str] = PLANETS,
) -> pd.DataFrame:
    """Compute the planetary master table for every calendar day in a range.

    The returned frame is *wide*: one row per calendar date with a
    ``<planet>_sign``, ``<planet>_degree``, ``<planet>_longitude`` and
    ``<planet>_is_retrograde`` column for each body, plus the Moon's sign as
    ``moon_sign_name`` for convenience.

    Args:
        start: First calendar date (inclusive).
        end: Last calendar date (inclusive).
        moment: Local evaluation instant, default 15:30 IST.
        ayanamsa: Ayanamsa selection.
        planets: Bodies to include.

    Returns:
        DataFrame indexed by ``date`` (datetime.date) with the columns above.
    """
    if start > end:
        raise ValueError(f"start ({start}) must not be after end ({end})")

    configure_sidereal(ayanamsa)

    days: list[date] = []
    cursor = start
    while cursor <= end:
        days.append(cursor)
        cursor += timedelta(days=1)

    # Pre-compute Julian days once.
    jds = [julian_day(d, moment) for d in days]

    # --- raw longitudes and speeds ----------------------------------------
    raw: dict[str, list[float]] = {planet: [] for planet in planets}
    speeds: dict[str, list[float]] = {planet: [] for planet in planets}

    for jd in jds:
        for planet in planets:
            if planet == "Ketu":
                node = swe.calc_ut(jd, BODY_IDS["Rahu"], CALC_FLAGS)
                raw["Ketu"].append((node[0][0] + KETU_OFFSET) % 360.0)
                speeds["Ketu"].append(node[0][3])
            else:
                result = swe.calc_ut(jd, BODY_IDS[planet], CALC_FLAGS)
                raw[planet].append(result[0][0] % 360.0)
                speeds[planet].append(result[0][3])

    # --- assemble the wide frame ------------------------------------------
    frame = pd.DataFrame({"date": days})
    for planet in planets:
        longitudes = raw[planet]
        signs = [int(lon // 30) for lon in longitudes]
        degrees = [lon - s * 30 for lon, s in zip(longitudes, signs)]
        retro = [
            False if planet in ALWAYS_DIRECT else speed < 0
            for speed in speeds[planet]
        ]
        frame[f"{planet.lower()}_sign"] = signs
        frame[f"{planet.lower()}_degree"] = [round(d, 6) for d in degrees]
        frame[f"{planet.lower()}_longitude"] = [round(lon, 6) for lon in longitudes]
        frame[f"{planet.lower()}_is_retrograde"] = retro

    frame["moon_sign_name"] = [SIGNS[s] for s in frame["moon_sign"]]
    frame["day"] = pd.to_datetime(frame["date"]).dt.day_name()

    logger.info(
        "Computed planetary master %s -> %s (%d days x %d bodies)",
        start, end, len(frame), len(planets),
    )
    return frame


def planetary_master_to_long(
    wide: pd.DataFrame,
    planets: Sequence[str] = PLANETS,
) -> pd.DataFrame:
    """Reshape the wide planetary frame into the long (date, planet) form.

    The long form is what the ``planetary_positions`` table stores.

    Args:
        wide: Frame produced by :func:`compute_planetary_master`.
        planets: Bodies to include.

    Returns:
        DataFrame with ``date``, ``planet``, ``sign``, ``degree``,
        ``is_retrograde`` and ``longitude``.
    """
    records: list[dict] = []
    for _, row in wide.iterrows():
        for planet in planets:
            key = planet.lower()
            records.append(
                {
                    "date": row["date"],
                    "planet": planet,
                    "sign": int(row[f"{key}_sign"]),
                    "degree": float(row[f"{key}_degree"]),
                    "is_retrograde": bool(row[f"{key}_is_retrograde"]),
                    "longitude": float(row[f"{key}_longitude"]),
                }
            )
    return pd.DataFrame(records, columns=[
        "date", "planet", "sign", "degree", "is_retrograde", "longitude"
    ])


def position_sign_label(planet: str, sign: int, degree: float) -> str:
    """Format a position as e.g. ``Mercury 12.34 Libra``."""
    return f"{planet} {degree:.2f} {SIGNS[int(sign) % 12]}"


def describe_positions(wide_row: Mapping[str, object], planets: Sequence[str] = PLANETS) -> str:
    """Render a single wide row as a human-readable multi-line summary."""
    lines = []
    for planet in planets:
        key = planet.lower()
        sign = int(wide_row[f"{key}_sign"])
        degree = float(wide_row[f"{key}_degree"])
        retro = bool(wide_row[f"{key}_is_retrograde"])
        marker = " R" if retro else ""
        lines.append(f"  {planet:<8} {degree:6.2f} {SIGNS[sign]}{marker}")
    return "\n".join(lines)


def check_ephemeris(ayanamsa: str = "lahiri") -> dict[str, float]:
    """Return the ephemeris' ayanamsa offset for a reference instant.

    Useful as a sanity check that the sidereal mode is actually active.

    Args:
        ayanamsa: Ayanamsa selection.

    Returns:
        Mapping with ``ayanamsa`` (degrees) and ``julian_day`` (the instant used).
    """
    configure_sidereal(ayanamsa)
    jd = swe.julday(2024, 1, 1, 10.0, swe.GREG_CAL)
    offset = swe.get_ayanamsa_ut(jd)
    return {"ayanamsa": float(offset), "julian_day": float(jd)}


__all__ = [
    "ALWAYS_DIRECT",
    "BODY_IDS",
    "Position",
    "check_ephemeris",
    "compute_planetary_master",
    "compute_position",
    "compute_positions_for_date",
    "configure_sidereal",
    "describe_positions",
    "julian_day",
    "planetary_master_to_long",
    "position_sign_label",
]
