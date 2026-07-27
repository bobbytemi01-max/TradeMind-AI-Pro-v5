from ta.momentum import RSIIndicator


def rsi(df):
    """
    Calculate the latest RSI value.
    """

    indicator = RSIIndicator(
        close=df["Close"],
        window=14,
    )

    return float(
        indicator.rsi().iloc[-1]
    )