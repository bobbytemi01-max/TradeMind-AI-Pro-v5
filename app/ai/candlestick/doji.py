class Doji:

    def detect(self, df):

        if len(df) < 1:
            return {
            "doji": bool(False,)
        }

        candle = df.iloc[-1]

        body = abs(candle["Close"] - candle["Open"])
        range_ = candle["High"] - candle["Low"]

        if range_ == 0:
            return {
            "doji": bool(False,)
        }

        return {
            "doji": bool(body <= (range_ * 0.1))
        }


doji = Doji()
