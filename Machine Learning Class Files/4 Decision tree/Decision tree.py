import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree
from sklearn import datasets

df = datasets.load_iris()

x = df['data']
x
y = df['target']
y

# train test split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state=42,test_size=0.2)

model = DecisionTreeClassifier()

model.fit(xtrain,ytrain)

train_prediction = model.predict(xtrain)
test_prediction = model.predict(xtest)

accuracy_score(ytrain,train_prediction)
accuracy_score(ytest,test_prediction)

print(classification_report(ytrain,train_prediction))
print(classification_report(ytest,test_prediction))