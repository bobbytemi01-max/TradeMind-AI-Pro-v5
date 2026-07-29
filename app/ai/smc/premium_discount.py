class PremiumDiscount:

    def analyze(self, df):

        high = float(df["High"].tail(100).max())
        low = float(df["Low"].tail(100).min())
        close = float(df["Close"].iloc[-1])

        equilibrium = (high + low) / 2

        if close > equilibrium:
            zone = "PREMIUM"
        elif close < equilibrium:
            zone = "DISCOUNT"
        else:
            zone = "EQUILIBRIUM"

        return {
            "premium_discount": zone,
            "equilibrium": round(equilibrium, 2),
        }


premium_discount = PremiumDiscount()
