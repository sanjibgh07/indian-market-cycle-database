"""Idempotent daily market-master and ephemeris updater.

The updater is deliberately separate from the analysis pipeline:

* Yahoo Finance is used only as a clearly labelled backup/live feed.
* Existing rows are upserted, never duplicated.
* Swiss Ephemeris is computed locally by the normal pipeline.
* A JSON status file makes the last attempt visible to the UI and scheduler.

Configure additional index tickers with environment variables when a provider
has a reliable symbol for them::

    CELESTIAL_TICKER_NIFTY_MIDCAP_100=...
    CELESTIAL_TICKER_NIFTY_MIDCAP_150=...

The default symbols cover the three stable Yahoo index symbols. An unknown
index is skipped and recorded rather than silently substituting another index.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import sys
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

import pandas as pd

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_pipeline import run_pipeline  # noqa: E402
from src.utils import Settings, setup_logging  # noqa: E402


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
MASTER_DB = DATA_DIR / "INDIAN_MARKET_MASTER_PRE_EPHEMERIS.sqlite"
RAW_DIR = DATA_DIR / "raw"
STATUS_PATH = DATA_DIR / "update_status.json"
LOCK_PATH = DATA_DIR / ".live_update.lock"

DEFAULT_TICKERS = {
    "SENSEX": "^BSESN",
    "NIFTY_50": "^NSEI",
    "NIFTY_BANK": "^NSEBANK",
    # Deliberately blank: do not confuse Smallcap/Midcap indices.
    "NIFTY_MIDCAP_100": "",
    "NIFTY_MIDCAP_150": "",
}


def _today_ist() -> date:
    return datetime.now(timezone(timedelta(hours=5, minutes=30))).date()


def _write_status(payload: dict) -> None:
    STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATUS_PATH.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")


def read_status() -> dict:
    if not STATUS_PATH.exists():
        return {"status": "never_run", "message": "No automatic update has run yet."}
    try:
        return json.loads(STATUS_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return {"status": "corrupt", "message": str(exc)}


def _tickers() -> dict[str, str]:
    return {
        index: os.getenv(f"CELESTIAL_TICKER_{index}", default).strip()
        for index, default in DEFAULT_TICKERS.items()
    }


def _last_date(connection: sqlite3.Connection, index_name: str) -> date | None:
    row = connection.execute(
        "SELECT MAX(date) FROM market_ohlcv WHERE index_name = ?", (index_name,)
    ).fetchone()
    return date.fromisoformat(row[0]) if row and row[0] else None


def _fetch_chart(ticker: str, start: date, end: date) -> pd.DataFrame:
    period1 = int(datetime.combine(start, datetime.min.time(), tzinfo=timezone.utc).timestamp())
    period2 = int(datetime.combine(end + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).timestamp())
    url = (
        "https://query1.finance.yahoo.com/v8/finance/chart/"
        f"{quote(ticker, safe='')}?period1={period1}&period2={period2}&interval=1d"
    )
    request = Request(url, headers={"User-Agent": "CelestialIndices/1.0"})
    with urlopen(request, timeout=30) as response:  # noqa: S310 - fixed HTTPS host
        payload = json.loads(response.read().decode("utf-8"))
    result = (payload.get("chart") or {}).get("result") or []
    if not result:
        raise RuntimeError(f"No Yahoo result for {ticker}")
    item = result[0]
    timestamps = item.get("timestamp") or []
    quote_data = ((item.get("indicators") or {}).get("quote") or [{}])[0]
    rows: list[dict] = []
    for pos, stamp in enumerate(timestamps):
        values = {key: (quote_data.get(key) or [None] * len(timestamps))[pos]
                  for key in ("open", "high", "low", "close", "volume")}
        if any(values[key] is None for key in ("open", "high", "low", "close")):
            continue
        day = datetime.fromtimestamp(stamp, tz=timezone.utc).date()
        rows.append({"date": day.isoformat(), **values})
    return pd.DataFrame(rows).drop_duplicates("date").sort_values("date")


def _append_raw(index_name: str, frame: pd.DataFrame) -> None:
    if frame.empty:
        return
    path = RAW_DIR / f"{index_name}_yahoo.csv"
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = pd.read_csv(path)
        frame = pd.concat([old, frame], ignore_index=True)
    frame.drop_duplicates("date", keep="last").sort_values("date").to_csv(path, index=False)


def _holiday_dates() -> set[str]:
    path = DATA_DIR / "reference" / "nse_holidays.json"
    if not path.exists():
        return set()
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("holidays", payload) if isinstance(payload, dict) else payload
    return {str(row.get("date", ""))[:10] for row in rows}


def _upsert_master(rows: dict[str, pd.DataFrame], today: date) -> int:
    if not MASTER_DB.exists():
        raise FileNotFoundError(MASTER_DB)
    holiday_dates = _holiday_dates()
    observed = {str(d)[:10] for frame in rows.values() for d in frame.get("date", [])}
    inserted = 0
    with sqlite3.connect(MASTER_DB) as connection:
        connection.execute("PRAGMA busy_timeout=30000")
        for index_name, frame in rows.items():
            for record in frame.to_dict("records"):
                connection.execute(
                    """INSERT OR REPLACE INTO market_ohlcv
                    (date,index_name,open,high,low,close,volume,is_special_session)
                    VALUES (?,?,?,?,?,?,?,?)""",
                    (record["date"], index_name, float(record["open"]), float(record["high"]),
                     float(record["low"]), float(record["close"]),
                     None if pd.isna(record.get("volume")) else float(record["volume"]),
                     int(datetime.fromisoformat(record["date"]).weekday() >= 5)),
                )
                inserted += 1
            _append_raw(index_name, frame)

        current = connection.execute("SELECT MAX(date) FROM trading_calendar").fetchone()[0]
        start = date.fromisoformat(current) + timedelta(days=1) if current else today
        day = start
        while day <= today:
            iso = day.isoformat()
            is_weekday = day.weekday() < 5
            is_trading = iso in observed
            if iso in holiday_dates:
                reason, session = "Official NSE holiday", "holiday"
            elif iso in observed and day.weekday() >= 5:
                reason, session = None, "special"
            elif is_trading:
                reason, session = None, "regular"
            elif not is_weekday:
                reason, session = "Weekend", "weekend"
            else:
                reason, session = "No provider bar yet", "closed"
            connection.execute(
                "INSERT OR REPLACE INTO trading_calendar(date,is_trading_day,holiday_reason,session_type) VALUES (?,?,?,?)",
                (iso, int(is_trading), reason, session),
            )
            day += timedelta(days=1)

        now = datetime.now(timezone(timedelta(hours=5, minutes=30))).isoformat(timespec="seconds")
        connection.execute(
            "INSERT OR REPLACE INTO meta(key,value) VALUES (?,?)",
            ("last_live_update_ist", now),
        )
        connection.execute(
            "INSERT OR REPLACE INTO meta(key,value) VALUES (?,?)",
            ("live_update_source", "Yahoo Finance chart API; rows labelled yahoo_backup"),
        )
    return inserted


def run_update(rebuild: bool = True) -> dict:
    """Fetch new bars, upsert them, then rebuild all derived artefacts."""
    if LOCK_PATH.exists():
        raise RuntimeError(f"Update already running: {LOCK_PATH}")
    LOCK_PATH.write_text(str(os.getpid()), encoding="ascii")
    started = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    result = {"status": "running", "started_ist": started.isoformat(timespec="seconds"), "indices": {}, "errors": []}
    try:
        today = _today_ist()
        rows: dict[str, pd.DataFrame] = {}
        with sqlite3.connect(MASTER_DB) as connection:
            for index_name, ticker in _tickers().items():
                if not ticker:
                    result["indices"][index_name] = {"status": "not_configured"}
                    result["errors"].append(f"{index_name}: ticker not configured")
                    continue
                last = _last_date(connection, index_name) or (today - timedelta(days=3650))
                try:
                    frame = _fetch_chart(ticker, max(last - timedelta(days=7), date(1999, 1, 1)), today)
                    rows[index_name] = frame
                    result["indices"][index_name] = {"status": "ok", "ticker": ticker, "rows_seen": len(frame), "last_existing": str(last)}
                except Exception as exc:  # noqa: BLE001
                    result["indices"][index_name] = {"status": "error", "ticker": ticker, "error": str(exc)}
                    result["errors"].append(f"{index_name}: {exc}")
        result["rows_upserted"] = _upsert_master(rows, today)
        if rebuild:
            pipeline = run_pipeline(settings=Settings.from_env(), master_path=MASTER_DB)
            result["pipeline_seconds"] = pipeline["duration_seconds"]
            result["alignment_passed"] = bool(pipeline["validation"].passed)
            result["derived_last_date"] = str(pipeline["aligned_long"]["date"].max()) if len(pipeline["aligned_long"]) else None
        result["status"] = "ok" if not result["errors"] else "partial"
    except Exception as exc:  # noqa: BLE001
        result["status"] = "error"
        result["errors"].append(str(exc))
        raise
    finally:
        result["finished_ist"] = datetime.now(timezone(timedelta(hours=5, minutes=30))).isoformat(timespec="seconds")
        _write_status(result)
        LOCK_PATH.unlink(missing_ok=True)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Update market data and rebuild Celestial artefacts")
    parser.add_argument("--once", action="store_true", help="Run one update and exit")
    parser.add_argument("--no-rebuild", action="store_true", help="Only update the master database")
    args = parser.parse_args()
    setup_logging("INFO")
    payload = run_update(rebuild=not args.no_rebuild)
    print(json.dumps(payload, indent=2, default=str))
    return 0 if payload["status"] in {"ok", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
