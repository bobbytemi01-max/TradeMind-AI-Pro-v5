"""
TradeMind AI Pro Analyzer Service
"""

from app.services.market import market
from app.services.indicators import indicator_service
from app.services.trade_engine import trade_engine
from app.trade.trade_manager import trade_manager

from app.ai.consensus import consensus
from app.ai.binary_engine import binary_engine
from app.ai.institutional_engine import institutional_engine
from app.ai.candlestick.engine import candlestick_engine
from app.ai.candlestick.scorer import candlestick_scorer
from app.ai.master.master_engine import master_engine



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

        master = master_engine.analyze(symbol, df, indicators)

        # AI Consensus
        ai = consensus.calculate(indicators)

        # Trade Plan (Master AI)

        decision = {
            "recommendation": master["decision"],
            "direction": master["decision"],
            "trade_allowed": master["decision"] != "WAIT",
            "risk_level": "LOW" if master["confidence_v2"] >= 80 else "MEDIUM",
        }

        trade = trade_engine.build(
            indicators,
            ai,
            decision,
        )


        if trade["trade_allowed"]:
            trade_manager.open_trade(
                symbol=symbol.upper(),
                signal=trade["direction"],
                entry=trade["entry"],
                stop_loss=trade["stop_loss"],
                tp1=trade["tp1"],
                tp2=trade["tp2"],
                tp3=trade["tp3"],
                confidence=master["confidence_v2"],
                institutional=master.get("institutional_bias", "UNKNOWN"),
                probability=master.get("execution_probability", 0),
                session=master.get("session", "UNKNOWN"),
                zone=master.get("premium_discount_zone", "UNKNOWN"),
                agreement=master.get("agreement", 0),
                strategy=master.get("strategy", "UNKNOWN"),
                market_regime=master.get("market_regime", "UNKNOWN"),
                trade_grade=master.get("trade_grade_v2", "UNKNOWN"),
                fusion_score=master.get("fusion_score", 0),
                confluence_score=master.get("confluence_score", 0),
            )

        institutional = institutional_engine.analyze(df)
        candlestick = candlestick_engine.analyze(df)

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

            # Master AI
            **master,

            # Smart Money Concepts
            **institutional,
            **candlestick,

            # Binary AI
            **binary,

            # Institutional AI
            **institutional,

        }

        return result


analyzer = AnalyzerService()

