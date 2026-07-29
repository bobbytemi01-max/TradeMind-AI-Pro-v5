class RiskManager:

    def build(self, indicators, institutional):

        price = indicators["price"]
        atr = indicators.get("atr", price * 0.02)

        bullish = institutional["institutional_bias"] in (
            "BULLISH",
            "STRONG_BULLISH",
        )

        bearish = institutional["institutional_bias"] in (
            "BEARISH",
            "STRONG_BEARISH",
        )

        if bullish:

            entry = price
            stop = price - atr
            tp1 = price + atr
            tp2 = price + atr * 2
            tp3 = price + atr * 3

        elif bearish:

            entry = price
            stop = price + atr
            tp1 = price - atr
            tp2 = price - atr * 2
            tp3 = price - atr * 3

        else:

            entry = price
            stop = price
            tp1 = price
            tp2 = price
            tp3 = price

        risk = abs(entry - stop)
        reward = abs(tp3 - entry)

        rr = round(reward / risk, 2) if risk else 0

        return {
            "entry": round(entry, 2),
            "stop_loss": round(stop, 2),
            "tp1": round(tp1, 2),
            "tp2": round(tp2, 2),
            "tp3": round(tp3, 2),
            "risk_reward": rr,
        }


risk_manager = RiskManager()
