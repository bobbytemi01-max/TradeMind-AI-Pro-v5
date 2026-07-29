class ThreeWhiteSoldiers:

    def detect(self, df):

        if len(df) < 3:
            return {"three_white_soldiers": bool(False)}

        c1 = df.iloc[-3]
        c2 = df.iloc[-2]
        c3 = df.iloc[-1]

        result = (
            c1["Close"] > c1["Open"] and
            c2["Close"] > c2["Open"] and
            c3["Close"] > c3["Open"] and
            c2["Close"] > c1["Close"] and
            c3["Close"] > c2["Close"]
        )

        return {
            "three_white_soldiers": bool(result)
        }


three_white_soldiers = ThreeWhiteSoldiers()
