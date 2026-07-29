from app.ai.smc.equal_highs_lows import equal_highs_lows


class LiquidityPool:

    def analyze(self, df):

        eql = equal_highs_lows.analyze(df)

        pools = []

        if eql["equal_highs"]:
            pools.append({
                "type": "BUY_SIDE",
                "level": eql["equal_high_level"],
            })

        if eql["equal_lows"]:
            pools.append({
                "type": "SELL_SIDE",
                "level": eql["equal_low_level"],
            })

        nearest = None

        if pools:
            price = float(df["Close"].iloc[-1])
            nearest = min(
                pools,
                key=lambda x: abs(x["level"] - price)
            )

        return {
            "liquidity_pools": pools,
            "nearest_liquidity": nearest,
        }


liquidity_pool = LiquidityPool()
