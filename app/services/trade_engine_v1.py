"""
TradeMind AI Pro Trade Engine
"""


class TradeEngine:

    def build(self, indicators, ai, decision):

        price = indicators["price"]
        atr = indicators["atr"]

        recommendation = decision["recommendation"]
        direction = decision["direction"]
        trade_allowed = decision["trade_allowed"]

        # ----------------------------------
        # No Trade
        # ----------------------------------

        if not trade_allowed:

            return {

                "direction": "🤝 WAIT",

                "entry": round(price, 2),

                "stop_loss": round(price, 2),

                "tp1": round(price, 2),

                "tp2": round(price, 2),

                "tp3": round(price, 2),

                "risk_reward": 0.0,

                "risk_level": decision["risk_level"]

            }

        # ----------------------------------
        # BUY
        # ----------------------------------

        if direction == "BUY":

            entry = price

            stop_loss = price - (1.5 * atr)

            risk = entry - stop_loss

            tp1 = entry + (1.5 * risk)

            tp2 = entry + (2.5 * risk)

            tp3 = entry + (4.0 * risk)

        # ----------------------------------
        # SELL
        # ----------------------------------

        else:

            entry = price

            stop_loss = price + (1.5 * atr)

            risk = stop_loss - entry

            tp1 = entry - (1.5 * risk)

            tp2 = entry - (2.5 * risk)

            tp3 = entry - (4.0 * risk)

        # ----------------------------------
        # Risk Reward
        # ----------------------------------

        reward = abs(tp2 - entry)

        risk_reward = round(reward / risk, 2) if risk > 0 else 0

        # ----------------------------------
        # Return
        # ----------------------------------

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

            "trade_allowed": trade_allowed

        }


trade_engine = TradeEngine()