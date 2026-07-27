from ta.volatility import BollingerBands


def bollinger(df):
    """
    Calculate the latest Bollinger Bands.
    Returns:
        (upper_band, middle_band, lower_band)
    """

    bb = BollingerBands(
        close=df["Close"],
        window=20,
        window_dev=2,
    )

    return (
        float(bb.bollinger_hband().iloc[-1]),
        float(bb.bollinger_mavg().iloc[-1]),
        float(bb.bollinger_lband().iloc[-1]),
    )