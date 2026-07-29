from telegram import Update
from telegram.ext import ContextTypes

from app.ai.learning.performance import performance_engine
from app.ai.learning.optimizer import strategy_optimizer


async def performance(update: Update, context: ContextTypes.DEFAULT_TYPE):

    stats = performance_engine.summary()
    advice = strategy_optimizer.optimize()

    text = f"""
📊 TradeMind Performance

Completed Trades : {advice.get("completed_trades",0)}
Wins             : {stats["wins"]}
Losses           : {stats["losses"]}
Win Rate         : {stats["win_rate"]}%

Recommendation
{advice["recommendation"]}
"""

    await update.message.reply_text(text)
