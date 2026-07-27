"""
TradeMind AI Pro v7
Market Regime Engine
"""


class MarketRegimeEngine:
    """
    Detects the overall market regime.
    """

    def detect(self, indicators):

        ema20 = indicators.get("ema20", 0)
        ema50 = indicators.get("ema50", 0)
        ema200 = indicators.get("ema200", 0)

        price = indicators.get("price", 0)
        adx = indicators.get("adx", 20)

        # Strong Bull Trend
        if (
            price > ema20
            and ema20 > ema50 > ema200
            and adx >= 25
        ):
            return {
                "market_regime": "🟢 Trending Bull",
                "bias": "BULLISH",
            }

        # Strong Bear Trend
        if (
            price < ema20
            and ema20 < ema50 < ema200
            and adx >= 25
        ):
            return {
                "market_regime": "🔴 Trending Bear",
                "bias": "BEARISH",
            }

        # Sideways Market
        if adx < 20:
            return {
                "market_regime": "🟡 Range",
                "bias": "NEUTRAL",
            }

        # Transition
        return {
            "market_regime": "⚪ Transition",
            "bias": "NEUTRAL",
        }


market_regime = MarketRegimeEngine()