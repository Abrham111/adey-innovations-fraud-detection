# Fraud Detection EDA

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

## **Data Analysis and Preprocessing**

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

---

## **Running the Notebook**

1. Clone the repository:
  ```bash
  git clone https://github.com/Abrham111/adey-innovations-fraud-detection.git
  cd adey-innovations-fraud-detection
  ```

2. Run the Jupyter Notebook:
  ```bash
  jupyter notebook
  ```

3. Open the notebook file and follow the instructions in each cell.

---

## **Results and Findings**
- Data preprocessing improved data quality and enriched it with geolocation and time-based features.
- Exploratory data analysis revealed some patterns relevant for further analysis.

---