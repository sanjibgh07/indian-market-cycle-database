"""Celestial Indices — Indian Stock Market & Planetary Correlation Engine.

The package is deliberately layered so that every stage can be used on its own:

``src.trading_calendar``
    Builds the authoritative NSE trading calendar.
``src.planetary``
    Computes sidereal (Lahiri) planetary positions at market close.
``src.data_pipeline``
    The core: fetches, aligns, validates and persists the master dataset.
``src.event_detector``
    Finds ingresses, stations, conjunctions and aspects.
``src.correlation_engine``
    Runs the forward-return event studies.
``src.reporter``
    Renders the human-readable effects report.
"""

from __future__ import annotations

__version__ = "1.0.0"
__all__ = ["__version__"]
