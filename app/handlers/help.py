from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🤖 <b>TradeMind AI Pro</b>

<b>Core</b>
/start
/help
/about
/status
/version

<b>Trading</b>
/price BTC
/analyze BTC
/signal BTC
/dashboard BTC
/chart BTC
/scan

<b>Portfolio</b>
/watchlist
/watch BTC
/alerts
/profile

<b>AI</b>
/news BTC
/why BTC
/explain BTC

🚀 Powered by TradeMind AI Pro
"""

    await update.message.reply_html(text)
