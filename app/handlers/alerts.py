from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        SELECT symbol, target_price
        FROM alerts
        WHERE telegram_id=?
        ORDER BY symbol
        """,
        (telegram_id,),
    )

    rows = cursor.fetchall()

    if not rows:
        await update.message.reply_text(
            "🔔 No active alerts."
        )
        return

    text = "🔔 Your Alerts\n\n"

    for row in rows:
        text += f"🪙 {row['symbol']} → {row['target_price']}\n"

    text += f"\nTotal: {len(rows)}"

    await update.message.reply_text(text)
