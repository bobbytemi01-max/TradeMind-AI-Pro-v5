from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def unwatch(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/unwatch BTC"
        )
        return

    symbol = context.args[0].upper()

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        DELETE FROM watchlist
        WHERE telegram_id = ?
        AND symbol = ?
        """,
        (telegram_id, symbol),
    )

    database.conn.commit()

    if cursor.rowcount == 0:
        await update.message.reply_text(
            f"⚠️ {symbol} is not in your watchlist."
        )
    else:
        await update.message.reply_text(
            f"✅ {symbol} removed from your watchlist."
        )
