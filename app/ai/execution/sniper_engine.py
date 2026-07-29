class SniperEngine:

    def evaluate(self, probability):

        p = probability["probability"]

        if p >= 90:
            status = "🔥 EXECUTE TRADE"

        elif p >= 75:
            status = "🟢 VALID SETUP"

        elif p >= 60:
            status = "🟡 WATCHLIST"

        else:
            status = "🔴 NO TRADE"

        return {
            "execution_status": status
        }


sniper_engine = SniperEngine()
