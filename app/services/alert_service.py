from app.database.database import database
from app.services.market import market


class AlertService:

    def check_alerts(self):

        cursor = database.conn.cursor()

        cursor.execute("""
            SELECT id, telegram_id, symbol, target_price
            FROM alerts
        """)

        triggered = []

        for row in cursor.fetchall():

            df = market.get_history(row["symbol"], period="5d")

            if df is None:
                continue

            price = float(df["Close"].iloc[-1])

            if price >= row["target_price"]:

                triggered.append({
                    "id": row["id"],
                    "telegram_id": row["telegram_id"],
                    "symbol": row["symbol"],
                    "price": price,
                    "target": row["target_price"],
                })

        return triggered


alert_service = AlertService()
