import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree

df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\titanic.csv")
df.head()

df.info()

df.describe().round(2)

df.isnull().sum()

# keep usefull columns
df.columns
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
       'Parch','Fare', 'Cabin', 'Embarked']]

df.head()
# rename columns in all lower
df = df.rename(columns={i:i.lower() for i in df.columns})
x = df.drop(columns="survived")
y = df['survived']


# Decision Trees do not require feature scaling.
# Decision Trees do need encoding if your dataset contains categorical (text) features.
# you need to remove null values only