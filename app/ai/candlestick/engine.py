from app.ai.candlestick.engulfing import engulfing
from app.ai.candlestick.doji import doji
from app.ai.candlestick.hammer import hammer
from app.ai.candlestick.shooting_star import shooting_star
from app.ai.candlestick.morning_star import morning_star
from app.ai.candlestick.evening_star import evening_star
from app.ai.candlestick.three_white_soldiers import three_white_soldiers
from app.ai.candlestick.three_black_crows import three_black_crows


class CandlestickEngine:

    def analyze(self, df):

        return {

            **engulfing.detect(df),

            **doji.detect(df),

            **hammer.detect(df),

            **shooting_star.detect(df),

            **morning_star.detect(df),

            **evening_star.detect(df),

            **three_white_soldiers.detect(df),

            **three_black_crows.detect(df),

        }


candlestick_engine = CandlestickEngine()
