# Project Scope

## Objective
Build a local-first data pipeline/platform that tracks PC hardware prices over time and follows industry-style workflow patterns.

## V1 Scope
### Categories
- CPU
- GPU
- SSD

### Product Count
- 12 total products

### Sources
- 1 initial source

### Refresh Pattern
- Manual run at first
- Designed so it can later run daily

## Grain
One row per:
- product
- source
- observation timestamp

## Outputs
### Raw
Untouched source captures and parsed extracts

### Staging
Cleaned, typed, minimally standardized source data

### Marts
- Latest prices by product
- Price history over time
- Average price by category

## Non-Goals for V1
- Full market coverage
- Perfect entity resolution
- Multi-source deduplication
- Real-time streaming
- Full dashboarding stack

## Success Criteria
- A single command can run extraction successfully
- Raw data is saved with timestamped files
- Parsed data lands in Parquet
- DuckDB can query extracted data
- dbt produces at least one fact table and one mart
