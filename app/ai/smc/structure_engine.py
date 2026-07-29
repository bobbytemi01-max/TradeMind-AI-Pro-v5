from app.ai.institutional_engine import institutional_engine
from app.ai.smc.premium_discount import premium_discount
from app.ai.smc.equal_highs_lows import equal_highs_lows
from app.ai.smc.liquidity_pool import liquidity_pool


class StructureEngine:

    def analyze(self, df):

        institutional = institutional_engine.analyze(df)
        premium = premium_discount.analyze(df)
        equal_levels = equal_highs_lows.analyze(df)
        liquidity = liquidity_pool.analyze(df)

        return {
            **institutional,
            **premium,
            **equal_levels,
            **liquidity,
        }


structure_engine = StructureEngine()
