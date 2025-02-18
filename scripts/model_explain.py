import shap
import lime
import lime.lime_tabular
import numpy as np
import matplotlib.pyplot as plt

def explain_model(model, X_train, X_test, feature_names):
  # SHAP Explanation
  explainer = shap.Explainer(model, X_train)
  shap_values = explainer(X_test)
  
  print("\nSHAP Summary Plot:")
  shap.summary_plot(shap_values, X_test, feature_names=feature_names)
  
  # LIME Explanation (single instance)
  lime_explainer = lime.lime_tabular.LimeTabularExplainer(
    X_train, feature_names=feature_names, class_names=['Negative', 'Positive'], discretize_continuous=True
  )
  
  sample_idx = np.random.randint(0, len(X_test))  # Pick a random test sample
  sample_instance = X_test[sample_idx].reshape(1, -1)
  
  print(f"\nLIME Explanation for instance {sample_idx}:")
  exp = lime_explainer.explain_instance(sample_instance[0], model.predict_proba)
  exp.show_in_notebook()
  exp.as_pyplot_figure()
  plt.show()
