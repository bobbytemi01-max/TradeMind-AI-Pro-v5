import yfinance as yf
import pandas as pd


class MarketData:

    def __init__(self):
        self.cache = {}

    def get_history(
        self,
        symbol: str,
        period: str = "6mo",
        interval: str = "1d"
    ) -> pd.DataFrame:

        key = f"{symbol}_{period}_{interval}"

        if key in self.cache:
            return self.cache[key]

        ticker = yf.Ticker(f"{symbol.upper()}-USD")

        df = ticker.history(
            period=period,
            interval=interval,
            auto_adjust=True
        )

        if df.empty:
            return None

        df = df.dropna()

        self.cache[key] = df

        return df


market = MarketData()