class Engulfing:

    def detect(self, df):

        if len(df) < 2:
            return {
                "engulfing": False,
                "direction": "NONE",
            }

        prev = df.iloc[-2]
        last = df.iloc[-1]

        # Bullish Engulfing
        if (
            prev["Close"] < prev["Open"] and
            last["Close"] > last["Open"] and
            last["Open"] < prev["Close"] and
            last["Close"] > prev["Open"]
        ):
            return {
                "engulfing": True,
                "direction": "BULLISH",
            }

        # Bearish Engulfing
        if (
            prev["Close"] > prev["Open"] and
            last["Close"] < last["Open"] and
            last["Open"] > prev["Close"] and
            last["Close"] < prev["Open"]
        ):
            return {
                "engulfing": True,
                "direction": "BEARISH",
            }

        return {
            "engulfing": False,
            "direction": "NONE",
        }


engulfing = Engulfing()
