# import data analysis libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


df = pd.read_csv("titanic.csv")
df.info()
df.head()
df.describe()
df.columns

df = df.drop(columns=['PassengerId','Name','Ticket','Embarked'])

x = df.drop(columns='Survived')
y = df['Survived']

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)



model = RandomForestClassifier()

model.fit(xtrain,ytrain)

prediction = model.predict(xtest)
accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))


