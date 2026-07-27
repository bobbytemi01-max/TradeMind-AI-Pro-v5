"""Simple Fibonacci retracement helper."""

from __future__ import annotations

from typing import Dict


def fibonacci_levels(high: float, low: float) -> Dict[str, float]:
    """Return key Fibonacci retracement levels between a swing high and low."""
    if high < low:
        high, low = low, high

    distance = high - low
    if distance <= 0:
        return {"0.0": high, "100.0": low}

    return {
        "0.0": high,
        "23.6": high - distance * 0.236,
        "38.2": high - distance * 0.382,
        "50.0": high - distance * 0.5,
        "61.8": high - distance * 0.618,
        "78.6": high - distance * 0.786,
        "100.0": low,
    }
