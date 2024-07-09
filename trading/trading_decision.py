import pandas as pd

def trading_decision(predicted_prices, current_prices):
    decisions = []
    for predicted_price, current_price in zip(predicted_prices, current_prices):
        if predicted_price > current_price:
            decisions.append("BUY")
        elif predicted_price < current_price:
            decisions.append("SELL")
        else:
            decisions.append("HOLD")
    return decisions

if __name__ == "__main__":
    data = pd.read_csv('data/pm_data_with_predictions.csv', index_col=0)
    data['Decision'] = trading_decision(data['Predicted_Price'], data['Close'])
    data.to_csv('data/pm_data_with_trading_decisions.csv')

