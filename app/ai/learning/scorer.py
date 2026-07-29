class LearningScorer:

    def score(self, learning):

        if not learning["learning_ready"]:
            return {
                "learning_score": 50,
                "learning_reasons": [
                    "No historical learning available"
                ]
            }

        score = learning["overall_win_rate"]

        reasons = [
            f'Historical win rate {learning["overall_win_rate"]}%'
        ]

        return {
            "learning_score": score,
            "learning_reasons": reasons
        }


learning_scorer = LearningScorer()
