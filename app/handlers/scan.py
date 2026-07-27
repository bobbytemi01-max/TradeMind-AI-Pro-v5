from telegram import Update
from telegram.ext import ContextTypes
import time

from app.scanner.scanner import scanner


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("✅ /scan command received")

    # Tell the user immediately
    await update.message.reply_text(
        "🔍 Scanning crypto markets...\nPlease wait..."
    )

    start = time.time()

    results = scanner.scan()

    print(f"✅ Scan completed in {time.time() - start:.2f} seconds")

    if not results:
        await update.message.reply_text(
            "❌ No markets could be analyzed."
        )
        return

    text = "🔥 <b>TradeMind AI Scanner</b>\n\n"

    medals = ["🥇", "🥈", "🥉"]

    for i, item in enumerate(results[:10]):

        medal = medals[i] if i < 3 else "📌"

        text += (
            f"{medal} <b>{item['symbol']}</b>\n"
            f"{item['recommendation']}\n"
            f"Score: <b>{item['score']}</b>\n"
            f"Confidence: <b>{item['confidence']}%</b>\n\n"
        )

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )