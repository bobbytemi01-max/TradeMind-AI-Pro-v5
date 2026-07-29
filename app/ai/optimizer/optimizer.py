from collections import Counter


class StrategyOptimizer:

    def optimize(self, trades):

        completed = [
            t for t in trades
            if t.get("result") in ("WIN", "LOSS")
        ]

        if not completed:
            return {
                "completed": 0,
                "best_asset": None,
                "recommendation": "Not enough completed trades."
            }

        wins = [t for t in completed if t["result"] == "WIN"]

        assets = Counter(
            t["symbol"]
            for t in wins
        )

        best_asset = None

        if assets:
            best_asset = assets.most_common(1)[0][0]

        return {
            "completed": len(completed),
            "best_asset": best_asset,
            "recommendation":
                "Continue trading to improve AI learning."
        }


strategy_optimizer = StrategyOptimizer()
