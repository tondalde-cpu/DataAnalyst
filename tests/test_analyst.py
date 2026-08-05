import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analyst import group_sums, summarize


def test_summarize_revenue():
    rows = [
        {"revenue": "100.0"},
        {"revenue": "200.0"},
        {"revenue": "300.0"},
    ]
    stats = summarize(rows, "revenue")
    assert stats["count"] == 3
    assert stats["sum"] == 600.0
    assert stats["mean"] == 200.0
    assert stats["median"] == 200.0
    assert stats["min"] == 100.0
    assert stats["max"] == 300.0


def test_group_sums():
    rows = [
        {"revenue": "100.0", "region": "North"},
        {"revenue": "200.0", "region": "South"},
        {"revenue": "50.0", "region": "North"},
    ]
    sums = group_sums(rows, "revenue", "region")
    assert sums == {"North": 150.0, "South": 200.0}
