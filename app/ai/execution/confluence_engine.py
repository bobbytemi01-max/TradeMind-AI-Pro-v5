class ConfluenceEngine:

    def calculate(
        self,
        institutional,
        candlestick,
        confidence,
        session,
    ):

        score = 0
        checks = []

        # Institutional
        score += institutional["institutional_score"]

        if institutional["institutional_score"] >= 35:
            checks.append("Institutional")

        # Candlestick
        score += max(0, candlestick["candlestick_score"])

        if candlestick["candlestick_score"] > 0:
            checks.append("Candlestick")

        # Confidence
        score += confidence["confidence_v2"] - 50

        if confidence["confidence_v2"] >= 60:
            checks.append("Confidence")

        # Session
        score += (session["session_score"] - 50) // 2

        if session["session_score"] >= 80:
            checks.append("Session")

        score = max(0, min(100, score))

        return {
            "confluence_score": score,
            "confluence_checks": checks,
        }


confluence_engine = ConfluenceEngine()
