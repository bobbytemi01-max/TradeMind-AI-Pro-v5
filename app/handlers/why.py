from telegram import Update
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer


async def why(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Usage:\n/why BTC")
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if not result:
        await update.message.reply_text("Analysis failed.")
        return

    reasons = result.get("reasons", [])

    text = f"🧠 Why {result['recommendation']}\n\n"

    if reasons:
        for reason in reasons:
            text += f"✅ {reason}\n"
    else:
        text += "No explanation available."

    await update.message.reply_text(text)
