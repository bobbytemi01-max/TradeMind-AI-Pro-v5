from ta.volatility import AverageTrueRange


def atr(df):
    """
    Calculate the latest ATR value.
    """

    indicator = AverageTrueRange(
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        window=14,
    )

    return float(
        indicator.average_true_range().iloc[-1]
    )