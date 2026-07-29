"""
TradeMind AI Pro Analyzer Service
"""

from app.services.market import market
from app.services.indicators import indicator_service
from app.services.trade_engine import trade_engine

from app.ai.consensus import consensus
from app.ai.smc import smc
from app.ai.binary_engine import binary_engine
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

        # Smart Money Concepts
        smc_data = smc.analyze(indicators)

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
            **smc_data,

            # Binary AI
            **binary,

        }

        return result


analyzer = AnalyzerService()
