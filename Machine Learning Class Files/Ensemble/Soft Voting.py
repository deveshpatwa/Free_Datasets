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
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.ensemble import VotingClassifier


df=  pd.read_csv("titanic_cleaned.csv")
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

estimators = [
    ("lr",LogisticRegression()),
    ("dt",DecisionTreeClassifier()),
    ("svm",SVC(probability=True))
]

model = VotingClassifier(estimators=estimators,voting="soft")

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