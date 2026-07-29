class SignalFusion:

    def decide(
        self,
        institutional,
        candlestick,
        confidence,
    ):

        score = 0
        reasons = []

        score += institutional["institutional_score"]

        if institutional["institutional_score"]:
            reasons.append(
                f"Institutional Score {institutional['institutional_score']}"
            )

        score += candlestick["candlestick_score"]
        reasons.extend(
            candlestick.get("candlestick_reasons", [])
        )

        score += confidence["confidence_v2"] - 50

        if score >= 90:
            signal = "STRONG BUY"

        elif score >= 45:
            signal = "BUY"

        elif score <= -90:
            signal = "STRONG SELL"

        elif score <= -45:
            signal = "SELL"

        else:
            signal = "WAIT"

        return {
            "final_signal": signal,
            "fusion_score": score,
            "fusion_reasons": reasons,
        }


signal_fusion = SignalFusion()
