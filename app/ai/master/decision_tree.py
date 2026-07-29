class DecisionTree:

    def decide(
        self,
        context,
        structure,
        probability,
        regime,
        strategy,
    ):

        reasons = []

        if regime["market_regime"] == "RANGING":
            reasons.append("Ranging market detected")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        if strategy["strategy"] == "WAIT":
            reasons.append("Strategy Router recommends WAIT")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # Trend Filter
        if context["market_trend"] not in ("BULL", "STRONG_BULL"):
            reasons.append("Trend not bullish")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # Institutional Filter
        if structure["institutional_bias"] != "BULLISH":
            reasons.append("Institutional bias not bullish")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # Discount Zone
        if structure["premium_discount"] != "DISCOUNT":
            reasons.append("Price not in discount")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # CHoCH
        if not structure["choch"]:
            reasons.append("No CHoCH")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # FVG
        if not structure["fvg"]:
            reasons.append("No Fair Value Gap")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # Multi-Timeframe
        if context["multi_timeframe_strength"] == "WEAK":
            reasons.append("Weak multi-timeframe agreement")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        # Probability
        if probability["probability"] < 80:
            reasons.append("Probability below threshold")
            return {
                "decision": "WAIT",
                "decision_reasons": reasons,
            }

        reasons.append("All institutional conditions satisfied")

        return {
            "decision": "BUY",
            "decision_reasons": reasons,
        }


decision_tree = DecisionTree()
