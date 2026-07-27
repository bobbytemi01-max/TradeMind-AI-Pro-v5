import pandas as pd
from ta.trend import ADXIndicator


def adx(df: pd.DataFrame) -> float:
    """
    Calculate the latest ADX value.
    """

    indicator = ADXIndicator(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        window=14,
    )

    return float(indicator.adx().iloc[-1])