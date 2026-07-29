class BinaryEngine:

    def decide(self, data):

        score = 0
        reasons = []

        # Trend
        if data["ema20"] > data["ema50"] > data["ema200"]:
            score += 20
            reasons.append("Bullish EMA Alignment")
        elif data["ema20"] < data["ema50"] < data["ema200"]:
            score -= 20
            reasons.append("Bearish EMA Alignment")

        # RSI
        rsi = data["rsi"]

        if 55 <= rsi <= 70:
            score += 15
            reasons.append("Bullish RSI")

        elif 30 <= rsi <= 45:
            score -= 15
            reasons.append("Bearish RSI")

        # ADX
        if data["adx"] >= 25:
            score += 15
            reasons.append("Strong Trend")

        # MACD
        if data["macd"] > data["macd_signal"]:
            score += 15
            reasons.append("Bullish MACD")
        else:
            score -= 15
            reasons.append("Bearish MACD")

        # VWAP
        if data["price"] > data["vwap"]:
            score += 10
            reasons.append("Above VWAP")
        else:
            score -= 10
            reasons.append("Below VWAP")

        # Volume
        if data["volume"] > data["volume_sma"]:
            score += 10
            reasons.append("Strong Volume")

        # Decision
        if score >= 45:
            direction = "CALL"

        elif score <= -45:
            direction = "PUT"

        else:
            direction = "WAIT"

        confidence = min(99, max(0, 50 + score))

        return {
            "binary_direction": direction,
            "binary_score": score,
            "binary_confidence": confidence,
            "binary_reasons": reasons,
        }


binary_engine = BinaryEngine()
