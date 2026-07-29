class FVGDetector:

    def detect(self, df):

        if len(df) < 3:
            return {
                "fvg": False,
                "direction": "NONE",
                "top": None,
                "bottom": None,
            }

        c1 = df.iloc[-3]
        c2 = df.iloc[-2]
        c3 = df.iloc[-1]

        # Bullish FVG
        if c1["High"] < c3["Low"]:
            return {
                "fvg": True,
                "direction": "BULLISH",
                "top": float(c3["Low"]),
                "bottom": float(c1["High"]),
            }

        # Bearish FVG
        if c1["Low"] > c3["High"]:
            return {
                "fvg": True,
                "direction": "BEARISH",
                "top": float(c1["Low"]),
                "bottom": float(c3["High"]),
            }

        return {
            "fvg": False,
            "direction": "NONE",
            "top": None,
            "bottom": None,
        }


fvg_detector = FVGDetector()
