from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/price BTC"
        )
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if result is None:
        await update.message.reply_text("❌ Symbol not found.")
        return

    text = f"""
💰 <b>{symbol}/USD</b>

Current Price

<b>${result["price"]:,.2f}</b>

Market Regime

{result["market_regime"]}

AI Recommendation

{result["recommendation"]}

AI Score

{result["score"]}/100
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML
    )