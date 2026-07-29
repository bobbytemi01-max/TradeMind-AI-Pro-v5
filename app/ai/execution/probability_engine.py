class ProbabilityEngine:

    def calculate(self, confluence):

        score = confluence["confluence_score"]

        probability = min(99, max(1, score + 10))

        if probability >= 90:
            rating = "ELITE"

        elif probability >= 80:
            rating = "HIGH"

        elif probability >= 65:
            rating = "GOOD"

        elif probability >= 50:
            rating = "AVERAGE"

        else:
            rating = "LOW"

        return {
            "probability": probability,
            "probability_rating": rating,
        }


probability_engine = ProbabilityEngine()
