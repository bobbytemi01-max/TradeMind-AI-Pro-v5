"""
TradeMind AI Pro Scanner
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from app.services.analyzer import analyzer
from app.scanner.universe import CRYPTO_UNIVERSE
from app.scanner.ranking import rank


class MarketScanner:

    def analyze_symbol(self, symbol):

        try:

            print(f"Scanning {symbol}...")

            return analyzer.analyze(symbol)

        except Exception as e:

            print(f"{symbol}: {e}")

            return None

    def scan(self):

        results = []

        # Analyze up to 5 symbols in parallel
        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = {
                executor.submit(
                    self.analyze_symbol,
                    symbol
                ): symbol
                for symbol in CRYPTO_UNIVERSE
            }

            for future in as_completed(futures):

                result = future.result()

                if result is not None:

                    results.append(result)

        return rank(results)


scanner = MarketScanner()