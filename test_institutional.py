from app.services.market import market
from app.ai.institutional_engine import institutional_engine

df = market.get_history("BTC")

result = institutional_engine.analyze(df)

print("\n========== INSTITUTIONAL ANALYSIS ==========\n")

for k, v in result.items():
    print(f"{k:25} {v}")
