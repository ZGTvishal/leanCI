# LeanCI

LeanCI is a lightweight command-line tool for detecting performance regressions in HTTP APIs.

## Planned features

- Benchmark HTTP endpoints and measure response latency.
- Report latency percentiles, throughput, and request failures.
- Save benchmark results as baselines and compare subsequent runs.
- Flag regressions using configurable thresholds.
- Support automated performance checks in GitHub Actions.

## Project status

Early development. Features are planned and have not yet been validated.

## Technology stack

- Python
- HTTPX for HTTP requests
- Typer for the command-line interface
- pytest for testing
- GitHub Actions for CI integration

## Goals

Build a reproducible, testable performance regression tool with clear reporting and documented measurement limitations.