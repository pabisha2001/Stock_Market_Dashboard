import sqlite3
import pandas as pd

def load_cleaned_data(csv_path='data/cleaned_stock_data.csv'):
    return pd.read_csv(csv_path)

def store_data_to_sqlite(df, db_path='stock_data.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table (if not exists)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            symbol TEXT,
            price REAL,
            datetime TEXT,
            date TEXT,
            time TEXT,
            day_of_week TEXT
        )
    ''')

    # Insert data
    df.to_sql('stocks', conn, if_exists='append', index=False)

    conn.commit()
    conn.close()
    print("✅ Data stored successfully in SQLite!")

def main():
    df = load_cleaned_data()
    store_data_to_sqlite(df)

if __name__ == "__main__":
    main()
