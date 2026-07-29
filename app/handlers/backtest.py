from telegram import Update
from telegram.ext import ContextTypes

from app.ai.learning.trade_logger import trade_logger
from app.backtest.backtest_engine import backtest_engine


async def backtest(update: Update, context: ContextTypes.DEFAULT_TYPE):

    trades = trade_logger.load()

    result = backtest_engine.run(trades)

    text = f"""
📊 <b>TradeMind AI Backtest</b>

━━━━━━━━━━━━━━━━━━

Total Trades

{result['trades']}

Wins

{result['wins']}

Losses

{result['losses']}

━━━━━━━━━━━━━━━━━━

Win Rate

{result['win_rate']}%

━━━━━━━━━━━━━━━━━━

Recommendation

{"✅ Strategy is profitable." if result["win_rate"] >= 60 else "⚠️ More data required."}
"""

    await update.message.reply_text(
        text,
        parse_mode="HTML",
    )
