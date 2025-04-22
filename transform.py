import json
import pandas as pd

def load_raw_data(path='data/stock_data.json'):
    with open(path, 'r') as f:
        raw_data = json.load(f)
    return raw_data

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Ensure correct types
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Add extra features (optional)
    df['date'] = df['datetime'].dt.date
    df['time'] = df['datetime'].dt.time
    df['day_of_week'] = df['datetime'].dt.day_name()

    return df

def main():
    raw = load_raw_data()
    cleaned = transform_data(raw)
    print(cleaned)

    # Optional: Save cleaned data to CSV
    cleaned.to_csv('data/cleaned_stock_data.csv', index=False)

if __name__ == "__main__":
    main()
