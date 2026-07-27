"""Chart theming and styling."""

from __future__ import annotations

from typing import Dict, Tuple


class Theme:
    """Chart color and style theme."""

    def __init__(self, name: str = "default") -> None:
        self.name = name
        self.colors = self._get_theme_colors(name)

    def _get_theme_colors(self, name: str) -> Dict[str, str]:
        """Get color palette for theme."""
        themes = {
            "default": {
                "background": "#ffffff",
                "grid": "#eeeeee",
                "candle_up": "#00aa00",
                "candle_down": "#ff0000",
                "volume": "#0088ff",
                "text": "#000000",
            },
            "dark": {
                "background": "#1e1e1e",
                "grid": "#333333",
                "candle_up": "#00ff00",
                "candle_down": "#ff4444",
                "volume": "#0099ff",
                "text": "#ffffff",
            },
        }
        return themes.get(name, themes["default"])

    def get_color(self, key: str) -> str:
        """Get color by key."""
        return self.colors.get(key, "#000000")
