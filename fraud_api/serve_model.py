from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load the trained model
with open('../fraud_api/fraud_detection_model.pkl', 'rb') as model_file:
  model = joblib.load(model_file)

@app.route("/")
def home():
  app.logger.info("Home endpoint was reached")
  return jsonify({"message": "Fraud Detection API is running!"})

# Define an endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()  # Get the input data as JSON
  required_features = [
    "user_id", "signup_time", "purchase_time", "purchase_value", "age",
    "ip_int", "transaction_count", "time_diff", "hour_of_day", "day_of_week",
    "source_Direct", "source_SEO", "browser_FireFox", "browser_IE",
    "browser_Opera", "browser_Safari", "sex_M"
  ]
  
  # Check if all required keys exist
  if not all(key in data for key in required_features):
    app.logger.error("Missing one or more required features in the request")
    return jsonify({'error': 'Missing one or more required features'}), 400

  # Extract feature values in correct order
  features = np.array([data[key] for key in required_features]).reshape(1, -1)

  # Make prediction using the model
  prediction = model.predict(features)
  app.logger.info(f"Prediction made: {prediction}")

  # Log the prediction
  result = 'Fraud' if prediction[0] == 1 else 'Not Fraud'
  app.logger.info(f"Based on the data the user is: {result}")
  
  return jsonify({'prediction': result})

if __name__ == '__main__':
  app.run(debug=True, port=5000)