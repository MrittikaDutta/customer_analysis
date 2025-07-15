from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

cluster_info = {
    0: "Young, high-spending customers",
    1: "Older, low-spending customers",
    2: "Average income and spending",
    3: "Wealthy but low-spending customers",
    4: "Low income but high spending",
    5: "Other segment"
}

@app.route("/")
def home():
    return "Customer Segmentation API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = data.get("features")
    
    if features is None:
        return jsonify({"error": "Missing 'features' in request."}), 400

    input_array = np.array(features).reshape(1, -1)
    cluster = int(model.predict(input_array)[0])
    description = cluster_info.get(cluster, "Unknown cluster")

    return jsonify({
        "cluster": cluster,
        "description": description
    })

if __name__ == "__main__":
    app.run(debug=True)
