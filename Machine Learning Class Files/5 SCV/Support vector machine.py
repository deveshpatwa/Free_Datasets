# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import necessary libraries for machine learning
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.compose import ColumnTransformer

# SVC on iris data
# Load the iris dataset
df = sns.load_dataset('iris')

df.head()
df.sample(10)
df.info()
df.describe().round(2)

# split the data into features and target variable
x,y = df.drop(columns='species'), df['species']
x
y

# Visualize the data
# sns.pairplot(df, hue='species', palette='coolwarm')
# plt.show()


# train test split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)


# Create a pipeline with StandardScaler and SVC
pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])

# Fit the pipeline to the training data
pipe.fit(xtrain, ytrain)

# Make predictions on the test data
prediction = pipe.predict(xtest)

# Evaluate the model
accuracy_score(ytest, prediction)

# classification report
print(classification_report(ytest,prediction))










# SVM on titanic dataset
df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\titanic.csv")

# 
df.head()
df = df.drop(columns=['Name', 'Ticket', 'Cabin', 'PassengerId'])
df.head()
df.info()

# data cleaning
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# split the data into features and target variable
x = df.drop(columns='Survived')
y = df['Survived']

# column transformer for categorical and numerical features
cat = x.select_dtypes(include='object').columns
num = x.select_dtypes(exclude='object').columns
cat
num


# train test split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)


# column transformer for categorical and numerical features
transformer = ColumnTransformer(
    [
        ('cat', OneHotEncoder(), cat),
        ('num', StandardScaler(), num)
    ]
)


# use kernal_trick {liner | poly | rbf } with degree = 3 and C = {5,1}
pipe = Pipeline(
    [
        ("transformer", transformer),
        ("svc", SVC(kernel='rbf',degree=3, C=1))   
    ]
)

pipe.fit(xtrain, ytrain)
prediction =  pipe.predict(xtest)
accuracy_score(ytest, prediction)
print(classification_report(ytest, prediction))









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
    'svc__degree': [3, 4]  # only used for poly kernel
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