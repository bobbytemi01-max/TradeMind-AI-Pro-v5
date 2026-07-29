class EqualHighsLows:

    def analyze(self, df, tolerance=0.002):

        highs = df["High"].tail(30).tolist()
        lows = df["Low"].tail(30).tolist()

        equal_highs = False
        equal_lows = False

        high_level = None
        low_level = None

        # Equal Highs
        for i in range(len(highs)-1):
            if abs(highs[i] - highs[i+1]) / highs[i] <= tolerance:
                equal_highs = True
                high_level = round((highs[i] + highs[i+1]) / 2, 2)
                break

        # Equal Lows
        for i in range(len(lows)-1):
            if abs(lows[i] - lows[i+1]) / lows[i] <= tolerance:
                equal_lows = True
                low_level = round((lows[i] + lows[i+1]) / 2, 2)
                break

        return {
            "equal_highs": equal_highs,
            "equal_high_level": high_level,
            "equal_lows": equal_lows,
            "equal_low_level": low_level,
        }


equal_highs_lows = EqualHighsLows()
