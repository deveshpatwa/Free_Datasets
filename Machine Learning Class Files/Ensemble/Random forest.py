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
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier


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


model = RandomForestClassifier(n_estimators=200)

pipe = Pipeline(
    [
        ("preprocessor",preprocessor),
        ("model",model)
    ]
)

pipe.fit(xtrain,ytrain)
predictions = pipe.predict(xtest)

accuracy_score(ytest,predictions)
print(classification_report(ytest,predictions))