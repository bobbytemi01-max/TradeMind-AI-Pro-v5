from app.ai.swing_detector import swing_detector


class BOSDetector:

    def detect(self, df):

        swings = swing_detector.highs(df)

        if len(swings) < 2:
            return {
                "bos": False,
                "bos_level": None,
            }

        last_high = swings[-1][1]

        close = df["Close"].iloc[-1]

        return {
            "bos": close > last_high,
            "bos_level": last_high,
        }


bos_detector = BOSDetector()
