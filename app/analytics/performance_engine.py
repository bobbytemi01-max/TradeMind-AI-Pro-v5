from collections import Counter


class PerformanceEngine:

    def analyze(self, trades):

        completed = [
            t for t in trades
            if t.get("result") in ("WIN", "LOSS")
        ]

        wins = [t for t in completed if t["result"] == "WIN"]
        losses = [t for t in completed if t["result"] == "LOSS"]

        assets = Counter(t["symbol"] for t in wins)
        sessions = Counter(t.get("session", "UNKNOWN") for t in wins)

        return {
            "total": len(completed),
            "wins": len(wins),
            "losses": len(losses),
            "win_rate": round(len(wins) / len(completed) * 100, 2) if completed else 0,
            "best_asset": assets.most_common(1)[0][0] if assets else "N/A",
            "best_session": sessions.most_common(1)[0][0] if sessions else "N/A",
        }


performance_engine = PerformanceEngine()
