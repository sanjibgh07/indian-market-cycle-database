# Official NSE Data Collection
This repository stores raw source-preserving snapshots and readable derived tables separately.
## Source contract
- Primary source: NSE India historical index data endpoint.
- NSE limits each request to a maximum 365-day range; longer histories must be split into non-overlapping windows.
- Every row retains index name, trading date, OHLC, shares traded, turnover, source URL, retrieval timestamp, and source response hash.
- Missing rows are recorded in a gap report. No values are interpolated or fabricated.
## Views
- Planetary Voice: date/event lookup and explanatory layer.
- Expert Historical: historical pattern, cycle, recurrence and confidence layer.
Both views use the same canonical market rows.
