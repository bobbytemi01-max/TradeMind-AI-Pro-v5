from app.ai.bos_detector import bos_detector
from app.ai.choch_detector import choch_detector
from app.ai.liquidity_detector import liquidity_detector
from app.ai.fvg_detector import fvg_detector
from app.ai.order_block_detector import order_block_detector


class InstitutionalEngine:

    def analyze(self, df):

        if df is None or df.empty:
            return {
                "institutional_bias": "UNKNOWN",
                "institutional_score": 0,
                "bos": False,
                "choch": False,
                "liquidity_sweep": False,
                "fvg": False,
                "order_block": False,
            }

        bos = bos_detector.detect(df)
        choch = choch_detector.detect(df)
        liquidity = liquidity_detector.detect(df)
        fvg = fvg_detector.detect(df)
        order_block = order_block_detector.detect(df)

        score = 0

        if bos["bos"]:
            score += 25

        if choch["choch"]:
            score += 20

        if liquidity["liquidity_sweep"]:
            score += 15

        if fvg["fvg"]:
            score += 20

        if order_block["order_block"]:
            score += 20

        if score >= 80:
            bias = "STRONG_BULLISH"

        elif score >= 60:
            bias = "BULLISH"

        elif score >= 40:
            bias = "NEUTRAL"

        else:
            bias = "BEARISH"

        return {

            "institutional_bias": bias,

            "institutional_score": score,

            **bos,
            **choch,
            **liquidity,
            **fvg,
            **order_block,

        }


institutional_engine = InstitutionalEngine()
