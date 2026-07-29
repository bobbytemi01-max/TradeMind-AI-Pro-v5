class RegimeScorer:

    def score(self, regime):

        score = 50
        reasons = []

        if regime["market_regime"] == "TRENDING":
            score += 25
            reasons.append("Trending Market")

        elif regime["market_regime"] == "TRANSITION":
            score += 10
            reasons.append("Transition Market")

        else:
            score -= 15
            reasons.append("Ranging Market")

        if regime["volatility"] == "HIGH":
            score += 10
            reasons.append("High Volatility")

        elif regime["volatility"] == "LOW":
            score -= 10
            reasons.append("Low Volatility")

        score = max(0, min(100, score))

        return {
            "regime_score": score,
            "regime_reasons": reasons
        }


regime_scorer = RegimeScorer()
