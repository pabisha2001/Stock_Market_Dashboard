import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def load_data_from_db(db_path='stock_data.db'):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM stocks", conn)
    conn.close()
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df


def plot_current_prices(df):
    plt.figure(figsize=(8, 5))
    plt.bar(df['symbol'], df['price'], color='skyblue')

    plt.title("Current Stock Prices")
    plt.xlabel("Stock Symbol")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.savefig('data/current_prices.png')
    plt.show()


def main():
    df = load_data_from_db()
    plot_current_prices(df)


if __name__ == "__main__":
    main()
