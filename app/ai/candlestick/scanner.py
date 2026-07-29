from app.services.market import market
from app.ai.candlestick.engine import candlestick_engine
from app.ai.candlestick.scorer import candlestick_scorer


class CandlestickScanner:

    def analyze(self, symbol):

        df = market.get_history(symbol)

        if df is None or df.empty:
            return None

        patterns = candlestick_engine.analyze(df)
        score = candlestick_scorer.score(patterns)

        return {
            "symbol": symbol.upper(),
            **patterns,
            **score,
        }


candlestick_scanner = CandlestickScanner()
