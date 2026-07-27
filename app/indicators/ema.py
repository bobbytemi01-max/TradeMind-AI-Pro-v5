import pandas as pd


def ema(df: pd.DataFrame, period: int) -> float:
    """
    Calculate the latest EMA value.
    """

    return float(
        df["Close"]
        .ewm(span=period, adjust=False)
        .mean()
        .iloc[-1]
    )