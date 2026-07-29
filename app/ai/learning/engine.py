from app.ai.learning.trade_logger import trade_logger


class LearningEngine:

    def analyze(self):

        trades = trade_logger.load()

        completed = [
            t for t in trades
            if t.get("result") in ("WIN", "LOSS")
        ]

        wins = sum(
            1 for t in completed
            if t.get("result") == "WIN"
        )

        strategy_stats = {}
        regime_stats = {}

        for trade in completed:

            strategy = trade.get("strategy", "UNKNOWN")
            regime = trade.get("market_regime", "UNKNOWN")
            win = trade.get("result") == "WIN"

            strategy_stats.setdefault(
                strategy,
                {"wins": 0, "total": 0},
            )

            regime_stats.setdefault(
                regime,
                {"wins": 0, "total": 0},
            )

            strategy_stats[strategy]["total"] += 1
            regime_stats[regime]["total"] += 1

            if win:
                strategy_stats[strategy]["wins"] += 1
                regime_stats[regime]["wins"] += 1

        strategy_rates = {
            k: round(v["wins"] * 100 / v["total"], 2)
            for k, v in strategy_stats.items()
            if v["total"] > 0
        }

        regime_rates = {
            k: round(v["wins"] * 100 / v["total"], 2)
            for k, v in regime_stats.items()
            if v["total"] > 0
        }

        return {
            "learning_ready": len(completed) > 0,
            "completed_trades": len(completed),
            "overall_win_rate": round(
                wins * 100 / len(completed),
                2,
            ) if completed else 0,
            "strategy_win_rates": strategy_rates,
            "regime_win_rates": regime_rates,
        }


learning_engine = LearningEngine()
