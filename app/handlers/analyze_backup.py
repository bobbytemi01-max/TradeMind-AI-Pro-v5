from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer


async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/analyze BTC"
        )
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if result is None:
        await update.message.reply_text("❌ Symbol not found.")
        return

    reasons = "\n".join(f"• {r}" for r in result["reasons"])

    text = f"""
🤖 <b>TradeMind AI PRO</b>

🪙 <b>{symbol}/USD</b>

━━━━━━━━━━━━━━━━━━

<b>Recommendation</b>

{result["recommendation"]}

<b>Trade Grade</b>

{result["trade_grade"]}

<b>AI Score</b>

{result["score"]}/100

<b>Confidence</b>

{result["confidence"]}%

<b>Market Regime</b>

{result["market_regime"]}

━━━━━━━━━━━━━━━━━━

<b>Price</b>

${result["price"]:,.2f}

<b>RSI</b>

{result["rsi"]:.2f}

<b>EMA20</b>

{result["ema20"]:.2f}

<b>EMA50</b>

{result["ema50"]:.2f}

<b>EMA200</b>

{result["ema200"]:.2f}

━━━━━━━━━━━━━━━━━━

<b>Reasons</b>

{reasons}

━━━━━━━━━━━━━━━━━━

🚀 <b>Powered by TradeMind AI Pro</b>
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML
    )