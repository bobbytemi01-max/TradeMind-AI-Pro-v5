class ConfidenceEngine:

    def calculate(
        self,
        institutional,
        candlestick,
        multi,
        regime,
        strategy,
        learning,
    ):

        confidence = 50

        if institutional["institutional_bias"] == "STRONG_BULLISH":
            confidence += 20
        elif institutional["institutional_bias"] == "BULLISH":
            confidence += 10
        elif institutional["institutional_bias"] == "STRONG_BEARISH":
            confidence += 20
        elif institutional["institutional_bias"] == "BEARISH":
            confidence += 10

        confidence += min(
            abs(candlestick["candlestick_score"]) // 5,
            15,
        )

        confidence += multi["agreement"] * 5

        if regime["market_regime"] == "TRENDING":
            confidence += 10
        elif regime["market_regime"] == "TRANSITION":
            confidence += 5
        else:
            confidence -= 5

        if strategy["strategy"] == "TREND_FOLLOWING":
            confidence += 5
        elif strategy["strategy"] == "BREAKOUT":
            confidence += 3
        elif strategy["strategy"] == "MEAN_REVERSION":
            confidence += 2

        if learning["learning_ready"]:
            confidence += min(
                learning["overall_win_rate"] / 20,
                5,
            )

        confidence = max(0, min(100, confidence))

        if confidence >= 90:
            grade = "A+"
        elif confidence >= 80:
            grade = "A"
        elif confidence >= 70:
            grade = "B+"
        elif confidence >= 60:
            grade = "B"
        elif confidence >= 50:
            grade = "C"
        else:
            grade = "D"

        return {
            "confidence_v2": confidence,
            "trade_grade_v2": grade,
        }


confidence_engine = ConfidenceEngine()
