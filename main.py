import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download stock data
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

# Step 2: Look at the data
print(data.head())

# Step 3: Extract closing prices
prices = data["Close"]

# Step 4: Calculate daily returns
returns = prices.pct_change()

# Step 5: Calculate moving averages
ma_5 = prices.rolling(window=5).mean()
ma_10 = prices.rolling(window=10).mean()

# Step 6: Plot everything
plt.figure(figsize=(10,5))
plt.plot(prices, label="Price")
plt.plot(ma_5, label="5-day MA")
plt.plot(ma_10, label="10-day MA")

plt.title("Stock Price and Moving Averages")
plt.legend()
plt.show()
print("\nSummary:")
print("Average daily return:", returns.mean())
print("Volatility:", returns.std())
