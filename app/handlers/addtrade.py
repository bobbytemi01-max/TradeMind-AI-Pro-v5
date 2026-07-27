from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def addtrade(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 3:
        await update.message.reply_text(
            "Usage:\n/addtrade BTC 65000 0.5"
        )
        return

    symbol = context.args[0].upper()

    try:
        entry = float(context.args[1])
        quantity = float(context.args[2])
    except ValueError:
        await update.message.reply_text("Invalid numbers.")
        return

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        INSERT INTO portfolio
        (telegram_id, symbol, entry, quantity)
        VALUES (?, ?, ?, ?)
        """,
        (telegram_id, symbol, entry, quantity),
    )

    database.conn.commit()

    await update.message.reply_text(
        f"✅ Trade added\n\n"
        f"{symbol}\n"
        f"Entry: {entry}\n"
        f"Qty: {quantity}"
    )
