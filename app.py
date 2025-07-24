from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model and scaler
model = joblib.load('iris_model.joblib')
scaler = joblib.load('scaler.joblib')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('features')
    arr = np.array(data).reshape(1, -1)
    scaled = scaler.transform(arr)
    pred = model.predict(scaled)[0]
    return jsonify({'prediction': int(pred)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
