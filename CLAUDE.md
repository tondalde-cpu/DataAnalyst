# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A minimal CLI tool that summarizes a numeric column from a CSV file, with an
optional group-by breakdown. Single-module Python project (`analyst.py`),
no external dependencies.

## Commands

Run the CLI:
```bash
python3 analyst.py sample_data/sales.csv revenue
python3 analyst.py sample_data/sales.csv revenue --group-by region
```

Run tests — `pytest` is not installed in this environment, so run the test
functions directly instead of `python3 -m pytest`:
```bash
python3 -c "
from tests.test_analyst import test_summarize_revenue, test_group_sums
test_summarize_revenue()
test_group_sums()
print('All tests PASSED')
"
```
(If `pytest` is available in your environment, `python3 -m pytest tests/` works too.)

## Architecture

`analyst.py` has three functions plus a CLI entry point:
- `load_csv(path)` — reads a CSV into a list of `dict` rows via `csv.DictReader`
- `summarize(rows, column)` — computes count/sum/mean/median/min/max for one column
- `group_sums(rows, column, group_by)` — sums `column` per distinct value of `group_by`
- `main(argv)` — parses args, validates the requested column(s) exist, prints
  `summarize` results always, and `group_sums` results (sorted descending, with
  the top group highlighted) only when `--group-by` is passed

Tests in `tests/test_analyst.py` import directly from `analyst.py` (path is
adjusted with `sys.path.insert` at the top of the test file) and call the pure
functions with hand-built row dicts rather than reading `sample_data/sales.csv`.
