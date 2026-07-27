from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute("""
        SELECT symbol, entry, quantity
        FROM portfolio
        WHERE telegram_id=?
        ORDER BY id DESC
    """, (telegram_id,))

    rows = cursor.fetchall()

    if not rows:
        await update.message.reply_text("📜 No trade history.")
        return

    text = "📜 Trade History\n\n"

    for row in rows:
        text += (
            f"🪙 {row['symbol']}\n"
            f"Entry: {row['entry']}\n"
            f"Qty: {row['quantity']}\n\n"
        )

    await update.message.reply_text(text)
