from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import mlflow

# Model Training and Evaluation Function
def train_and_evaluate(models, X_train, X_test, y_train, y_test, dataset_name):
  for model_name, model in models.items():
    with mlflow.start_run(run_name=f"{model_name} - {dataset_name}"):
      model.fit(X_train, y_train)
      y_pred = model.predict(X_test)

      # Metrics
      accuracy = accuracy_score(y_test, y_pred)
      precision = precision_score(y_test, y_pred, zero_division=1)
      recall = recall_score(y_test, y_pred, zero_division=1)
      f1 = f1_score(y_test, y_pred)
      roc_auc = roc_auc_score(y_test, y_pred)

      # Log parameters and metrics to MLflow
      mlflow.log_param("model", model_name)
      mlflow.log_param("dataset", dataset_name)
      mlflow.log_metrics({
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
        "roc_auc": roc_auc
      })

      print(f"{model_name} on {dataset_name}: Accuracy={accuracy:.4f}, Precision={precision:.4f}, Recall={recall:.4f}, F1={f1:.4f}, ROC-AUC={roc_auc:.4f}")
