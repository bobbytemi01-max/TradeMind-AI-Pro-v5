from app.services.alert_service import alert_service
from app.database.database import database


async def alert_job(context):

    alerts = alert_service.check_alerts()

    for alert in alerts:

        await context.bot.send_message(
            chat_id=alert["telegram_id"],
            text=(
                "🔔 PRICE ALERT\n\n"
                f"{alert['symbol']}\n"
                f"Current: ${alert['price']:.2f}\n"
                f"Target: ${alert['target']:.2f}"
            ),
        )

        cursor = database.conn.cursor()

        cursor.execute(
            "DELETE FROM alerts WHERE id=?",
            (alert["id"],),
        )

        database.conn.commit()
