class BacktestEngine:

    def run(self, signals):

        trades = 0
        wins = 0
        losses = 0

        for signal in signals:

            if signal.get("result") == "WIN":
                wins += 1
                trades += 1

            elif signal.get("result") == "LOSS":
                losses += 1
                trades += 1

        win_rate = round(
            wins / trades * 100,
            2
        ) if trades else 0

        return {
            "trades": trades,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate,
        }


backtest_engine = BacktestEngine()
