"""Formatting helpers for TradeMindAI."""

from __future__ import annotations

from typing import Any


def format_currency(value: float) -> str:
    return f"${value:,.2f}"


def format_percent(value: float) -> str:
    return f"{value:.2f}%"


def format_number(value: Any) -> str:
    return str(value)
