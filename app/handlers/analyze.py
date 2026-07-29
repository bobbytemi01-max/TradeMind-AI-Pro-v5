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

    reasons = []

    reasons.extend(result.get("institutional_reasons", []))
    reasons.extend(result.get("candlestick_reasons", []))
    reasons.extend(result.get("fusion_reasons", []))

    reasons = list(dict.fromkeys(reasons))

    tf = result.get("multi_timeframe", {})

    def icon(name):
        if name not in tf:
            return "⚪"

        bias = tf[name]["institutional"]

        if "BULLISH" in bias:
            return "🟢"

        if "BEARISH" in bias:
            return "🔴"

        return "⚪"

    text = f"""
🤖 <b>TradeMind AI PRO v7</b>

🪙 <b>{symbol}/USD</b>

━━━━━━━━━━━━━━━━━━

🚀 <b>Final Signal</b>

{result.get("final_signal","WAIT")}

🎯 <b>Confidence</b>

{result.get("confidence_v2",0)}%
({result.get("trade_grade_v2","-")})

━━━━━━━━━━━━━━━━━━

🏦 <b>Institutional</b>

{result.get("institutional_bias")}
({result.get("institutional_score")})

🕯️ <b>Candlestick</b>

{result.get("candlestick_bias")}
({result.get("candlestick_score")})

━━━━━━━━━━━━━━━━━━

💼 <b>Trade Setup</b>

Entry      : ${result.get("entry",0):,.2f}
Stop Loss  : ${result.get("stop_loss",0):,.2f}

TP1        : ${result.get("tp1",0):,.2f}
TP2        : ${result.get("tp2",0):,.2f}
TP3        : ${result.get("tp3",0):,.2f}

Risk/Reward : {result.get("risk_reward",0)} : 1

━━━━━━━━━━━━━━━━━━

🎯 <b>Execution</b>

Probability : {result.get("probability",0)}%

Rating      : {result.get("probability_rating","-")}

Confluence  : {result.get("confluence_score",0)}

Session     : {result.get("session","UNKNOWN")}

Status

{result.get("execution_status","WAIT")}

━━━━━━━━━━━━━━━━━━

🌍 <b>Multi-Timeframe</b>

15m {icon("15m")}
1H  {icon("1h")}
4H  {icon("4h")}
1D  {icon("1d")}

Agreement: {tf.get("agreement",0)}/4

━━━━━━━━━━━━━━━━━━

📊 <b>Market Structure</b>

Bias

{result.get("institutional_bias")}
({result.get("institutional_score")})

Zone

{result.get("premium_discount")}

━━━━━━━━━━━━━━━━━━

BOS              {"✅" if result.get("bos") else "❌"}
CHoCH            {"✅" if result.get("choch") else "❌"}
Fair Value Gap   {"✅" if result.get("fvg") else "❌"}
Order Block      {"✅" if result.get("order_block") else "❌"}

━━━━━━━━━━━━━━━━━━

Equal Highs

{"✅ " + str(result.get("equal_high_level")) if result.get("equal_highs") else "❌"}

Equal Lows

{"✅ " + str(result.get("equal_low_level")) if result.get("equal_lows") else "❌"}

━━━━━━━━━━━━━━━━━━

Nearest Liquidity

{result.get("nearest_liquidity", {}).get("type","NONE")}

Level

{result.get("nearest_liquidity", {}).get("level","-")}

━━━━━━━━━━━━━━━━━━

📝 <b>Reasons</b>

{"".join(f"• {r}\n" for r in reasons)}

━━━━━━━━━━━━━━━━━━

🚀 <b>TradeMind AI Pro v7</b>
"""

    await update.message.reply_text(
        text,
        parse_mode=ParseMode.HTML,
    )
