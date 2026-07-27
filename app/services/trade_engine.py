"""
TradeMind AI Pro
Professional Trade Engine v2
"""


class TradeEngine:

    def build(self, indicators, ai, decision):

        price = indicators["price"]
        atr = indicators["atr"]
        adx = indicators.get("adx", 20)

        recommendation = decision["recommendation"]
        direction = decision["direction"]
        trade_allowed = decision["trade_allowed"]

        # ======================================
        # Dynamic ATR Multiplier
        # ======================================

        if adx >= 35:
            atr_multiplier = 2.0
            position_quality = "A+"

        elif adx >= 25:
            atr_multiplier = 1.5
            position_quality = "A"

        else:
            atr_multiplier = 1.2
            position_quality = "B"

        # ======================================
        # No Trade
        # ======================================

        if not trade_allowed:

            return {

                "direction": "🤝 WAIT",

                "recommendation": recommendation,

                "entry": round(price, 2),

                "stop_loss": round(price, 2),

                "tp1": round(price, 2),

                "tp2": round(price, 2),

                "tp3": round(price, 2),

                "risk_reward": 0.0,

                "risk_level": decision["risk_level"],

                "trade_allowed": False,

                "position_quality": "N/A",

                "expected_reward": 0,

                "expected_risk": 0,

            }

        # ======================================
        # BUY
        # ======================================

        if direction == "BUY":

            entry = price

            stop_loss = price - (atr_multiplier * atr)

            risk = entry - stop_loss

            tp1 = entry + (1.5 * risk)

            tp2 = entry + (2.5 * risk)

            tp3 = entry + (4.0 * risk)

        # ======================================
        # SELL
        # ======================================

        else:

            entry = price

            stop_loss = price + (atr_multiplier * atr)

            risk = stop_loss - entry

            tp1 = entry - (1.5 * risk)

            tp2 = entry - (2.5 * risk)

            tp3 = entry - (4.0 * risk)

        reward = abs(tp2 - entry)

        risk_reward = round(reward / risk, 2) if risk > 0 else 0

        return {

            "direction": direction,

            "recommendation": recommendation,

            "entry": round(entry, 2),

            "stop_loss": round(stop_loss, 2),

            "tp1": round(tp1, 2),

            "tp2": round(tp2, 2),

            "tp3": round(tp3, 2),

            "risk_reward": risk_reward,

            "risk_level": decision["risk_level"],

            "trade_allowed": trade_allowed,

            "position_quality": position_quality,

            "expected_reward": round(reward, 2),

            "expected_risk": round(risk, 2),

        }


trade_engine = TradeEngine()
