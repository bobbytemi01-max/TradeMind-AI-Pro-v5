"""Chart layout management."""

from __future__ import annotations

from typing import Dict, List, Tuple


class Layout:
    """Manage chart layout and positioning."""

    def __init__(self, width: int = 1200, height: int = 600) -> None:
        self.width = width
        self.height = height
        self.panels: Dict[str, Tuple[int, int, int, int]] = {}

    def add_panel(self, name: str, x: int, y: int, w: int, h: int) -> None:
        """Add a panel to the layout."""
        self.panels[name] = (x, y, w, h)

    def get_main_chart_area(self) -> Tuple[int, int, int, int]:
        """Get the main chart area coordinates."""
        margin = 40
        return (margin, margin, self.width - 2 * margin, int(self.height * 0.7))

    def get_volume_area(self) -> Tuple[int, int, int, int]:
        """Get the volume panel area."""
        margin = 40
        x, y, w, h = self.get_main_chart_area()
        return (x, y + h + 10, w, int(self.height * 0.25))
