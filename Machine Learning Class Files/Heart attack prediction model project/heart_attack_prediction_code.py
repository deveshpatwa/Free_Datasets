# import imp library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# import machine learning library
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import roc_curve, roc_auc_score

# find the file
os.listdir()

df=  pd.read_csv("data.csv")

df.head()
df.info()
df.isnull().sum()
df.describe().round(2).T


for i in df.columns:
    print(df[i].value_counts())

# data cleaning 
df['BMI'] = df['BMI'].fillna(28)


# EDA
# analysis on BMI
# df.columns
# sns.histplot(data=df,x='BMI',bins=50,kde=True,hue='HeartDiseaseorAttack')
# plt.show()

x = df.drop(columns='HeartDiseaseorAttack')
y = df['HeartDiseaseorAttack']

model = LogisticRegression()

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.05,random_state=42)

model.fit(xtrain,ytrain)
prediction = model.predict(xtest)

accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))



# change probability solution for only testing the data
# Instead of: y_pred = model.predict(X_test)
y_probs = model.predict_proba(xtest)[:, 1]

# Lower threshold to boost recall
custom_threshold = 0.15
y_pred_custom = (y_probs >= custom_threshold).astype(int)
print(classification_report(ytest,y_pred_custom))


# add more data solution for training the data
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
xtrain_res, ytrain_res = smote.fit_resample(xtrain, ytrain)
model.fit(xtrain_res,ytrain_res)
prediction = model.predict(xtest)

accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))