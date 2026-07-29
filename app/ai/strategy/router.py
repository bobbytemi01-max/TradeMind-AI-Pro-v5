class StrategyRouter:

    def select(self, regime):

        market = regime["market_regime"]
        volatility = regime["volatility"]

        if market == "TRENDING":
            strategy = "TREND_FOLLOWING"

        elif market == "RANGING":
            strategy = "MEAN_REVERSION"

        elif market == "TRANSITION":
            strategy = "BREAKOUT"

        else:
            strategy = "WAIT"

        if volatility == "HIGH":
            risk = "REDUCED"

        elif volatility == "LOW":
            risk = "NORMAL"

        else:
            risk = "STANDARD"

        return {
            "strategy": strategy,
            "risk_profile": risk
        }


strategy_router = StrategyRouter()
