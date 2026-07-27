from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.analyzer import analyzer
from app.services.multi_timeframe import multi_timeframe


async def dashboard(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage:\n/dashboard BTC"
        )
        return

    symbol = context.args[0].upper()

    result = analyzer.analyze(symbol)

    if result is None:
        await update.message.reply_text("❌ Symbol not found.")
        return

    mtf = multi_timeframe.analyze(symbol)

    if mtf is None:
        await update.message.reply_text("❌ Unable to analyze multiple timeframes.")
        return

    tf = mtf["timeframes"]

    def tf_line(name):
        if name not in tf:
            return "N/A"

        return f'{tf[name]["recommendation"]} ({tf[name]["score"]}/100)'

    breakdown = result["score_breakdown"]

    text = f"""
══════════════════════════════

🤖 <b>TradeMind AI PRO</b>

🪙 <b>{symbol}/USD</b>

<b>{result["trade_grade"]}</b>

━━━━━━━━━━━━━━━━━━━━━━

🧠 <b>AI Score</b>

{result["score"]} / 100

🎯 <b>Probability</b>

{result["confidence"]}%

━━━━━━━━━━━━━━━━━━━━━━

🌍 <b>Market Regime</b>

{result["market_regime"]}

━━━━━━━━━━━━━━━━━━━━━━

⏱ <b>Multi-Timeframe</b>

15m  {tf_line("15m")}

1H   {tf_line("1H")}

4H   {tf_line("4H")}

1D   {tf_line("1D")}

━━━━━━━━━━━━━━━━━━━━━━

📈 <b>Trade Decision</b>

{result["recommendation"]}

{result.get("reason", "")}

━━━━━━━━━━━━━━━━━━━━━━

💵 <b>Entry</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'${result["entry"]:,.2f}'}

🛑 <b>Stop Loss</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'${result["stop_loss"]:,.2f}'}

🥇 <b>TP1</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'${result["tp1"]:,.2f}'}

🥈 <b>TP2</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'${result["tp2"]:,.2f}'}

🥉 <b>TP3</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'${result["tp3"]:,.2f}'}

━━━━━━━━━━━━━━━━━━━━━━

📊 <b>Risk / Reward</b>

{"N/A" if result["direction"] == "🤝 WAIT" else f'1 : {result["risk_reward"]}'}

⚠️ <b>Risk Level</b>

{result["risk_level"]}

━━━━━━━━━━━━━━━━━━━━━━

📈 <b>AI Breakdown</b>

Trend ............. {breakdown["trend"]}

Momentum ...... {breakdown["momentum"]}

Volume .......... {breakdown["volume"]}

Volatility ...... {breakdown["volatility"]}

Structure ...... {breakdown["structure"]}

Support ......... {breakdown["support"]}

Risk ............... {breakdown["risk"]}

━━━━━━━━━━━━━━━━━━━━━━

📋 <b>Reasons</b>

{"".join(f"• {r}\n" for r in result["reasons"][:5])}

━━━━━━━━━━━━━━━━━━━━━━

🚀 <b>Powered by TradeMind AI Pro v6</b>
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML
    )