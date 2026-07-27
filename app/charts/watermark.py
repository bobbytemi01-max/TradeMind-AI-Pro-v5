"""Chart watermark utilities."""

from __future__ import annotations

from typing import Optional


class Watermark:
    """Chart watermark."""

    def __init__(self, text: str = "TradeMind AI") -> None:
        self.text = text
        self.opacity = 0.3
        self.position = "bottom_right"

    def set_opacity(self, opacity: float) -> None:
        """Set watermark opacity (0.0-1.0)."""
        self.opacity = max(0.0, min(1.0, opacity))

    def set_position(self, position: str) -> None:
        """Set watermark position."""
        valid_positions = ["bottom_right", "bottom_left", "top_right", "top_left", "center"]
        if position in valid_positions:
            self.position = position

    def render(self) -> str:
        """Render watermark."""
        return f"💧 Watermark: '{self.text}' at {self.position} (opacity: {self.opacity})"
