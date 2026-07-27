from ta.trend import MACD


def macd(df):
    """
    Calculate MACD, Signal and Histogram.
    """

    indicator = MACD(
        close=df["Close"],
        window_slow=26,
        window_fast=12,
        window_sign=9,
    )

    return (
        float(indicator.macd().iloc[-1]),
        float(indicator.macd_signal().iloc[-1]),
        float(indicator.macd_diff().iloc[-1]),
    )