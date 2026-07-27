import pandas as pd


def vwap(df: pd.DataFrame) -> float:
    """
    Calculate VWAP.
    """

    typical_price = (
        df["High"] +
        df["Low"] +
        df["Close"]
    ) / 3

    cumulative_tp_volume = (
        typical_price * df["Volume"]
    ).cumsum()

    cumulative_volume = df["Volume"].cumsum()

    return float(
        (
            cumulative_tp_volume /
            cumulative_volume
        ).iloc[-1]
    )