class ConfidenceEngine:

    def calculate(self, ai):

        confidence = 50

        confidence += ai.get("trend_score", 0) * 0.35
        confidence += ai.get("momentum_score", 0) * 0.20
        confidence += ai.get("volume_score", 0) * 0.10
        confidence += ai.get("structure_score", 0) * 0.15
        confidence += ai.get("support_score", 0) * 0.05
        confidence += ai.get("risk_score", 0) * 0.05
        confidence += ai.get("adx_score", 0) * 0.05
        confidence += ai.get("vwap_score", 0) * 0.05

        confidence = max(0, min(99, round(confidence)))

        return confidence


confidence_engine = ConfidenceEngine()
