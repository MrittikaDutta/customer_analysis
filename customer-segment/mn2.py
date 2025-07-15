from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Example: Load your model (adjust filename)
# model = joblib.load("your_model.pkl")
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Example: Load your model (adjust filename)
# model = joblib.load("your_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Example: extract features
    features = data['features']
    # prediction = model.predict([features])
    prediction = np.sum(features)   # Dummy example

    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Example: extract features
    features = data['features']
    # prediction = model.predict([features])
    prediction = np.sum(features)   # Dummy example

    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
