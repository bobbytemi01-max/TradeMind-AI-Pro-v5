from app.ai.swing_detector import swing_detector


class LiquidityDetector:

    def detect(self, df):

        highs = swing_detector.highs(df)
        lows = swing_detector.lows(df)

        if not highs or not lows:
            return {
                "liquidity_sweep": False,
                "side": "NONE",
            }

        last_close = df["Close"].iloc[-1]
        last_high = df["High"].iloc[-1]
        last_low = df["Low"].iloc[-1]

        swing_high = highs[-1][1]
        swing_low = lows[-1][1]

        # Buy-side liquidity sweep
        if last_high > swing_high and last_close < swing_high:
            return {
                "liquidity_sweep": True,
                "side": "BUY_SIDE",
            }

        # Sell-side liquidity sweep
        if last_low < swing_low and last_close > swing_low:
            return {
                "liquidity_sweep": True,
                "side": "SELL_SIDE",
            }

        return {
            "liquidity_sweep": False,
            "side": "NONE",
        }


liquidity_detector = LiquidityDetector()
