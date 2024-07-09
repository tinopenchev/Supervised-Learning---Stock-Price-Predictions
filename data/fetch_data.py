import yfinance as yf
import pandas as pd

def fetch_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def save_data(data, filename):
    data.to_csv(filename)

if __name__ == "__main__":
    ticker = 'PM'
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    data = fetch_data(ticker, start_date, end_date)
    save_data(data, 'data/pm_data.csv')
