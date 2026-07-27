"""
Volume analysis utilities.
"""

import pandas as pd


def average_volume(df: pd.DataFrame, period: int = 20) -> float:
    """
    Calculate the average trading volume over the specified period.
    """

    return float(
        df["Volume"]
        .tail(period)
        .mean()
    )