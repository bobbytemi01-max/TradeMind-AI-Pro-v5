from app.services.market import market
from app.ai.institutional_engine import institutional_engine
from app.ai.candlestick.engine import candlestick_engine
from app.ai.candlestick.scorer import candlestick_scorer


class MultiTimeframeEngine:

    def analyze(self, symbol):

        timeframes = {

            "15m": ("7d", "15m"),
            "1h": ("30d", "1h"),
            "4h": ("90d", "4h"),
            "1d": ("6mo", "1d"),

        }

        result = {}

        agreement = 0

        for tf, (period, interval) in timeframes.items():

            df = market.get_history(
                symbol,
                period=period,
                interval=interval,
            )

            if df is None or df.empty:
                continue

            institutional = institutional_engine.analyze(df)

            candle = candlestick_engine.analyze(df)

            score = candlestick_scorer.score(candle)

            bias = institutional["institutional_bias"]

            if bias in ["BULLISH", "STRONG_BULLISH"]:
                agreement += 1

            result[tf] = {

                "institutional": bias,

                "candlestick": score["candlestick_bias"],

                "score": score["candlestick_score"],

            }

        result["agreement"] = agreement

        return result


multi_timeframe = MultiTimeframeEngine()
