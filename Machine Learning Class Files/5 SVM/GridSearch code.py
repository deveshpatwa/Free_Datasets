# grid search code
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load Titanic dataset
df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\titanic.csv")

# Drop unused columns
df = df.drop(columns=['Name', 'Ticket', 'Cabin', 'PassengerId'])

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Features and target
X = df.drop(columns='Survived')
y = df['Survived']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Categorical and numerical feature lists
cat_features = X.select_dtypes(include='object').columns
num_features = X.select_dtypes(exclude='object').columns

# Preprocessing transformer
transformer = ColumnTransformer(
    [
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features),
        ('num', StandardScaler(), num_features)
    ]
)

# Pipeline with preprocessing and SVC
pipe = Pipeline(
    [
        ('transformer', transformer),
        ('svc', SVC())
    ]
)

# Grid search parameter grid
param_grid = {
    'svc__kernel': ['linear', 'poly', 'rbf'],
    'svc__C': [0.1, 1, 5, 10],
    'svc__gamma': ['scale', 'auto'],
    'svc__degree': [2,3, 4]  # only used for poly kernel
}

grid = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

# Fit grid search
grid.fit(X_train, y_train)

# Best parameters
print("Best params:", grid.best_params_)
print("Best cross-val score:", grid.best_score_)

# Evaluate on test set
y_pred = grid.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))