"""Candlestick rendering."""

from __future__ import annotations

from typing import List, Tuple


class Candlestick:
    """Represent a single candlestick."""

    def __init__(self, time: str, open_: float, high: float, low: float, close: float) -> None:
        self.time = time
        self.open = open_
        self.high = high
        self.low = low
        self.close = close

    def is_bullish(self) -> bool:
        """Check if candle is bullish (close > open)."""
        return self.close > self.open

    def body_height(self) -> float:
        """Get the body height (absolute value of close - open)."""
        return abs(self.close - self.open)

    def wick_range(self) -> float:
        """Get the total wick range (high - low)."""
        return self.high - self.low


class CandleRenderer:
    """Render candlesticks on a chart."""

    def __init__(self) -> None:
        self.candles: List[Candlestick] = []

    def add_candle(self, candle: Candlestick) -> None:
        """Add a candlestick to render."""
        self.candles.append(candle)

    def render(self) -> str:
        """Render all candlesticks."""
        return f"🕯️ {len(self.candles)} candles rendered"
