#!/usr/bin/env python3
"""Summarize a numeric column from a CSV file."""
import argparse
import csv
import statistics
import sys


def summarize(rows, column):
    values = [float(row[column]) for row in rows]
    return {
        "count": len(values),
        "sum": sum(values),
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "min": min(values),
        "max": max(values),
    }


def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Path to a CSV file")
    parser.add_argument("column", help="Numeric column to summarize")
    args = parser.parse_args(argv)

    rows = load_csv(args.csv_path)
    if args.column not in rows[0]:
        print(f"Column '{args.column}' not found. Available: {', '.join(rows[0])}", file=sys.stderr)
        return 1

    stats = summarize(rows, args.column)
    for key, value in stats.items():
        print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
