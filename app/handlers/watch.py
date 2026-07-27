from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def watch(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Usage:\n/watch BTC")
        return

    symbol = context.args[0].upper()
    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        "SELECT 1 FROM watchlist WHERE telegram_id=? AND symbol=?",
        (telegram_id, symbol),
    )

    if cursor.fetchone():
        await update.message.reply_text(
            f"⚠️ {symbol} is already in your watchlist."
        )
        return

    cursor.execute(
        "INSERT INTO watchlist (telegram_id, symbol) VALUES (?, ?)",
        (telegram_id, symbol),
    )

    database.conn.commit()

    await update.message.reply_text(
        f"✅ {symbol} added to your watchlist."
    )
