class MorningStar:

    def detect(self, df):

        if len(df) < 3:
            return {
                "morning_star": bool(False),
            }

        c1 = df.iloc[-3]
        c2 = df.iloc[-2]
        c3 = df.iloc[-1]

        result = (
            c1["Close"] < c1["Open"] and
            abs(c2["Close"] - c2["Open"]) < abs(c1["Close"] - c1["Open"]) * 0.5 and
            c3["Close"] > c3["Open"] and
            c3["Close"] > ((c1["Open"] + c1["Close"]) / 2)
        )

        return {
            "morning_star": bool(result)
        }


morning_star = MorningStar()
