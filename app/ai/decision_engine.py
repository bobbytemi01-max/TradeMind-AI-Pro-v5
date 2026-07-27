"""
TradeMind AI Pro v7
Decision Engine
"""

from app.ai.market_regime import market_regime
from app.ai.confidence_engine import confidence_engine


class DecisionEngine:
    """
    AI Decision Engine

    Converts the AI consensus score into
    BUY / SELL / WAIT decisions.
    """

    def decide(self, indicators, ai):

        score = ai.get("score", 50)
        confidence = confidence_engine.calculate(ai)

        regime = ai.get("market_regime", "⚪ Transition")
        bias = ai.get("market_bias", "NEUTRAL")

        price = indicators.get("price", 0)
        ema200 = indicators.get("ema200", 0)
        adx = indicators.get("adx", 0)
        vwap = indicators.get("vwap", price)

        recommendation = "🤝 WAIT"
        direction = "WAIT"
        trade_allowed = False
        strength = "NONE"

        reasons = []

        # =====================================
        # Safety Filters
        # =====================================

        if adx < 20:
            reasons.append("Weak trend (ADX)")
            return self._result(
                recommendation,
                direction,
                trade_allowed,
                strength,
                confidence,
                reasons,
            )

        if regime == "🟡 Range":
            reasons.append("Market is ranging")
            return self._result(
                recommendation,
                direction,
                trade_allowed,
                strength,
                confidence,
                reasons,
            )

        if price < ema200 and score >= 90:
            score = 80
            reasons.append("Price below EMA200")

        if price < vwap:
            score -= 5
            reasons.append("Price below VWAP")

        score = max(0, min(100, score))

        # =====================================
        # BUY
        # =====================================

        if (
            score >= 90
            and bias == "BULLISH"
            and price > ema200
        ):

            recommendation = "🔥 ELITE BUY"
            direction = "BUY"
            trade_allowed = True
            strength = "ELITE"

            reasons.append("Elite bullish setup")

        elif (
            score >= 75
            and bias == "BULLISH"
        ):

            recommendation = "🟢 BUY"
            direction = "BUY"
            trade_allowed = True
            strength = "STRONG"

            reasons.append("Bullish trend confirmed")

        # =====================================
        # SELL
        # =====================================

        elif (
            score <= 25
            and bias == "BEARISH"
        ):

            recommendation = "🚨 STRONG SELL"
            direction = "SELL"
            trade_allowed = True
            strength = "ELITE"

            reasons.append("Strong bearish continuation")

        elif (
            score <= 40
            and bias == "BEARISH"
        ):

            recommendation = "🔴 SELL"
            direction = "SELL"
            trade_allowed = True
            strength = "STRONG"

            reasons.append("Bearish trend confirmed")

        else:

            recommendation = "🤝 WAIT"

            direction = "WAIT"

            trade_allowed = False

            strength = "NONE"

            reasons.append("No high probability setup")

        return self._result(
            recommendation,
            direction,
            trade_allowed,
            strength,
            confidence,
            reasons,
        )

    def _result(
        self,
        recommendation,
        direction,
        trade_allowed,
        strength,
        confidence,
        reasons,
    ):

        if confidence >= 90:
            risk = "🟢 Low"
        elif confidence >= 70:
            risk = "🟡 Medium"
        else:
            risk = "🔴 High"

        return {

            "recommendation": recommendation,

            "direction": direction,

            "trade_allowed": trade_allowed,

            "strength": strength,

            "risk_level": risk,

            "reason": "\n".join(reasons),

            "confidence": confidence,

        }


decision_engine = DecisionEngine()
