"""
TradeMind AI Pro Analyzer Service
"""

from app.services.market import market
from app.services.indicators import indicator_service
from app.services.trade_engine import trade_engine

from app.ai.consensus import consensus
from app.ai.binary_engine import binary_engine
from app.ai.institutional_engine import institutional_engine
from app.ai.decision_engine import decision_engine


class AnalyzerService:

    def analyze(
        self,
        symbol: str,
        period: str = "6mo",
        interval: str = "1d"
    ):

        df = market.get_history(
            symbol,
            period=period,
            interval=interval,
        )

        if df is None or df.empty:
            return None

        return self.analyze_dataframe(symbol, df)

    def analyze_dataframe(self, symbol, df):

        # Indicators
        indicators = indicator_service.calculate(df)

        # AI Consensus
        ai = consensus.calculate(indicators)

        # AI Decision
        decision = decision_engine.decide(
            indicators,
            ai,
        )

        # Trade Plan
        trade = trade_engine.build(
            indicators,
            ai,
            decision,
        )

        institutional = institutional_engine.analyze(df)

        # Smart Money Concepts
        institutional = institutional_engine.analyze(df)

        binary = binary_engine.decide(indicators)

        binary = binary_engine.decide(indicators)

        # Final Result
        result = {

            "symbol": symbol.upper(),

            # Indicators
            **indicators,

            # AI Scores
            **ai,

            # Decision
            **decision,

            # Trade
            **trade,

            # Smart Money Concepts
            **institutional,

            # Binary AI
            **binary,

            # Institutional AI
            **institutional,

        }

        return result


analyzer = AnalyzerService()
