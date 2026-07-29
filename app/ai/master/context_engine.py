class ContextEngine:

    def analyze(
        self,
        indicators,
        institutional,
        multi,
    ):

        price = indicators["price"]
        ema20 = indicators["ema20"]
        ema50 = indicators["ema50"]
        ema200 = indicators["ema200"]
        adx = indicators["adx"]

        # Trend
        if price > ema20 > ema50 > ema200:
            trend = "STRONG_BULL"

        elif price < ema20 < ema50 < ema200:
            trend = "STRONG_BEAR"

        elif price > ema200:
            trend = "BULL"

        elif price < ema200:
            trend = "BEAR"

        else:
            trend = "RANGE"

        # Strength
        if adx >= 30:
            strength = "HIGH"
        elif adx >= 20:
            strength = "MEDIUM"
        else:
            strength = "LOW"

        agreement = multi["agreement"]

        if agreement >= 4:
            mtf = "FULL"

        elif agreement >= 3:
            mtf = "STRONG"

        elif agreement >= 2:
            mtf = "MEDIUM"

        else:
            mtf = "WEAK"

        return {

            "market_trend": trend,

            "trend_strength": strength,

            "multi_timeframe_strength": mtf,

            "institutional_bias":
                institutional["institutional_bias"],

        }


context_engine = ContextEngine()
