from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 2:
        await update.message.reply_text(
            "Usage:\n/alert BTC 120000"
        )
        return

    symbol = context.args[0].upper()

    try:
        target = float(context.args[1])
    except ValueError:
        await update.message.reply_text("Invalid price.")
        return

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        INSERT INTO alerts
        (telegram_id, symbol, target_price)
        VALUES (?, ?, ?)
        """,
        (telegram_id, symbol, target),
    )

    database.conn.commit()

    await update.message.reply_text(
        f"🔔 Alert created\n\n{symbol} → {target}"
    )
