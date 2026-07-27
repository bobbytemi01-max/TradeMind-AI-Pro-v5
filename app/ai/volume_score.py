class VolumeScore:

    def calculate(self, data):

        score = 0
        reasons = []

        volume = data["volume"]
        avg = data["avg_volume"]

        ratio = volume / avg if avg else 1

        if ratio >= 2:
            score += 20
            reasons.append("Exceptional trading volume")

        elif ratio >= 1.5:
            score += 15
            reasons.append("Very strong volume")

        elif ratio >= 1.1:
            score += 10
            reasons.append("Above-average volume")

        elif ratio >= 0.9:
            score += 2
            reasons.append("Average volume")

        else:
            score -= 10
            reasons.append("Below-average volume")

        return {
            "score": score,
            "reasons": reasons,
        }


volume_score = VolumeScore()