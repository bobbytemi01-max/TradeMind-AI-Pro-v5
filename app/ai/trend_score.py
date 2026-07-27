class TrendScore:

    def calculate(self, data):

        score = 0
        reasons = []

        ema20 = data["ema20"]
        ema50 = data["ema50"]
        ema200 = data["ema200"]
        price = data["price"]

        if ema20 > ema50 > ema200:
            score += 20
            reasons.append("Strong bullish EMA alignment")

        elif ema20 > ema50:
            score += 12
            reasons.append("Bullish EMA alignment")

        elif ema20 < ema50 < ema200:
            score -= 20
            reasons.append("Strong bearish EMA alignment")

        else:
            reasons.append("Mixed EMA alignment")

        if price > ema200:
            score += 10
            reasons.append("Price above EMA200")
        else:
            score -= 10
            reasons.append("Price below EMA200")

        return {
            "score": score,
            "reasons": reasons,
        }


trend_score = TrendScore()