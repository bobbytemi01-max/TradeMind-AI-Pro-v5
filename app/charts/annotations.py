"""Chart annotations and labels."""

from __future__ import annotations

from typing import Dict, List, Optional


class Annotation:
    """Single chart annotation."""

    def __init__(self, text: str, x: float, y: float) -> None:
        self.text = text
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"'{self.text}' at ({self.x}, {self.y})"


class AnnotationManager:
    """Manage chart annotations."""

    def __init__(self) -> None:
        self.annotations: List[Annotation] = []

    def add_annotation(self, text: str, x: float, y: float) -> None:
        """Add an annotation."""
        self.annotations.append(Annotation(text, x, y))

    def render(self) -> str:
        """Render all annotations."""
        return f"📝 {len(self.annotations)} annotations"
