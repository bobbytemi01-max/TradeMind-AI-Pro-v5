from datetime import datetime, timezone


class SessionEngine:

    def current(self):

        hour = datetime.now(timezone.utc).hour

        if 0 <= hour < 8:
            return {
                "session": "ASIAN",
                "session_score": 60,
            }

        elif 8 <= hour < 13:
            return {
                "session": "LONDON",
                "session_score": 90,
            }

        elif 13 <= hour < 22:
            return {
                "session": "NEW_YORK",
                "session_score": 95,
            }

        return {
            "session": "AFTER_HOURS",
            "session_score": 40,
        }


session_engine = SessionEngine()
