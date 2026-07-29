class SMCEngine:

    def detect_bos(self, highs, closes):

        if len(highs) < 3:
            return False

        return closes[-1] > max(highs[-3:-1])

    def detect_choch(self, lows, closes):

        if len(lows) < 3:
            return False

        return closes[-1] < min(lows[-3:-1])

    def detect_fvg(self, highs, lows):

        if len(highs) < 3:
            return False

        return lows[-1] > highs[-3]

    def detect_order_block(self, opens, closes, highs, lows):

        if len(opens) < 2:
            return "None"

        # Bullish Order Block
        if (
            closes[-2] < opens[-2]
            and closes[-1] > highs[-2]
        ):
            return "Bullish"

        # Bearish Order Block
        if (
            closes[-2] > opens[-2]
            and closes[-1] < lows[-2]
        ):
            return "Bearish"

        return "None"

    def analyze(self, df):

        highs = df["High"].tolist()
        lows = df["Low"].tolist()
        opens = df["Open"].tolist()
        closes = df["Close"].tolist()

        return {
            "bos": self.detect_bos(highs, closes),
            "choch": self.detect_choch(lows, closes),
            "fvg": self.detect_fvg(highs, lows),
            "order_block": self.detect_order_block(
                opens,
                closes,
                highs,
                lows,
            ),
        }


smc_engine = SMCEngine()
