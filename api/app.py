from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('models/linear_regression_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = [data['MA10'], data['MA50'], data['Volume']]
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

