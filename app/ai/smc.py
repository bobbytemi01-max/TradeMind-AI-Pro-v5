class SMCEngine:

    def analyze(self, data):

        high = data["high"]
        low = data["low"]
        close = data["price"]
        ema20 = data["ema20"]
        ema50 = data["ema50"]

        bos = close > high * 0.995
        choch = close < ema20 and ema20 > ema50

        order_block = "Bullish" if close > ema20 else "Bearish"

        fvg = abs(high - low) > (close * 0.01)

        liquidity = (
            "Buy-side"
            if close > ema20
            else "Sell-side"
        )

        return {
            "bos": bos,
            "choch": choch,
            "order_block": order_block,
            "fair_value_gap": fvg,
            "liquidity": liquidity,
        }


smc = SMCEngine()
