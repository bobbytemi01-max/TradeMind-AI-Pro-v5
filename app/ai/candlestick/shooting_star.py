class ShootingStar:

    def detect(self, df):

        if len(df) < 1:
            return {
                "shooting_star": bool(False),
            }

        c = df.iloc[-1]

        body = abs(c["Close"] - c["Open"])
        upper = c["High"] - max(c["Open"], c["Close"])
        lower = min(c["Open"], c["Close"]) - c["Low"]

        return {
            "shooting_star": bool(upper > body * 2 and lower < body)
        }


shooting_star = ShootingStar()
