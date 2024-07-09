import joblib
import pandas as pd

def load_model(filename):
    model = joblib.load(filename)
    return model

def predict(model, data):
    predictions = model.predict(data)
    return predictions

if __name__ == "__main__":
    model = load_model('models/linear_regression_model.pkl')
    data = pd.read_csv('data/pm_data_with_features.csv', index_col=0)
    features = ['MA10', 'MA50', 'Volume']
    data['Predicted_Price'] = predict(model, data[features])
    data.to_csv('data/pm_data_with_predictions.csv')

