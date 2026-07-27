"""Forecast generation logic."""

from typing import Sequence


def generate_forecast(prices: Sequence[float]) -> float:
    return float(prices[-1]) if prices else 0.0
