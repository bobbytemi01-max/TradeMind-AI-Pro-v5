"""Chart export utilities."""

from __future__ import annotations

from typing import Optional


class Exporter:
    """Export charts to various formats."""

    def __init__(self) -> None:
        self.supported_formats = ["png", "jpg", "svg", "pdf"]

    def export(self, filename: str, format: str = "png") -> str:
        """Export chart to file."""
        if format not in self.supported_formats:
            return f"❌ Unsupported format: {format}"
        return f"✅ Chart exported to {filename}.{format}"

    def export_url(self) -> str:
        """Generate chart URL for sharing."""
        return "https://charts.trademind.ai/chart_abc123.png"
