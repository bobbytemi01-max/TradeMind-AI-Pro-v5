"""Indicator panels for charts."""

from __future__ import annotations

from typing import Dict, List, Optional


class Panel:
    """Chart panel for indicators."""

    def __init__(self, name: str, height: float = 0.25) -> None:
        self.name = name
        self.height = height
        self.indicators: List[str] = []

    def add_indicator(self, indicator: str) -> None:
        """Add indicator to panel."""
        self.indicators.append(indicator)

    def __repr__(self) -> str:
        return f"{self.name}: {', '.join(self.indicators)}"


class PanelManager:
    """Manage multiple indicator panels."""

    def __init__(self) -> None:
        self.panels: Dict[str, Panel] = {}

    def create_panel(self, name: str, height: float = 0.25) -> Panel:
        """Create a new panel."""
        panel = Panel(name, height)
        self.panels[name] = panel
        return panel

    def render(self) -> str:
        """Render all panels."""
        return f"📊 {len(self.panels)} panels: {', '.join(self.panels.keys())}"
