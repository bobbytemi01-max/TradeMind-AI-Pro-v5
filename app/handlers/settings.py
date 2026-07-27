from telegram import Update
from telegram.ext import ContextTypes


async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
⚙️ TradeMind Settings

Current Settings

• Timeframe: 1D
• Risk Level: Medium
• Alerts: ON
• News: ON

🚧 Custom settings coming soon.
"""

    await update.message.reply_text(text)
