import pandas as pd

def calculate_features(data):
    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data = data.dropna()
    return data

def save_features(data, filename):
    data.to_csv(filename)

if __name__ == "__main__":
    data = pd.read_csv('data/pm_data.csv', index_col=0)
    data = calculate_features(data)
    save_features(data, 'data/pm_data_with_features.csv')

