import json
from pathlib import Path


class StrategyOptimizer:

    FILE = Path("data/trades.json")

    def optimize(self):

        if not self.FILE.exists():
            return {
                "recommendation": "No trade history.",
                "win_rate": 0,
            }

        trades = json.loads(self.FILE.read_text())

        completed = [
            t for t in trades
            if t.get("result") in ["WIN", "LOSS"]
        ]

        if not completed:
            return {
                "recommendation": "Waiting for completed trades.",
                "win_rate": 0,
            }

        wins = sum(
            1 for t in completed
            if t["result"] == "WIN"
        )

        win_rate = round(
            wins / len(completed) * 100,
            2,
        )

        if win_rate >= 75:
            recommendation = "Increase position size."

        elif win_rate >= 60:
            recommendation = "Current strategy is healthy."

        elif win_rate >= 45:
            recommendation = "Reduce risk and wait for stronger confirmations."

        else:
            recommendation = "Retrain strategy. Too many losing trades."

        return {

            "completed_trades": len(completed),

            "win_rate": win_rate,

            "recommendation": recommendation,

        }


strategy_optimizer = StrategyOptimizer()
