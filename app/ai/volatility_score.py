class VolatilityScore:

    def calculate(self, data):

        score = 0
        reasons = []

        atr = data["atr"]
        price = data["price"]

        volatility = (atr / price) * 100

        if 1 <= volatility <= 4:
            score += 10
            reasons.append("Healthy volatility")

        elif volatility < 1:
            score -= 5
            reasons.append("Low volatility")

        else:
            score -= 5
            reasons.append("High volatility")

        return {
            "score": score,
            "reasons": reasons,
        }


volatility_score = VolatilityScore()