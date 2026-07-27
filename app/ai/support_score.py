class SupportScore:

    def calculate(self, data):

        score = 0
        reasons = []

        price = data["price"]
        support = data["support"]
        resistance = data["resistance"]

        support_distance = abs(price - support)
        resistance_distance = abs(resistance - price)

        if support_distance < resistance_distance:
            score += 10
            reasons.append("Price closer to support")

        else:
            score -= 10
            reasons.append("Price closer to resistance")

        return {
            "score": score,
            "reasons": reasons,
        }


support_score = SupportScore()