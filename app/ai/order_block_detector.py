class OrderBlockDetector:

    def detect(self, df):

        if len(df) < 4:
            return {
                "order_block": False,
                "direction": "NONE",
                "high": None,
                "low": None,
            }

        last = df.iloc[-1]
        prev = df.iloc[-2]

        # Bullish Order Block
        if (
            prev["Close"] < prev["Open"]
            and last["Close"] > prev["High"]
        ):
            return {
                "order_block": True,
                "direction": "BULLISH",
                "high": float(prev["High"]),
                "low": float(prev["Low"]),
            }

        # Bearish Order Block
        if (
            prev["Close"] > prev["Open"]
            and last["Close"] < prev["Low"]
        ):
            return {
                "order_block": True,
                "direction": "BEARISH",
                "high": float(prev["High"]),
                "low": float(prev["Low"]),
            }

        return {
            "order_block": False,
            "direction": "NONE",
            "high": None,
            "low": None,
        }


order_block_detector = OrderBlockDetector()
