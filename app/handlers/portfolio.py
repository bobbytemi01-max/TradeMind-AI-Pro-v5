from telegram import Update
from telegram.ext import ContextTypes

from app.database.database import database
from app.services.market import market


async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):

    telegram_id = update.effective_user.id

    cursor = database.conn.cursor()

    cursor.execute("""
        SELECT symbol, entry, quantity
        FROM portfolio
        WHERE telegram_id=?
        ORDER BY symbol
    """, (telegram_id,))

    rows = cursor.fetchall()

    if not rows:
        await update.message.reply_text(
            "💼 Portfolio is empty.\n\nUse /addtrade BTC 65000 0.5"
        )
        return

    text = "💼 TradeMind Portfolio\n\n"

    total_value = 0

    for row in rows:

        symbol = row["symbol"]
        entry = float(row["entry"])
        qty = float(row["quantity"])

        df = market.get_history(symbol, period="5d")

        if df is None:
            continue

        current = float(df["Close"].iloc[-1])

        pnl = (current - entry) * qty
        pnl_pct = ((current - entry) / entry) * 100
        value = current * qty

        total_value += value

        icon = "🟢" if pnl >= 0 else "🔴"

        text += (
            f"{icon} {symbol}\n"
            f"Entry: ${entry:,.2f}\n"
            f"Current: ${current:,.2f}\n"
            f"P/L: ${pnl:,.2f} ({pnl_pct:.2f}%)\n"
            f"Qty: {qty}\n"
            f"Value: ${value:,.2f}\n\n"
        )

    text += f"💰 Total Value: ${total_value:,.2f}"

    await update.message.reply_text(text)
