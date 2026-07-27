class MomentumScore:

    def calculate(self, data):

        score = 0
        reasons = []

        rsi = data["rsi"]

        if 50 <= rsi <= 65:
            score += 8
            reasons.append("Healthy RSI")

        elif rsi < 30:
            score += 12
            reasons.append("Oversold")

        elif rsi > 70:
            score -= 12
            reasons.append("Overbought")

        if data["macd"] > data["signal"]:
            score += 8
            reasons.append("Bullish MACD crossover")
        else:
            score -= 8
            reasons.append("Bearish MACD crossover")

        if data["histogram"] > 0:
            score += 4
            reasons.append("Positive MACD histogram")
        else:
            score -= 4
            reasons.append("Negative MACD histogram")

        return {
            "score": score,
            "reasons": reasons,
        }


momentum_score = MomentumScore()