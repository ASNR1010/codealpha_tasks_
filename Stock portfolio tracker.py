'''

Features:
1. Add Stock: The user can add a stock symbol and specify how many shares they own.
2. Remove Stock: The user can remove a specific number of shares or entirely remove the stock from their portfolio.
3. Track Performance: The program fetches real-time stock prices using a financial API, calculates the value of the stocks owned, and displays the portfolio's total value.
4. API Integration: The get_stock_price function uses Alpha Vantage's GLOBAL_QUOTE API to fetch current stock prices (you can use another financial data provider like Yahoo Finance or IEX Cloud).

'''

import requests

# Alpha Vantage API setup (Replace with your own API key)
API_KEY = 'your_alpha_vantage_api_key'
BASE_URL = 'https://www.alphavantage.co/query'

def get_stock_price(symbol):
    """Fetches the current price of a stock from the Alpha Vantage API"""
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if 'Global Quote' in data and '05. price' in data['Global Quote']:
            return float(data['Global Quote']['05. price'])
        else:
            print("Invalid stock symbol or no data available.")
    else:
        print("Error fetching data from API.")
    return None

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}  # Store stock symbol and shares owned

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio or update the shares owned"""
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        """Remove a stock or reduce shares in the portfolio"""
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed {symbol} from your portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol}.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def track_performance(self):
        """Track and display the current value of all stocks in the portfolio"""
        total_value = 0
        print("\nYour Portfolio Performance:")
        print("-------------------------------------")
        for symbol, shares in self.portfolio.items():
            price = get_stock_price(symbol)
            if price:
                stock_value = price * shares
                total_value += stock_value
                print(f"{symbol}: {shares} shares @ ${price:.2f} each = ${stock_value:.2f}")
        print("-------------------------------------")
        print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\n--- Stock Portfolio Tracker ---")
        print("1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)

        elif choice == '3':
            portfolio.track_performance()

        elif choice == '4':
            print("Exiting portfolio tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()



'''

API Replacement (for Real-Time Data):
1. Alpha Vantage: You need to register and get an API key from Alpha Vantage here.
2. Yahoo Finance API: You can use the yfinance Python package if you prefer Yahoo Finance data.
3. Install the package: pip install yfinance
4. Replace the get_stock_price function with the yfinance package methods.

With this, the tool can manage a user’s stock portfolio by adding/removing stocks and tracking real-time performance

'''

import yfinance as yf

def get_stock_price(symbol):
    """Fetches the current price of a stock from Yahoo Finance using yfinance"""
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'].iloc[0]
    return price

