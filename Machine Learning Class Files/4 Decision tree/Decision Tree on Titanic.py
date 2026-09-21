import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree,export_text
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv("titanic.csv")
df.head()
df.info()

df = df.drop(columns=['PassengerId','Name','Ticket'])


df['Age'] = df['Age'].fillna(df.Age.median())

df.Cabin.value_counts()
df['Cabin'] = df['Cabin'].astype(str)
df['Cabin'] = df['Cabin'].apply(lambda x : str(x)[0])

df['Embarked'].value_counts()
df['Embarked'] = df['Embarked'].fillna("S")

df.info()
df.isnull().sum()

x=  df.drop(columns="Survived")
y = df['Survived']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

cat = x.select_dtypes(str).columns

preprocessor = ColumnTransformer( [ ("cat",OneHotEncoder(),cat)] )

y.value_counts()
model = DecisionTreeClassifier(random_state=42)

pipe = Pipeline([("preprocessor",preprocessor),("model",model)])


pipe.fit(xtrain,ytrain)

prediction = pipe.predict(xtest)
prediction_on_train = pipe.predict(xtrain)

accuracy_score(ytrain,prediction_on_train)
print(classification_report(ytrain,prediction_on_train))

accuracy_score(ytest,prediction)
print(classification_report(ytest,prediction))


# Rough
# using dummy variables in pandas 
df_processed = pd.get_dummies(df,cat)
x = df_processed.drop(columns='Survived')
y = df_processed['Survived']
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(xtrain,ytrain)
prediction = model.predict(xtest)

plot_tree(model,feature_names=xtrain.columns,filled=True)
plt.savefig("model.pdf")

print(export_text(model,feature_names=xtrain.columns))




