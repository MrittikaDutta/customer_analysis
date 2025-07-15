from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained KMeans model
model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check if 'features' key exists
    if 'features' not in data:
        return jsonify({'error': 'JSON body must contain a "features" key.'}), 400

    features = data['features']

    # Ensure we have exactly 3 features
    if len(features) != 3:
        return jsonify({'error': 'Exactly 3 features required: [Age, Annual Income, Spending Score]'}), 400

    # Convert to numpy array
    input_array = np.array(features).reshape(1, -1)

    # Predict cluster label
    cluster = model.predict(input_array)

    # Convert numpy int to Python int for JSON serialization
    cluster_label = int(cluster[0])

    return jsonify({'cluster': cluster_label})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
