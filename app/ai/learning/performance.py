import json
from pathlib import Path


class PerformanceEngine:

    FILE = Path("data/trades.json")

    def summary(self):

        if not self.FILE.exists():
            return {
                "total": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0,
            }

        trades = json.loads(self.FILE.read_text())

        wins = sum(1 for t in trades if t.get("result") == "WIN")
        losses = sum(1 for t in trades if t.get("result") == "LOSS")

        total = wins + losses

        if total == 0:
            win_rate = 0
        else:
            win_rate = round((wins / total) * 100, 2)

        return {
            "total": total,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
        }


performance_engine = PerformanceEngine()
