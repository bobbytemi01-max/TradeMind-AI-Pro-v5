from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from app.services.market import market
from app.services.analyzer import analyzer
from app.chart.chart_engine import chart_engine


async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/chart BTC"
        )
        return

    symbol = context.args[0].upper()

    df = market.get_history(symbol)

    if df is None or df.empty:
        await update.message.reply_text("❌ Symbol not found.")
        return

    analysis = analyzer.analyze_dataframe(symbol, df)

    image = chart_engine.create(
        df,
        symbol,
        analysis,
    )

    caption = f"""
📈 <b>{symbol}/USD</b>

🚀 <b>{analysis['final_signal']}</b>

🎯 Probability: {analysis['probability']}%

🎯 Confidence: {analysis['confidence_v2']}%
({analysis['trade_grade_v2']})

🏦 Institutional:
{analysis['institutional_bias']}

📍 Zone:
{analysis['premium_discount']}

━━━━━━━━━━━━━━━━━━

🟢 Entry
${analysis['entry']:,.2f}

🔴 Stop Loss
${analysis['stop_loss']:,.2f}

🎯 TP1
${analysis['tp1']:,.2f}

🎯 TP2
${analysis['tp2']:,.2f}

🎯 TP3
${analysis['tp3']:,.2f}

━━━━━━━━━━━━━━━━━━

⚡ Execution

{analysis['execution_status']}
"""

    with open(image, "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            parse_mode=ParseMode.HTML,
        )
