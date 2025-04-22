import requests
import json
from datetime import datetime

# Load API key from config file
with open('config.json') as f:
    config = json.load(f)

API_KEY = config['api_key']
symbols = ['AAPL', 'MSFT', 'TSLA']


def fetch_stock_data(symbol):
    url = f'https://api.twelvedata.com/price?symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if 'price' in data:
        return {
            'symbol': symbol,
            'price': float(data['price']),
            'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    else:
        print(f"Error fetching {symbol}: {data}")
        return None


def main():
    stock_data = []
    for symbol in symbols:
        result = fetch_stock_data(symbol)
        if result:
            print(result)
            stock_data.append(result)

    # Optional: Save to a JSON file for now
    with open('data/stock_data.json', 'w') as f:
        json.dump(stock_data, f, indent=4)


if __name__ == '__main__':
    main()
