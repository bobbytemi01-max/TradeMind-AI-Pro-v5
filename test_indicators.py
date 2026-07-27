from app.services.market import market
from app.services.indicators import indicator_service

# Get market history
df = market.get_history("BTC")

# Calculate indicators
data = indicator_service.calculate(df)

print("Price :", data["price"])
print("ADX   :", data["adx"])
print("VWAP  :", data["vwap"])