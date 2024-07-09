import pandas as pd
import matplotlib.pyplot as plt

def plot_trading_decisions(data, ticker):
    colors = {'BUY': 'green', 'SELL': 'red', 'HOLD': 'blue'}
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Close'], label='Close Price', color='black')
    plt.plot(data.index, data['MA10'], label='MA10', color='orange')
    plt.plot(data.index, data['MA50'], label='MA50', color='purple')

    for i in range(len(data)):
        if data['Decision'].iloc[i] == "BUY":
            plt.scatter(data.index[i], data['Close'].iloc[i], color='green', label='BUY', marker='^', alpha=1)
        elif data['Decision'].iloc[i] == "SELL":
            plt.scatter(data.index[i], data['Close'].iloc[i], color='red', label='SELL', marker='v', alpha=1)

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.title(f"Trading Visualization for {ticker}")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    ticker = 'PM'
    data = pd.read_csv('data/pm_data_with_trading_decisions.csv', index_col=0)
    plot_trading_decisions(data, ticker)

