class RiskScore:

    def calculate(self, data):

        score = 0
        reasons = []

        atr = data["atr"]
        price = data["price"]

        risk = (atr / price) * 100

        if risk < 2:
            score += 10
            reasons.append("Low market risk")

        elif risk < 4:
            score += 5
            reasons.append("Moderate risk")

        else:
            score -= 10
            reasons.append("High market risk")

        return {
            "score": score,
            "reasons": reasons,
        }


risk_score = RiskScore()