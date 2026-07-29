class SwingDetector:

    def highs(self, df, left=2, right=2):

        swings = []

        highs = df["High"].tolist()

        for i in range(left, len(highs) - right):

            if highs[i] == max(highs[i-left:i+right+1]):

                swings.append((i, highs[i]))

        return swings

    def lows(self, df, left=2, right=2):

        swings = []

        lows = df["Low"].tolist()

        for i in range(left, len(lows) - right):

            if lows[i] == min(lows[i-left:i+right+1]):

                swings.append((i, lows[i]))

        return swings


swing_detector = SwingDetector()
