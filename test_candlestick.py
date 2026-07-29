from app.services.market import market
from app.ai.candlestick.engine import candlestick_engine
from app.ai.candlestick.scorer import candlestick_scorer

df = market.get_history("BTC")

patterns = candlestick_engine.analyze(df)
score = candlestick_scorer.score(patterns)

print("\n========== CANDLESTICK ENGINE ==========\n")

for k, v in patterns.items():
    print(f"{k:30} {v}")

print("\n========== SCORE ==========\n")

for k, v in score.items():
    print(f"{k:30} {v}")
