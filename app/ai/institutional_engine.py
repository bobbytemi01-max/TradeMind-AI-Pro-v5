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
        reasons = []

        # BOS
        if bos["bos"]:
            score += 35
            reasons.append("Break of Structure")

        # CHoCH
        if choch["choch"]:
            score += 20
            reasons.append("Change of Character")

        # FVG
        if fvg["fvg"]:
            score += 15
            reasons.append("Fair Value Gap")

            if fvg.get("direction") == "BULLISH":
                score += 10

            elif fvg.get("direction") == "BEARISH":
                score -= 10

        # Order Block
        if order_block["order_block"]:
            score += 20
            reasons.append("Order Block")

            if order_block.get("direction") == "BULLISH":
                score += 10

            elif order_block.get("direction") == "BEARISH":
                score -= 10

        # Liquidity
        if liquidity["liquidity_sweep"]:
            reasons.append("Liquidity Sweep")

            if liquidity["side"] == "SELL_SIDE":
                score += 20

            elif liquidity["side"] == "BUY_SIDE":
                score -= 20

        # Synergy Bonuses
        if bos["bos"] and order_block["order_block"]:
            score += 15

        if choch["choch"] and fvg["fvg"]:
            score += 10

        if bos["bos"] and liquidity["liquidity_sweep"]:
            score += 10

        # Clamp
        score = max(-100, min(100, score))

        if score >= 70:
            bias = "STRONG_BULLISH"
        elif score >= 35:
            bias = "BULLISH"
        elif score <= -70:
            bias = "STRONG_BEARISH"
        elif score <= -35:
            bias = "BEARISH"
        else:
            bias = "NEUTRAL"

        return {

            "institutional_bias": bias,
            "institutional_score": score,
            "institutional_reasons": reasons,

            **bos,
            **choch,
            **liquidity,
            **fvg,
            **order_block,

        }


institutional_engine = InstitutionalEngine()
