from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.effective_user
    telegram_id = user.id

    cursor = database.conn.cursor()

    cursor.execute(
        "SELECT joined_at FROM users WHERE telegram_id=?",
        (telegram_id,),
    )

    row = cursor.fetchone()

    if not row:
        cursor.execute(
            "INSERT INTO users (telegram_id, username) VALUES (?, ?)",
            (telegram_id, user.username),
        )
        database.conn.commit()
        joined = "Today"
    else:
        joined = row["joined_at"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM watchlist WHERE telegram_id=?",
        (telegram_id,),
    )
    watchlist = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM alerts WHERE telegram_id=?",
        (telegram_id,),
    )
    alerts = cursor.fetchone()["total"]

    cursor.execute(
        "SELECT COUNT(*) AS total FROM portfolio WHERE telegram_id=?",
        (telegram_id,),
    )
    portfolio = cursor.fetchone()["total"]

    text = f"""👤 TradeMind AI Pro

Username: @{user.username or "Unknown"}

Member Since:
{joined}

Watchlist:
{watchlist}

Alerts:
{alerts}

Portfolio:
{portfolio}

Subscription:
Free
"""

    await update.message.reply_text(text)
