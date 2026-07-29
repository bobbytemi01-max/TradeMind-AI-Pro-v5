class Hammer:

    def detect(self, df):

        if len(df) < 1:
            return {
                "hammer": bool(False),
            }

        c = df.iloc[-1]

        body = abs(c["Close"] - c["Open"])
        lower = min(c["Open"], c["Close"]) - c["Low"]
        upper = c["High"] - max(c["Open"], c["Close"])

        return {
            "hammer": bool(lower > body * 2 and upper < body)
        }


hammer = Hammer()
