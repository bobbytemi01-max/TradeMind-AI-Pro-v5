"""
TradeMind AI Pro v6
Multi-Timeframe Analysis
"""

from app.services.market import market
from app.services.indicators import indicator_service

from app.ai.consensus import consensus
from app.ai.decision_engine import decision_engine


class MultiTimeframeAnalyzer:

    TIMEFRAMES = {

        "15m": ("30d", "15m", 1),

        "1H": ("90d", "1h", 2),

        "4H": ("180d", "4h", 3),

        "1D": ("1y", "1d", 4),

    }

    def analyze(self, symbol):

        results = {}

        weighted_buy = 0
        weighted_sell = 0
        weighted_wait = 0

        total_score = 0
        total_weight = 0

        for tf, (period, interval, weight) in self.TIMEFRAMES.items():

            df = market.get_history(
                symbol,
                period=period,
                interval=interval,
            )

            if df is None or df.empty:
                continue

            # -------------------------
            # Indicators
            # -------------------------

            indicators = indicator_service.calculate(df)

            # -------------------------
            # AI Consensus
            # -------------------------

            ai = consensus.calculate(indicators)

            # -------------------------
            # Decision Engine
            # -------------------------

            decision = decision_engine.decide(
                indicators,
                ai,
            )

            results[tf] = {

                "recommendation": decision["recommendation"],

                "score": ai["score"],

                "confidence": ai["confidence"],

                "market_regime": ai["market_regime"],

                "direction": decision["direction"],

            }

            total_score += ai["score"] * weight
            total_weight += weight

            direction = decision["direction"]

            if direction == "BUY":
                weighted_buy += weight

            elif direction == "SELL":
                weighted_sell += weight

            else:
                weighted_wait += weight

        if not results:
            return None

        average = round(total_score / total_weight, 1)

        # -------------------------
        # Final Recommendation
        # -------------------------

        if weighted_buy >= 6:
            final = "🟢 BUY"

        elif weighted_sell >= 6:
            final = "🔴 SELL"

        else:
            final = "🤝 WAIT"

        return {

            "average_score": average,

            "final_recommendation": final,

            "buy_votes": weighted_buy,

            "sell_votes": weighted_sell,

            "wait_votes": weighted_wait,

            "timeframes": results,

        }


multi_timeframe = MultiTimeframeAnalyzer()