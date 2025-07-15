from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (for frontend on different port)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check if JSON contains 'features'
    if not data or 'features' not in data:
        return jsonify({'error': 'JSON body must contain a "features" key.'}), 400

    features = data['features']

    # Validate feature length
    if len(features) != 3:
        return jsonify({'error': 'Exactly 3 features required: [Age, Annual Income, Spending Score]'}), 400

    # Convert to numpy array and reshape
    input_array = np.array(features).reshape(1, -1)

    # Predict cluster
    cluster = model.predict(input_array)

    return jsonify({'cluster': int(cluster[0])})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
