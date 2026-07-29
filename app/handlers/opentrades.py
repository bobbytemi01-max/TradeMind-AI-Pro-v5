from telegram import Update
from telegram.ext import ContextTypes

from app.ai.learning.trade_logger import trade_logger


async def opentrades(update: Update, context: ContextTypes.DEFAULT_TYPE):

    trades = trade_logger.load()

    open_trades = [
        (i, t) for i, t in enumerate(trades)
        if t.get("status") == "OPEN"
    ]

    if not open_trades:
        await update.message.reply_text("📭 No open trades.")
        return

    text = "📊 <b>Open Trades</b>\n\n"

    for idx, trade in open_trades:
        text += (
            f"#{idx}\n"
            f"{trade['symbol']} • {trade['signal']}\n"
            f"Entry: {trade['entry']}\n"
            f"Confidence: {trade['confidence']}%\n"
            f"Status: {trade['status']}\n\n"
        )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )
