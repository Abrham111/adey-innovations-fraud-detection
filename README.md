# Fraud Detection Project

This project involves detecting fraudulent transactions using three datasets: `Fraud_Data.csv`, `IpAddress_to_Country.csv`, and `creditcard.csv`. The goal is to preprocess the data, perform exploratory data analysis (EDA), engineer relevant features, and build machine learning models for fraud classification.

---

## **Datasets**

1. **Fraud_Data.csv**  
   Contains e-commerce transaction data aimed at identifying fraudulent activities.
   - `user_id`: Unique identifier for the user.
   - `signup_time`: Timestamp when the user signed up.
   - `purchase_time`: Timestamp when the purchase was made.
   - `purchase_value`: Value of the purchase in dollars.
   - `device_id`: Unique identifier for the device used.
   - `source`: Source through which the user came to the site (e.g., SEO, Ads).
   - `browser`: Browser used to make the transaction (e.g., Chrome, Safari).
   - `sex`: Gender of the user (M/F).
   - `age`: Age of the user.
   - `ip_address`: IP address from which the transaction was made.
   - `class`: Target variable (1 = fraudulent, 0 = non-fraudulent).

2. **IpAddress_to_Country.csv**  
   Maps IP addresses to countries.
   - `lower_bound_ip_address`: Lower bound of the IP address range.
   - `upper_bound_ip_address`: Upper bound of the IP address range.
   - `country`: Country corresponding to the IP range.

3. **creditcard.csv**  
   Contains anonymized bank transaction data for fraud detection.
   - `Time`: Seconds elapsed between this transaction and the first transaction in the dataset.
   - `V1` to `V28`: Anonymized features from a PCA transformation.
   - `Amount`: Transaction amount in dollars.
   - `Class`: Target variable (1 = fraudulent, 0 = non-fraudulent).

---

## **Project Structure**
# **Data Analysis and Preprocessing**

1. **Data Preprocessing**
   - Handle missing values.
   - Remove duplicates and correct data types.
   - Normalize and scale numerical features.
   - Encode categorical features.

2. **Exploratory Data Analysis (EDA)**
   - Univariate and bivariate analysis.
   - Identify patterns and anomalies in the data.

3. **Geolocation Analysis**
   - Convert IP addresses to integer format.
   - Merge `Fraud_Data.csv` with `IpAddress_to_Country.csv` to map transactions to countries.

4. **Feature Engineering**
   - Create time-based features (e.g., hour of day, day of week).
   - Calculate transaction frequency and velocity.

---

# **Model Building and Training**

1. **Data Preparation**
   - **Feature and Target Separation:**
     - For `creditcard.csv`: Separate features and target variable **'Class'**.
     - For `Fraud_Data.csv`: Separate features and target variable **'class'**.
   - **Train-Test Split:**
     - Split datasets into training and testing sets to evaluate model performance.

2. **Model Selection**
   - Compare performance using the following models:
     - **Logistic Regression**
     - **Decision Tree**
     - **Random Forest**
     - **Gradient Boosting**
     - **Multi-Layer Perceptron (MLP)**

3. **Model Training and Evaluation**
   - **Train Models:**
     - Train models on both `creditcard.csv` and `Fraud_Data.csv` datasets.
   - **Evaluate Models:**
     - Evaluate models using performance metrics such as:
       - Accuracy
       - Precision
       - Recall
       - F1 Score
       - ROC-AUC

4. **MLOps Steps**
   - **Versioning and Experiment Tracking:**
     - Use tools like **MLflow** to:
       - Track experiments
       - Log parameters
       - Record metrics
       - Manage model versioning


---
# **Model Explainability**

1. **Using SHAP for Explainability**
   - SHAP (Shapley Additive exPlanations) provides a unified measure of feature importance, explaining the contribution of each feature to the model’s predictions.
   - **Installing SHAP**  
     Install SHAP with the following command:
     ```bash
     pip install shap
     ```
   - **Explaining a Model with SHAP**  
     Use SHAP to interpret your fraud detection model’s predictions and understand the importance of each feature.
   - **SHAP Plots**:
     - **Summary Plot**: Provides an overview of the most important features affecting the model’s predictions.
     - **Force Plot**: Visualizes the contribution of each feature for a specific prediction.
     - **Dependence Plot**: Displays the relationship between a feature and the model’s output, helping to identify feature interactions.

2. **Using LIME for Explainability**
   - LIME (Local Interpretable Model-agnostic Explanations) explains individual predictions by approximating the model locally with an interpretable model.
   - **Installing LIME**  
     Install LIME with the following command:
     ```bash
     pip install lime
     ```
   - **Explaining a Model with LIME**  
     Apply LIME to understand individual fraud predictions and how specific features influence the model.
   - **LIME Plots**:
     - **Feature Importance Plot**: Shows the most influential features for a particular prediction, helping to understand the model's decision-making process.

---

# **Model Deployment and API Development**

1. **Setting Up the Flask API**
   - **Create the Flask Application**:
     - Create a new directory for your project.
     - Inside the directory, create a Python script, `serve_model.py`, to serve the fraud detection model using Flask.
     - Create a `requirements.txt` file to list the necessary dependencies, such as Flask and any other libraries.
   - **API Development**:
     - **Define API Endpoints**:  
       Create the necessary API endpoints to receive data, process the model prediction, and return the results.
     - **Test the API**:  
       Test the API to ensure it works as expected by sending sample requests and validating the responses.

2. **Dockerizing the Flask Application**
   - **Create a Dockerfile**:  
     Create a `Dockerfile` to containerize the Flask application for easier deployment.
     ```dockerfile
     # Use an official Python runtime as a parent image
     FROM python:3.13-slim

     # Set the working directory in the container
     WORKDIR /app

     # Copy the current directory contents into the container at /app
     COPY . .

     # Install any needed packages specified in requirements.txt
     RUN pip install --no-cache-dir -r requirements.txt

     # Make port 5000 available to the world outside this container
     EXPOSE 5000

     # Run serve_model.py when the container launches
     CMD ["python", "serve_model.py"]
     ```
   - **Build and Run the Docker Container**:
     - **Build the Docker image**:
       ```bash
       docker build -t fraud_api .
       ```
     - **Run the Docker container**:
       ```bash
       docker run -p 5000:5000 fraud_api
       ```
---
# **Fraud Detection Dashboard**

## **1. Overview**
An **interactive fraud detection dashboard** using **Flask** and **Dash**.  
The Flask backend serves fraud data from a CSV file through API endpoints, while Dash is used to visualize insights.

## **2. Features**
- **Flask API Endpoints**:
  - Serve summary statistics and fraud trends via API.
- **Dash Visualizations**:
  - **Summary Boxes**: Display total transactions, fraud cases, and fraud percentages.
  - **Line Chart**: Shows fraud cases over time.
  - **Fraud by Source & Browser**: Bar chart comparing fraud cases across different sources and browsers.

## **3. Installation**
### **Prerequisites**
Ensure you have **Python 3.13** and install the required dependencies.

### **Step 1: Install Dependencies**
```bash
pip install flask dash pandas plotly
---

## **Requirements**

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

**Required Libraries:**
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- ipaddress
- mlflow
- joblib
- shap
- lime
- flask
- dash

---

## **Running the Notebook**

Clone the repository:
   ```bash
   git clone https://github.com/Abrham111/adey-innovations-fraud-detection.git
   cd adey-innovations-fraud-detection
   ```

## **Author**
- Abrham B.

## **License**
This project is licensed under the MIT License.

---

*Feel free to reach out to me for any question.*

