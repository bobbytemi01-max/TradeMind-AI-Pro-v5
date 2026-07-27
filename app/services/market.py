"""
TradeMind AI Pro
Market Data Service
"""

import yfinance as yf


class MarketService:

    def get_history(
        self,
        symbol: str,
        period: str = "6mo",
        interval: str = "1d",
    ):

        symbol = symbol.upper().strip()

        # Only append -USD if it doesn't already exist
        if not symbol.endswith("-USD"):
            symbol = f"{symbol}-USD"

        ticker = yf.Ticker(symbol)

        df = ticker.history(
            period=period,
            interval=interval,
            auto_adjust=True,
        )

        if df.empty:
            return None

        return df


market = MarketService()
