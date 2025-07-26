from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/")
def home():
    return "Phishing Detector API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        email_text = data.get("email_text", "")

        if not email_text.strip():
            return jsonify({"error": "Empty email text"}), 400

        # Vectorize and predict
        X = vectorizer.transform([email_text])
        prediction = model.predict(X)[0]
        proba = model.predict_proba(X)[0].max()

        result = {
            "label": "Phishing Email" if prediction == 1 else "Safe Email",
            "phishing_score": round(proba * 100, 2)
        }
        return jsonify(result)
    
    except Exception as e:
        print("❌ ERROR:", str(e))  # Print error in terminal
        return jsonify({"error": str(e)}), 500

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)