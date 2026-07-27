class StructureScore:

    def calculate(self, data):

        score = 0
        reasons = []

        if data["price"] > data["ema20"]:
            score += 10
            reasons.append("Price above EMA20")

        if data["volume"] >= data["avg_volume"]:
            score += 15
            reasons.append("Strong volume")
        else:
            reasons.append("Below average volume")

        return {
            "score": score,
            "reasons": reasons,
        }


structure_score = StructureScore()