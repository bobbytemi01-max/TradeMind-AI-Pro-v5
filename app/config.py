import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - exercised when optional dependency is absent.
    def load_dotenv() -> bool:
        return False


load_dotenv()


TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

DATA_SOURCE = os.getenv("DATA_SOURCE", "yfinance")