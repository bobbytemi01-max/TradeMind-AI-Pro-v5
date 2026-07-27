"""Trade level overlays for charts."""

from __future__ import annotations

from typing import Dict, List, Optional, Tuple


class TradeLevel:
    """Represent a single trade level."""

    def __init__(self, name: str, price: float, color: str = "#000000") -> None:
        self.name = name
        self.price = price
        self.color = color

    def __repr__(self) -> str:
        return f"{self.name}: ${self.price:.2f}"


class Overlay:
    """Trade level overlays for charts."""

    def __init__(self) -> None:
        self.levels: List[TradeLevel] = []

    def add_level(self, name: str, price: float, color: str = "#000000") -> None:
        """Add a trade level."""
        self.levels.append(TradeLevel(name, price, color))

    def set_entry(self, price: float) -> None:
        """Set entry level."""
        self.add_level("Entry", price, "#0000ff")

    def set_stop_loss(self, price: float) -> None:
        """Set stop-loss level."""
        self.add_level("Stop Loss", price, "#ff0000")

    def set_take_profit(self, price: float) -> None:
        """Set take-profit level."""
        self.add_level("Take Profit", price, "#00aa00")

    def apply(self) -> str:
        """Apply overlays to chart."""
        if not self.levels:
            return "no levels set"
        return " | ".join(str(level) for level in self.levels)
