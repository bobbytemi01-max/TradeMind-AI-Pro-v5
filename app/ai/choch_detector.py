from app.ai.swing_detector import swing_detector


class CHOCHDetector:

    def detect(self, df):

        highs = swing_detector.highs(df)
        lows = swing_detector.lows(df)

        if len(highs) < 2 or len(lows) < 2:
            return {
                "choch": False,
                "direction": "NONE",
            }

        last_high = highs[-1][1]
        prev_high = highs[-2][1]

        last_low = lows[-1][1]
        prev_low = lows[-2][1]

        if last_high > prev_high and last_low < prev_low:
            return {
                "choch": True,
                "direction": "REVERSAL",
            }

        return {
            "choch": False,
            "direction": "TREND",
        }


choch_detector = CHOCHDetector()
