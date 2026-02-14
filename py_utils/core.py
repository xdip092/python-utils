"""Reusable helper functions for Python projects."""

from __future__ import annotations

import re
from statistics import mean


def normalize_text(text: str) -> str:
    """Normalize user input text by trimming and collapsing spaces."""
    cleaned = re.sub(r"\s+", " ", text or "").strip()
    return cleaned.lower()


def chunk_list(values: list, size: int) -> list[list]:
    """Split a list into fixed-size chunks."""
    if size <= 0:
        raise ValueError("size must be greater than 0")
    return [values[i : i + size] for i in range(0, len(values), size)]


def moving_average(values: list[float], window: int = 3) -> list[float]:
    """Compute moving average for a numeric list."""
    if window <= 0:
        raise ValueError("window must be greater than 0")
    if len(values) < window:
        return []

    result = []
    for i in range(len(values) - window + 1):
        result.append(round(mean(values[i : i + window]), 4))
    return result
