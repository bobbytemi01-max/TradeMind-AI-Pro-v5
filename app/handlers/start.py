from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 <b>Welcome to TradeMind AI Pro v6</b>

Your AI-powered crypto trading assistant.

━━━━━━━━━━━━━━━━━━

<b>Available Commands</b>

🚀 /start
Show this welcome message

💰 /price BTC
Current market price

📊 /analyze BTC
Complete AI market analysis

🎯 /signal BTC
Professional trade signal

📈 /dashboard BTC
Premium AI dashboard

❓ /help
Show help

━━━━━━━━━━━━━━━━━━

Powered by <b>TradeMind AI Pro</b>
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML
    )