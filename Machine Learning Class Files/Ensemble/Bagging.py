# import imp library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import machine learning library
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import BaggingClassifier


df =  pd.read_csv("titanic_cleaned.csv")
df.head()

x = df.drop(columns="Survived")
y = df['Survived']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

cat = x.select_dtypes(str).columns
num = x.select_dtypes(np.number).columns

preprocessor = ColumnTransformer(
     [
         ("cat",OneHotEncoder(),cat),
         ("num",StandardScaler(),num)
    ] 
)

# Define the base estimator
base_tree = DecisionTreeClassifier()

# Create and train the Bagging Classifier
model = BaggingClassifier(
    estimator=base_tree,
    n_estimators=200,       # Number of base trees
    max_samples=0.2,       # Train each tree on 80% of data
    oob_score=False,        # Use Out-of-Bag samples for validation (dataset with replacement)
    random_state=42,
    n_jobs=-1,
    bootstrap=False            # Use all CPU cores (parallel training)
)


pipe = Pipeline(
    [
        ("preprocessor",preprocessor),
        ("voting",model)
    ]
)

pipe.fit(xtrain,ytrain)
predictions = pipe.predict(xtest)

accuracy_score(ytest,predictions)
print(classification_report(ytest,predictions))