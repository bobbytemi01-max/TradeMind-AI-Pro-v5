class CandlestickScorer:

    def score(self, data):

        score = 0
        reasons = []

        if data["engulfing"]:
            if data["direction"] == "BULLISH":
                score += 30
                reasons.append("Bullish Engulfing")
            elif data["direction"] == "BEARISH":
                score -= 30
                reasons.append("Bearish Engulfing")

        if data["hammer"]:
            score += 15
            reasons.append("Hammer")

        if data["shooting_star"]:
            score -= 15
            reasons.append("Shooting Star")

        if data["morning_star"]:
            score += 25
            reasons.append("Morning Star")

        if data["evening_star"]:
            score -= 25
            reasons.append("Evening Star")

        if data["three_white_soldiers"]:
            score += 35
            reasons.append("Three White Soldiers")

        if data["three_black_crows"]:
            score -= 35
            reasons.append("Three Black Crows")

        if data["doji"]:
            reasons.append("Doji (Indecision)")

        if score >= 40:
            bias = "STRONG_BULLISH"
        elif score >= 20:
            bias = "BULLISH"
        elif score <= -40:
            bias = "STRONG_BEARISH"
        elif score <= -20:
            bias = "BEARISH"
        else:
            bias = "NEUTRAL"

        return {
            "candlestick_score": score,
            "candlestick_bias": bias,
            "candlestick_reasons": reasons,
        }


candlestick_scorer = CandlestickScorer()
