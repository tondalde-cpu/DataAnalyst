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


def group_sums(rows, column, group_by):
    sums = {}
    for row in rows:
        key = row[group_by]
        sums[key] = sums.get(key, 0.0) + float(row[column])
    return sums


def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", help="Path to a CSV file")
    parser.add_argument("column", help="Numeric column to summarize")
    parser.add_argument("--group-by", help="Group sums by this column and show the top group")
    args = parser.parse_args(argv)

    rows = load_csv(args.csv_path)
    if args.column not in rows[0]:
        print(f"Column '{args.column}' not found. Available: {', '.join(rows[0])}", file=sys.stderr)
        return 1

    stats = summarize(rows, args.column)
    for key, value in stats.items():
        print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

    if args.group_by:
        if args.group_by not in rows[0]:
            print(f"Column '{args.group_by}' not found. Available: {', '.join(rows[0])}", file=sys.stderr)
            return 1
        sums = group_sums(rows, args.column, args.group_by)
        print(f"\n{args.column} by {args.group_by}:")
        for key, total in sorted(sums.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {key}: {total:.2f}")
        top_group = max(sums, key=sums.get)
        print(f"top {args.group_by}: {top_group} ({sums[top_group]:.2f})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
