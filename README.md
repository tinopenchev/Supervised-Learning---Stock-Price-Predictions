# Stock Closing Price Prediction

This repository contains code for predicting stock closing prices using machine learning models and visualizing trading decisions.

## Structure

- `data/`: Scripts to fetch and save stock data.
  - `fetch_data.py`: Fetches historical stock data and saves it to a CSV file.
- `features/`: Scripts to calculate and save features for the models.
  - `calculate_features.py`: Calculates moving averages and other features.
- `models/`: Scripts to train and save models, as well as make predictions.
  - `train_model.py`: Trains the machine learning models and saves them.
  - `predict_model.py`: Loads the trained models and makes predictions.
- `trading/`: Scripts to implement trading logic and visualize trading decisions.
  - `trading_decision.py`: Makes trading decisions based on model predictions.
  - `trading_visualization.py`: Visualizes trading decisions.
- `api/`: Scripts to create a Flask API for making predictions.
  - `app.py`: Flask API to serve predictions from the trained model.
- `main.py`: Main script to run the entire pipeline.
- `requirements.txt`: List of dependencies required to run the project.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/tinopenchev/Supervised-Learning---Stock-Price-Predictions.git
   cd Supervised-Learning---Stock-Price-Predictions
# Supervised-Learning---Stock-Price-Predictions
