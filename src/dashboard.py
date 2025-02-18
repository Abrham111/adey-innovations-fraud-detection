import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import requests
import pandas as pd
import plotly.express as px

# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Fetch fraud statistics
summary_data = requests.get("http://127.0.0.1:5001/api/summary").json()
fraud_trends = requests.get("http://127.0.0.1:5001/api/fraud_trends").json()

# Convert fraud trends data to DataFrame
df_fraud_trends = pd.DataFrame(list(fraud_trends.items()), columns=["Date", "Fraud Cases"])

# Layout
app.layout = dbc.Container([
  html.H1("Fraud Detection Dashboard", className="text-center mb-4"),

  # Summary Cards
  dbc.Row([
    dbc.Col(dbc.Card([
      dbc.CardBody([
        html.H5("Total Transactions", className="card-title"),
        html.H2(f"{summary_data['total_transactions']:,}", className="text-primary")
      ])
    ]), width=3),
    
    dbc.Col(dbc.Card([
      dbc.CardBody([
        html.H5("Total Fraud Cases", className="card-title"),
        html.H2(f"{summary_data['total_fraud_cases']:,}", className="text-danger")
      ])
    ]), width=3),
    
    dbc.Col(dbc.Card([
      dbc.CardBody([
        html.H5("Fraud Percentage", className="card-title"),
        html.H2(f"{summary_data['fraud_percentage']}%", className="text-warning")
      ])
    ]), width=3),
  ], className="mb-4"),

  # Tabs for Visualization
  dcc.Tabs([
    dcc.Tab(label="Fraud Trends", children=[
      dcc.Graph(id="fraud-trends-chart",
            figure=px.line(df_fraud_trends, x="Date", y="Fraud Cases",
                   title="Fraud Cases Over Time",
                   markers=True))
    ]),

    dcc.Tab(label="Fraud by Source & Browser", children=[
      dcc.Graph(id="fraud-source-chart"),
      dcc.Graph(id="fraud-browser-chart"),
      html.Button("Refresh Data", id="refresh-btn", n_clicks=0)
    ]),

    dcc.Tab(label="Fraud Prediction", children=[
      html.Br(),
      dbc.Row([
        dbc.Col(dcc.Input(id="user_id", type="number", placeholder="User ID"), width=4),
        dbc.Col(dcc.Input(id="signup_time", type="text", placeholder="Signup Time"), width=4),
        dbc.Col(dcc.Input(id="purchase_time", type="text", placeholder="Purchase Time"), width=4),
        dbc.Col(dcc.Input(id="purchase_value", type="number", placeholder="Purchase Value"), width=4),
        dbc.Col(dcc.Input(id="age", type="number", placeholder="Age"), width=4),
        dbc.Col(dcc.Input(id="ip_int", type="number", placeholder="IP Address (Integer)"), width=4),
        dbc.Col(dcc.Input(id="transaction_count", type="number", placeholder="Transaction Count"), width=4),
        dbc.Col(dcc.Input(id="time_diff", type="number", placeholder="Time Difference"), width=4),
        dbc.Col(dcc.Input(id="hour_of_day", type="number", placeholder="Hour of Day"), width=4),
        dbc.Col(dcc.Input(id="day_of_week", type="number", placeholder="Day of Week"), width=4),
        dbc.Col(dcc.Input(id="source_Direct", type="number", placeholder="Source Direct (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="source_SEO", type="number", placeholder="Source SEO (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="browser_FireFox", type="number", placeholder="Browser FireFox (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="browser_IE", type="number", placeholder="Browser IE (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="browser_Opera", type="number", placeholder="Browser Opera (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="browser_Safari", type="number", placeholder="Browser Safari (1 or 0)"), width=4),
        dbc.Col(dcc.Input(id="sex_M", type="number", placeholder="Sex M (1 or 0)"), width=4)
      ]),
      html.Br(),
      html.Button("Predict Fraud", id="predict-btn", className="btn btn-primary"),
      html.Br(), html.Br(),
      html.Div(id="prediction-output")
    ])
  ])
], fluid=True)

# Callbacks for browser fraud insights
@app.callback(
  Output("fraud-source-chart", "figure"),
  Output("fraud-browser-chart", "figure"),
  Input("refresh-btn", "n_clicks")
)
def update_fraud_charts(n):
  fraud_data = requests.get("http://127.0.0.1:5001/api/fraud_browser_source").json()

  # Convert response to DataFrame
  df_browser = pd.DataFrame(fraud_data["browser_fraud"])
  df_source = pd.DataFrame(fraud_data["source_fraud"])

  # Plot fraud cases by browser
  fig_browser = px.bar(df_browser, x="browser", y="fraud_cases", title="Fraud Cases by Browser")

  # Plot fraud cases by source
  fig_source = px.bar(df_source, x="source", y="fraud_cases", title="Fraud Cases by Source")

  return fig_browser, fig_source

# Callback for Fraud Prediction
@app.callback(
  Output("prediction-output", "children"),
  Input("predict-btn", "n_clicks"),
  State("user_id", "value"),
  State("signup_time", "value"),
  State("purchase_time", "value"),
  State("purchase_value", "value"),
  State("age", "value"),
  State("ip_int", "value"),
  State("transaction_count", "value"),
  State("time_diff", "value"),
  State("hour_of_day", "value"),
  State("day_of_week", "value"),
  State("source_Direct", "value"),
  State("source_SEO", "value"),
  State("browser_FireFox", "value"),
  State("browser_IE", "value"),
  State("browser_Opera", "value"),
  State("browser_Safari", "value"),
  State("sex_M", "value")
)
def predict_fraud(n_clicks, user_id, signup_time, purchase_time, purchase_value, age, ip_int, transaction_count, time_diff, hour_of_day, day_of_week, source_Direct, source_SEO, browser_FireFox, browser_IE, browser_Opera, browser_Safari, sex_M):
  if n_clicks:
    response = requests.post("http://127.0.0.1:5000/predict", json={
      "user_id": user_id,
      "signup_time": signup_time,
      "purchase_time": purchase_time,
      "purchase_value": purchase_value,
      "age": age,
      "ip_int": ip_int,
      "transaction_count": transaction_count,
      "time_diff": time_diff,
      "hour_of_day": hour_of_day,
      "day_of_week": day_of_week,
      "source_Direct": source_Direct,
      "source_SEO": source_SEO,
      "browser_FireFox": browser_FireFox,
      "browser_IE": browser_IE,
      "browser_Opera": browser_Opera,
      "browser_Safari": browser_Safari,
      "sex_M": sex_M
    }).json()
    prediction_result = "Fraud Detected ⚠️" if response["fraud_prediction"] == "Fraud" else "Legitimate Transaction ✅"
    return html.H4(prediction_result, className="text-danger" if response["fraud_prediction"] else "text-success")

if __name__ == "__main__":
  app.run(debug=True, port=8050)