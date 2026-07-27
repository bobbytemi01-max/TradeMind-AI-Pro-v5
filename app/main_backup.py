"""
TradeMind AI Pro v6
Main Application
"""

from __future__ import annotations

import logging
import traceback

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from telegram.request import HTTPXRequest

from app.config import TELEGRAM_TOKEN

# ==========================
# Import Handlers
# ==========================

from app.handlers.start import start
from app.handlers.watch import watch
from app.handlers.help import help_command
from app.handlers.price import price
from app.handlers.analyze import analyze_command
from app.handlers.signal import signal
from app.handlers.dashboard import dashboard
from app.handlers.chart import chart
from app.handlers.scan import scan

# ==========================
# Logging
# ==========================

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.INFO)

# ==========================
# Global Error Handler
# ==========================


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
):

    print("\n" + "=" * 60)
    print("UNHANDLED ERROR")
    print("=" * 60)

    traceback.print_exception(
        type(context.error),
        context.error,
        context.error.__traceback__,
    )

    print("=" * 60 + "\n")


# ==========================
# Main
# ==========================


def main():

    if not TELEGRAM_TOKEN:
        raise RuntimeError(
            "TELEGRAM_TOKEN is missing in app/config.py"
        )

    # --------------------------
    # Telegram HTTP Settings
    # --------------------------

    request = HTTPXRequest(
        connect_timeout=20,
        read_timeout=60,
        write_timeout=60,
        pool_timeout=20,
    )

    # --------------------------
    # Build Application
    # --------------------------

    app = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .request(request)
        .build()
    )

    # --------------------------
    # Register Commands
    # --------------------------

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("watch", watch))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("analyze", analyze_command))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("dashboard", dashboard))
    app.add_handler(CommandHandler("chart", chart))
    app.add_handler(CommandHandler("scan", scan))

    # --------------------------
    # Error Handler
    # --------------------------

    app.add_error_handler(error_handler)

    # --------------------------
    # Startup Banner
    # --------------------------

    print("\n")
    print("=" * 60)
    print("🚀 TradeMind AI Pro v6")
    print("=" * 60)
    print("Bot : @TradeMindAIV2Bot")
    print("Status : ONLINE")
    print("=" * 60)

    print("Commands")
    print("/start")
    print("/price BTC")
    print("/analyze BTC")
    print("/signal BTC")
    print("/dashboard BTC")
    print("/chart BTC")
    print("/scan")

    print("=" * 60)

    # --------------------------
    # Run
    # --------------------------

    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        close_loop=False,
    )


# ==========================
# Entry Point
# ==========================

if __name__ == "__main__":
    main()