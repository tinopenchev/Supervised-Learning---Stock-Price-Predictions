import os
from data.fetch_data import fetch_data, save_data
from features.calculate_features import calculate_features, save_features
from models.train_model import train_model, save_model
from models.predict_model import load_model, predict
from trading.trading_decision import trading_decision
from trading.trading_visualization import plot_trading_decisions

# Fetch data
ticker = 'PM'
start_date = "2020-01-01"
end_date = "2023-01-01"
data = fetch_data(ticker, start_date, end_date)
save_data(data, 'data/pm_data.csv')

# Calculate features
data = pd.read_csv('data/pm_data.csv', index_col=0)
data = calculate_features(data)
save_features(data, 'data/pm_data_with_features.csv')

# Train model
data = pd.read_csv('data/pm_data_with_features.csv', index_col=0)
features = ['MA10', 'MA50', 'Volume']
target = 'Close'
X = data[features]
y = data[target]
model = train_model(X, y)
save_model(model, 'models/linear_regression_model.pkl')

# Predict
model = load_model('models/linear_regression_model.pkl')
data['Predicted_Price'] = predict(model, data[features])
data.to_csv('data/pm_data_with_predictions.csv')

# Trading decisions
data['Decision'] = trading_decision(data['Predicted_Price'], data['Close'])
data.to_csv('data/pm_data_with_trading_decisions.csv')

# Plot trading decisions
plot_trading_decisions(data, ticker)

