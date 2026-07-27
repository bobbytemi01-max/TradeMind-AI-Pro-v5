from telegram import Update
from telegram.ext import ContextTypes

from app.services.news_service import news_service


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):

    articles = news_service.latest()

    text = "📰 Latest Crypto News\n\n"

    for article in articles:
        text += (
            f"• {article['title']}\n"
            f"{article['link']}\n\n"
        )

    await update.message.reply_text(
        text,
        disable_web_page_preview=True,
    )
