"""Simplified Ichimoku Cloud indicator."""

from __future__ import annotations

from typing import Sequence, Dict


def ichimoku(highs: Sequence[float], lows: Sequence[float], closes: Sequence[float], tenkan_period: int = 9, kijun_period: int = 26, senkou_b_period: int = 52) -> Dict[str, float]:
    """Return a simplified set of Ichimoku cloud values."""
    if not highs or not lows or not closes:
        return {}

    if len(highs) != len(lows) or len(lows) != len(closes):
        return {}

    if len(closes) < max(tenkan_period, kijun_period, senkou_b_period):
        return {}

    tenkan_sen = (max(highs[-tenkan_period:]) + min(lows[-tenkan_period:])) / 2
    kijun_sen = (max(highs[-kijun_period:]) + min(lows[-kijun_period:])) / 2
    senkou_span_a = (tenkan_sen + kijun_sen) / 2
    senkou_span_b = (max(highs[-senkou_b_period:]) + min(lows[-senkou_b_period:])) / 2

    return {
        "tenkan_sen": float(tenkan_sen),
        "kijun_sen": float(kijun_sen),
        "senkou_span_a": float(senkou_span_a),
        "senkou_span_b": float(senkou_span_b),
        "chikou_span": float(closes[-1]),
    }
