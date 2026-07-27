from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer


async def analyze_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Usage:\n/analyze BTC")
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if result is None:
        await update.message.reply_text("❌ Symbol not found.")
        return

    reasons = "\n".join(f"• {r}" for r in result.get("reasons", []))

    text = f"""
🤖 <b>TradeMind AI PRO</b>

🪙 <b>{symbol}/USD</b>

━━━━━━━━━━━━━━━━━━

📈 <b>Recommendation</b>

{result["recommendation"]}

🏆 <b>Trade Grade</b>

{result["trade_grade"]}

🧠 <b>AI Score</b>

{result["score"]}/100

🎯 <b>Confidence</b>

{result["confidence"]}%

🌍 <b>Market Regime</b>

{result["market_regime"]}

━━━━━━━━━━━━━━━━━━

💼 <b>Trade Setup</b>

Entry: ${result["entry"]:,.2f}

Stop Loss: ${result["stop_loss"]:,.2f}

TP1: ${result["tp1"]:,.2f}

TP2: ${result["tp2"]:,.2f}

TP3: ${result["tp3"]:,.2f}

Risk / Reward: {result["risk_reward"]}

━━━━━━━━━━━━━━━━━━

📊 <b>Market Data</b>

Price: ${result["price"]:,.2f}

RSI: {result["rsi"]:.2f}

EMA20: {result["ema20"]:,.2f}

EMA50: {result["ema50"]:,.2f}

EMA200: {result["ema200"]:,.2f}

━━━━━━━━━━━━━━━━━━

📝 <b>AI Reasons</b>

{reasons}

━━━━━━━━━━━━━━━━━━

🚀 <b>Powered by TradeMind AI Pro</b>
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )
