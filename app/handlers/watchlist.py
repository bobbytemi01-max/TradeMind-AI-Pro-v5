from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def watchlist(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute(
        """
        SELECT symbol
        FROM watchlist
        WHERE telegram_id = ?
        ORDER BY symbol
        """,
        (telegram_id,),
    )

    rows = cursor.fetchall()

    if not rows:
        await update.message.reply_text(
            "📋 Your watchlist is empty.\n\nUse /watch BTC to add a coin."
        )
        return

    text = "📋 Your Watchlist\n\n"

    for row in rows:
        text += f"🪙 {row['symbol']}\n"

    text += f"\nTotal: {len(rows)} assets"

    await update.message.reply_text(text)
