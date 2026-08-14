# import data analysis libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


# loading the data
df = pd.read_csv("titanic.csv")

# check info
df.info()
df.head()
df.describe()
df.columns

# remove columns which we dont need
df = df.drop(columns=['PassengerId','Name','Ticket'])


# data cleaning and feature engineering 
# age has null values
df.Age.describe()
df['Age'] = df['Age'].fillna(df.Age.median())


# filling cabin column with only its initials 
df.head()
df.Cabin.value_counts()
df['Cabin'] = df['Cabin'].astype(str)
df['Cabin'] = df['Cabin'].fillna("Na")
df['Cabin'] = df['Cabin'].apply(lambda x : x[0])


df.head()
df.info()

# Embarked column as some values null fix those
df['Embarked'].value_counts()
df['Embarked'] = df['Embarked'].fillna("S")

df.info()


x = df.drop(columns="Survived")
y = df['Survived']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

cat = x.select_dtypes("object").columns
num = x.select_dtypes(np.number).columns

preprocessor = ColumnTransformer( [ ("cat",OneHotEncoder(handle_unknown="ignore"),cat)] )

model = RandomForestClassifier(n_estimators=200)

pipe = Pipeline([("preprocessor",preprocessor),("model",model)])


pipe.fit(xtrain,ytrain)

prediction = pipe.predict(xtest)

accuracy_score(ytest,prediction)
confusion_matrix(ytest,prediction)
print(classification_report(ytest,prediction))
