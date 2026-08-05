# DataAnalyst

A minimal starter project for learning Claude Code: a small CLI that summarizes a numeric column from a CSV file.

## Usage

```bash
python3 analyst.py sample_data/sales.csv revenue
```

Optionally break the total down by another column and see the top group:

```bash
python3 analyst.py sample_data/sales.csv revenue --group-by region
```

## Tests

```bash
python3 -m pytest tests/
```
