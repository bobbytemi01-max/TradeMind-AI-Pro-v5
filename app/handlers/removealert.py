from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def removealert(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/removealert BTC"
        )
        return

    symbol = context.args[0].upper()
    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        DELETE FROM alerts
        WHERE telegram_id=?
        AND symbol=?
        """,
        (telegram_id, symbol),
    )

    database.conn.commit()

    if cursor.rowcount:
        await update.message.reply_text(
            f"✅ Alert removed for {symbol}"
        )
    else:
        await update.message.reply_text(
            f"⚠️ No alert found for {symbol}"
        )
