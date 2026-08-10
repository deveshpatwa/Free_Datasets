# import data analysis libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score














import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# 1. Load sample dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# 2. Split train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Instantiate and train Random Forest Classifier
rf_model = RandomForestClassifier(
    n_estimators=100,        # Grow 100 trees
    max_features='sqrt',     # Select sqrt(P) features at each split
    oob_score=True,          # Calculate Out-of-Bag score
    random_state=42
)

rf_model.fit(X_train, y_train)

# 4. Predictions and Evaluation
y_pred = rf_model.predict(X_test)

print(f"Test Set Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Out-of-Bag (OOB) Accuracy: {rf_model.oob_score_:.4f}\n")

# 5. Extract Feature Importances
importances = pd.Series(rf_model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("Feature Importances:")
print(importances)