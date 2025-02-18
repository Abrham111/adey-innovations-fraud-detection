from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("../data/Fraud_Data.csv")

# API Endpoint: Summary statistics
@app.route("/api/summary", methods=["GET"])
def get_summary():
  total_transactions = len(df)
  total_fraud_cases = df[df["class"] == 1].shape[0]
  fraud_percentage = round((total_fraud_cases / total_transactions) * 100, 2)

  summary = {
    "total_transactions": total_transactions,
    "total_fraud_cases": total_fraud_cases,
    "fraud_percentage": fraud_percentage,
  }
  return jsonify(summary)

# API Endpoint: Fraud cases over time
@app.route("/api/fraud_trends", methods=["GET"])
def get_fraud_trends():
  df["purchase_time"] = pd.to_datetime(df["purchase_time"])
  fraud_trends = df[df["class"] == 1].groupby(df["purchase_time"].dt.to_period("M"))["class"].count()
  fraud_trends.index = fraud_trends.index.astype(str)  # Convert PeriodIndex to string for JSON serialization
  return jsonify(fraud_trends.to_dict())

# API Endpoint: Fraud data by browser and source
@app.route("/api/fraud_browser_source", methods=["GET"])
def fraud_by_browser_source():
  """
  Returns fraud cases grouped by browser and source as JSON.
  """

  # Filter only fraudulent transactions
  fraud_df = df[df['class'] == 1]

  # Group by Browser
  browser_counts = fraud_df.groupby('browser')['class'].count().reset_index()
  browser_counts.columns = ['browser', 'fraud_cases']

  # Group by Source
  source_counts = fraud_df.groupby('source')['class'].count().reset_index()
  source_counts.columns = ['source', 'fraud_cases']

  # Convert to JSON response
  response = {
    "browser_fraud": browser_counts.to_dict(orient="records"),
    "source_fraud": source_counts.to_dict(orient="records")
  }

  return jsonify(response)

if __name__ == "__main__":
  app.run(debug=True, port=5001)
