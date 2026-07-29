from app.indicators import (
    ema,
    rsi,
    macd,
    atr,
    bollinger,
    average_volume,
    adx,
    vwap,
)


class IndicatorService:

    def calculate(self, df):

        macd_line, signal_line, histogram = macd(df)

        bb_high, bb_mid, bb_low = bollinger(df)

        return {

            "price": float(df["Close"].iloc[-1]),

            "ema20": ema(df, 20),
            "ema50": ema(df, 50),
            "ema200": ema(df, 200),

            "rsi": rsi(df),

            "macd": macd_line,
            "signal": signal_line,
            "histogram": histogram,

            "atr": atr(df),

            "bb_high": bb_high,
            "bb_mid": bb_mid,
            "bb_low": bb_low,

            "macd": macd_line,
            "macd_signal": signal_line,
            "macd_histogram": histogram,

            "adx": adx(df),
            "vwap": vwap(df),

            "support": float(df["Low"].tail(20).min()),
            "resistance": float(df["High"].tail(20).max()),

            "volume": float(df["Volume"].iloc[-1]),
            "volume_sma": average_volume(df),

        }


indicator_service = IndicatorService()