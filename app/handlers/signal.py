from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("✅ SIGNAL COMMAND RECEIVED")

    if len(context.args) == 0:
    
        await update.message.reply_text(
            "Usage:\n/signal BTC"
        )
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if result is None:
        await update.message.reply_text("❌ Symbol not found.")
        return

    if result["direction"] == "🤝 WAIT":

        text = f"""
🤖 <b>TradeMind AI PRO</b>

🪙 <b>{symbol}/USD</b>

{result["recommendation"]}

━━━━━━━━━━━━━━━━━━

No high-probability trade setup detected.

Market Regime

{result["market_regime"]}

AI Score

{result["score"]}/100

Confidence

{result["confidence"]}%
"""

    else:

        text = f"""
🤖 <b>TradeMind AI PRO</b>

🪙 <b>{symbol}/USD</b>

{result["recommendation"]}

━━━━━━━━━━━━━━━━━━

Direction

{result["direction"]}

Entry

${result["entry"]:,.2f}

Stop Loss

${result["stop_loss"]:,.2f}

TP1

${result["tp1"]:,.2f}

TP2

${result["tp2"]:,.2f}

TP3

${result["tp3"]:,.2f}

━━━━━━━━━━━━━━━━━━

Risk / Reward

1 : {result["risk_reward"]}

Risk

{result["risk_level"]}

━━━━━━━━━━━━━━━━━━

AI Score

{result["score"]}/100

Confidence

{result["confidence"]}%
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML
    )