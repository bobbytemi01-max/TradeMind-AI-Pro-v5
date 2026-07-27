from app.ai.trend_score import trend_score
from app.ai.momentum_score import momentum_score
from app.ai.volume_score import volume_score
from app.ai.volatility_score import volatility_score
from app.ai.structure_score import structure_score
from app.ai.support_score import support_score
from app.ai.risk_score import risk_score


class ConsensusEngine:

    def calculate(self, data):

        # ==========================================
        # Individual AI Scores
        # ==========================================

        trend = trend_score.calculate(data)
        momentum = momentum_score.calculate(data)
        volume = volume_score.calculate(data)
        volatility = volatility_score.calculate(data)
        structure = structure_score.calculate(data)
        support = support_score.calculate(data)
        risk = risk_score.calculate(data)

        trend_points = trend["score"]
        momentum_points = momentum["score"]
        volume_points = volume["score"]
        volatility_points = volatility["score"]
        structure_points = structure["score"]
        support_points = support["score"]
        risk_points = risk["score"]

        reasons = []

        for section in (
            trend,
            momentum,
            volume,
            volatility,
            structure,
            support,
            risk,
        ):
            reasons.extend(section["reasons"])

        # ==========================================
        # Base Score
        # ==========================================

        score = 50

        score += trend_points
        score += momentum_points
        score += volume_points
        score += volatility_points
        score += structure_points
        score += support_points
        score += risk_points

        # ==========================================
        # ADX Score
        # ==========================================

        adx_score = 0

        adx = data.get("adx", 0)

        if adx >= 40:
            adx_score = 15
            reasons.append("Very strong trend (ADX)")

        elif adx >= 25:
            adx_score = 10
            reasons.append("Strong trend (ADX)")

        elif adx >= 20:
            adx_score = 5
            reasons.append("Developing trend (ADX)")

        else:
            adx_score = -10
            reasons.append("Weak trend (Low ADX)")

        score += adx_score

        # ==========================================
        # VWAP Score
        # ==========================================

        vwap_score = 0

        if "vwap" in data:

            if data["price"] > data["vwap"]:
                vwap_score = 10
                reasons.append("Price above VWAP")

            else:
                vwap_score = -10
                reasons.append("Price below VWAP")

        score += vwap_score

        # ==========================================
        # Normalize Score
        # ==========================================

        score = max(0, min(100, score))

        # ==========================================
        # Market Regime
        # ==========================================

        ema20 = data["ema20"]
        ema50 = data["ema50"]
        ema200 = data["ema200"]

        if ema20 > ema50 > ema200:
            regime = "🟢 Trending Bull"

        elif ema20 < ema50 < ema200:
            regime = "🔴 Trending Bear"

        elif adx < 20:
            regime = "🟡 Range"

        else:
            regime = "⚪ Transition"

        # ==========================================
        # Smart Conflict Detection
        # ==========================================

        if (
            trend_points <= -20
            and momentum_points >= 15
            and adx < 20
        ):

            recommendation = "🤝 WAIT"
            reasons.append(
                "Bearish trend but bullish momentum in weak market"
            )

        elif (
            trend_points >= 20
            and momentum_points <= 0
            and adx < 20
        ):

            recommendation = "🤝 WAIT"
            reasons.append(
                "Bullish trend but weak momentum in weak market"
            )

        elif score >= 90:
            recommendation = "🔥 ELITE BUY"

        elif score >= 80:
            recommendation = "🟢 BUY"

        elif score >= 65:
            recommendation = "🟢 WATCH BUY"

        elif score >= 45:
            recommendation = "🤝 WAIT"

        elif score >= 25:
            recommendation = "🔴 SELL"

        else:
            recommendation = "🚨 STRONG SELL"

        # ==========================================
        # EMA200 Trend Filter
        # ==========================================

        if (
            recommendation in ["🔥 ELITE BUY", "🟢 BUY"]
            and data["price"] < ema200
        ):

            recommendation = "🤝 WAIT"
            reasons.append("Price below EMA200")

        if (
            recommendation in ["🔴 SELL", "🚨 STRONG SELL"]
            and data["price"] > ema200
        ):

            recommendation = "🤝 WAIT"
            reasons.append("Price above EMA200")

        # ==========================================
        # Trade Grade
        # ==========================================

        if score >= 95:
            grade = "A+"

        elif score >= 90:
            grade = "A"

        elif score >= 80:
            grade = "B+"

        elif score >= 70:
            grade = "B"

        elif score >= 60:
            grade = "C"

        elif score >= 50:
            grade = "D"

        else:
            grade = "F"

        # ==========================================
        # Dynamic Confidence
        # ==========================================

        confidence = score

        if adx >= 25:
            confidence += 5

        if volume_points > 0:
            confidence += 3

        if abs(momentum_points) >= 15:
            confidence += 2

        confidence = max(5, min(99, int(confidence)))

        # ==========================================
        # Return Result
        # ==========================================

        return {

            "score": score,

            "confidence": confidence,

            "recommendation": recommendation,

            "market_regime": regime,

            "trade_grade": grade,

            "score_breakdown": {

                "trend": trend_points,

                "momentum": momentum_points,

                "volume": volume_points,

                "volatility": volatility_points,

                "structure": structure_points,

                "support": support_points,

                "risk": risk_points,

                "adx": adx_score,

                "vwap": vwap_score,

            },

            "trend_score": trend_points,

            "momentum_score": momentum_points,

            "volume_score": volume_points,

            "volatility_score": volatility_points,

            "structure_score": structure_points,

            "support_score": support_points,

            "risk_score": risk_points,

            "adx_score": adx_score,

            "vwap_score": vwap_score,

            "reasons": reasons,

        }


consensus = ConsensusEngine()