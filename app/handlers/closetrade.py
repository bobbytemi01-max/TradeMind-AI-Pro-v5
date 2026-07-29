from telegram import Update
from telegram.ext import ContextTypes

from app.trade.trade_manager import trade_manager


async def closetrade(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) != 2:
        await update.message.reply_text(
            "Usage:\n/closetrade <id> WIN\n/closetrade <id> LOSS"
        )
        return

    try:
        trade_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("❌ Trade ID must be a number.")
        return

    result = context.args[1].upper()

    if result not in ("WIN", "LOSS"):
        await update.message.reply_text(
            "❌ Result must be WIN or LOSS."
        )
        return

    if trade_manager.close_trade(trade_id, result):

        await update.message.reply_text(
            f"✅ Trade #{trade_id} closed.\n\n"
            f"Result: {result}"
        )

    else:

        await update.message.reply_text(
            "❌ Trade not found."
        )
