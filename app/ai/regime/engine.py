from ta.trend import ADXIndicator
from ta.volatility import AverageTrueRange


class MarketRegimeEngine:

    def analyze(self, df):

        close = df["Close"]
        high = df["High"]
        low = df["Low"]

        adx = ADXIndicator(
            high=high,
            low=low,
            close=close
        ).adx().iloc[-1]

        atr = AverageTrueRange(
            high=high,
            low=low,
            close=close
        ).average_true_range().iloc[-1]

        price = close.iloc[-1]

        volatility = (atr / price) * 100

        if adx >= 30:
            regime = "TRENDING"
        elif adx >= 20:
            regime = "TRANSITION"
        else:
            regime = "RANGING"

        if volatility >= 3:
            volatility_state = "HIGH"
        elif volatility >= 1.5:
            volatility_state = "MEDIUM"
        else:
            volatility_state = "LOW"

        confidence = min(
            100,
            int(adx * 2)
        )

        return {

            "market_regime": regime,

            "trend_strength": round(float(adx), 2),

            "volatility": volatility_state,

            "volatility_percent": round(float(volatility), 2),

            "regime_confidence": confidence,

        }


market_regime_engine = MarketRegimeEngine()
