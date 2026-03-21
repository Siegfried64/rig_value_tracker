# Rig Value Guide

A local-first personal data platform for tracking computer hardware prices over time using production-style workflows.

## Goals
- Practice data engineering workflow locally
- Track PC component prices over time
- Use layered data design: raw -> staging -> marts
- Build good habits around documentation, testing, and repeatable runs

## V1 Scope
- Categories: CPU, GPU, SSD
- Products: 12 canonical products
- Sources: 1 source initially
- Refresh cadence: daily or manual daily-style runs
- Storage: local files + DuckDB
- Transformation: dbt
- Orchestration: manual first, Dagster later

## Core Questions
- What is the latest price for each tracked product?
- How has price changed over time?
- What is the average price trend by category?

## Planned Stack
- Python
- DuckDB
- dbt Core
- Docker Compose
- Dagster later

## Project Principles
- Raw data is immutable
- Every run is timestamped
- Every table has a purpose
- Every assumption should become a test
