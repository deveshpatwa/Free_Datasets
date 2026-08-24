import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sklearn lib
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report

mnist = fetch_openml("mnist_784",version=1)
x,y = mnist['data'],mnist['target']

x
y

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

model = SGDClassifier()

model.fit(xtrain,ytrain)

prediction = model.predict(xtest)

accuracy_score(prediction,ytest)

print(classification_report(prediction,ytest))

