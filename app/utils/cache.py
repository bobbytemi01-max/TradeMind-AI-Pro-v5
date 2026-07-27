"""Simple in-memory cache utilities."""

from __future__ import annotations

from typing import Any, Dict, Optional, TypeVar

T = TypeVar("T")


class SimpleCache:
    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def get(self, key: str, default: Optional[T] = None) -> Optional[T]:
        return self._store.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def delete(self, key: str) -> None:
        self._store.pop(key, None)

    def clear(self) -> None:
        self._store.clear()
