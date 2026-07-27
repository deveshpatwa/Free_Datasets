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

df=  pd.read_csv("Titanic-Dataset.csv")
df.head()


# column info

# | PassengerId | A unique ID assigned to each passenger. It has no effect on survival and is mainly used for identification.                    | `1`, `892`                                               |
# | Survived    | Whether the passenger survived the disaster. This is the target variable in ML.                                            | `0 = No`, `1 = Yes`                                      |
# | Pclass      | Passenger class (ticket class). It indicates the socioeconomic status of the passenger.                                        | `1 = First Class`, `2 = Second Class`, `3 = Third Class` |
# | Name        | Full name of the passenger, often including title (Mr., Mrs., Miss., etc.).                                                    | `Braund, Mr. Owen Harris`                                |
# | Sex         | Gender of the passenger.                                                                                                       | `male`, `female`                                         |
# | Age         | Age of the passenger in years. Some values are missing.                                                                        | `22`, `38`, `NaN`                                        |
# | SibSp       | Number of siblings and spouses aboard the Titanic.                                                                         | `1` means one sibling or spouse was traveling with them. |
# | Parch       | Number of parents and children aboard the Titanic.                                                                         | `2` means two parents/children were traveling with them. |
# | Ticket      | Ticket number assigned to the passenger. It is usually treated as a categorical feature or dropped because of high uniqueness. | `A/5 21171`                                              |
# | Fare        | The ticket price paid by the passenger.                                                                                        | `7.25`, `71.2833`                                        |
# | Cabin       | Cabin number where the passenger stayed. Many values are missing because not every passenger had an assigned cabin.            | `C85`, `B28`, `NaN`                                      |
# | Embarked    | Port where the passenger boarded the Titanic.                                                                                  | `C`, `Q`, `S`                                            |



# remove unusefull columns
df = df.drop(columns=['PassengerId','Name','Ticket'])

df.head()

df.info()

df.isnull().sum()

# data cleaning and feature engineering 

# age has null values
df.Age.describe()
df['Age'] = df['Age'].fillna(df.Age.median())


# filling cabin column with only its initials 
df.head()
df.Cabin.value_counts()
df['Cabin'] = df['Cabin'].astype(str)
df['Cabin'] = df['Cabin'].apply(lambda x : x[0])

df.head()
df.info()

# Embarked column as some values null fix those
df['Embarked'].value_counts()
df['Embarked'] = df['Embarked'].fillna("S")

# ------------check sigmoid function----------
# logistic sigmoid function

# def sigmoid(x):
#     e = 2.178
#     y = 1/ (1+(e**-x))
#     return round(y,2)

# plt.plot([sigmoid(i) for i in list(range(-10,10))] )
# plt.show()

# -----------------------------------------

df.head()

x = df.drop(columns="Survived")
y = df['Survived']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=42)

cat = x.select_dtypes("object").columns
num = x.select_dtypes(np.number).columns

preprocessor = ColumnTransformer( [ ("cat",OneHotEncoder(),cat),("num",StandardScaler(),num)] )

model = LogisticRegression()

pipe = Pipeline([("preprocessor",preprocessor),("model",model)])


pipe.fit(xtrain,ytrain)

prediction = pipe.predict(xtest)

accuracy_score(ytest,prediction)
confusion_matrix(ytest,prediction)
print(classification_report(ytest,prediction))

# making ROC and AUC curve
prediction_probability = pipe.predict_proba(xtest)[:,1]
prediction_probability

fpr,tpr,threshhold = roc_curve(ytest,prediction_probability)
auc = roc_auc_score(ytest,prediction)


# plot ROC-AUC curve
plt.plot(fpr, tpr, linewidth=2, label=f"AUC = {auc:.2f}")
plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()