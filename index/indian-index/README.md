# Indian Index Database

This folder stores source-preserving NSE/BSE and other Indian index time series.

## Verified coverage

- NIFTY 50 public snapshot: 1-minute data from 2017; 15-second data from 2026-09-04.
- SENSEX public snapshot: 1-minute data from 2023; 15-second data from 2026-09-15.
- Official NIFTY 50 historical series: available from 1990-07-03.
- Official BSE SENSEX launch: 1986-01-02.

The public GitHub snapshots are not 60-year datasets. Missing periods are never fabricated or interpolated.

Every imported file must record source URL, retrieval time, source commit/request, file size, SHA-256, schema, row count, min/max dates, timezone, known gaps and license notes. Raw files, normalized files, planetary ephemeris and analytical joins remain separate.

