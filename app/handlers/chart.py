from telegram import Update
from telegram.ext import ContextTypes

from app.services.market import market
from app.services.analyzer import analyzer
from app.charts.chart import create_chart


async def chart(update: Update, context: ContextTypes.DEFAULT_TYPE):

    print("✅ /chart command received")

    # -----------------------------
    # Validate arguments
    # -----------------------------

    if len(context.args) == 0:

        await update.message.reply_text(
            "Usage:\n/chart BTC"
        )

        return

    symbol = context.args[0].upper()

    # -----------------------------
    # Get market data
    # -----------------------------

    df = market.get_history(symbol)

    if df is None:

        await update.message.reply_text(
            "❌ Symbol not found."
        )

        return

    # -----------------------------
    # Analyze
    # -----------------------------

    result = analyzer.analyze_dataframe(
        symbol,
        df,
    )

    # -----------------------------
    # Generate chart
    # -----------------------------

    image = create_chart(
        symbol,
        df,
        result,
    )

    # -----------------------------
    # Send chart
    # -----------------------------

    with open(image, "rb") as photo:

        if result["trade_allowed"]:

            caption = f"""
📈 <b>{symbol}/USD</b>

{result["recommendation"]}

🟢 Entry: ${result["entry"]:,.2f}

🔴 Stop Loss: ${result["stop_loss"]:,.2f}

🎯 TP1: ${result["tp1"]:,.2f}

🎯 TP2: ${result["tp2"]:,.2f}

🎯 TP3: ${result["tp3"]:,.2f}

📊 AI Score: {result["score"]}/100

🎯 Confidence: {result["confidence"]}%
"""

        else:

            caption = f"""
📈 <b>{symbol}/USD</b>

🤝 WAIT

No high-probability setup detected.

📊 AI Score: {result["score"]}/100

🎯 Confidence: {result["confidence"]}%

Reason:

{result["reason"]}
"""

        await update.message.reply_photo(
            photo=photo,
            caption=caption,
            parse_mode="HTML",
        )