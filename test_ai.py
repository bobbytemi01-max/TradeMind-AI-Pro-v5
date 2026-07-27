from app.services.analyzer import analyzer
from app.ai.consensus import consensus

data = analyzer.analyze("BTC")

result = consensus.calculate(data)

print("\n========== TradeMind AI Pro v5 ==========\n")

for key, value in result.items():
    print(f"{key}: {value}")