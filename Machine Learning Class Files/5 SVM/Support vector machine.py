# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import necessary libraries for machine learning
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report,accuracy_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# SVC on iris data
# Load the iris dataset
df = sns.load_dataset('iris')

df.head()
df.sample(10)
df.info()
df.describe().round(2)

# split the data into features and target variable
x,y = df.drop(columns='species'), df['species']
x
y

sns.scatterplot(data=df, x = "petal_length", y = "petal_width", hue = "species")
plt.show()


# Visualize the data
sns.pairplot(df, hue='species', palette='coolwarm')
plt.show()


# train test split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)


# Create a pipeline with StandardScaler and SVC
pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])

# Fit the pipeline to the training data
pipe.fit(xtrain, ytrain)

# Make predictions on the test data
prediction = pipe.predict(xtest)
train_prediction = pipe.predict(xtrain)

# Evaluate the model
accuracy_score(ytest, prediction)
accuracy_score(ytrain, train_prediction)

# classification report
print(classification_report(ytest,prediction))
print(classification_report(ytrain, train_prediction))









# SVM on titanic dataset
df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\titanic.csv")

# 
df.head()
df = df.drop(columns=['Name', 'Ticket', 'Cabin', 'PassengerId'])
df.head()
df.info()

# data cleaning
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# split the data into features and target variable
x = df.drop(columns='Survived')
y = df['Survived']

# column transformer for categorical and numerical features
cat = x.select_dtypes(include='object').columns
num = x.select_dtypes(exclude='object').columns
cat
num


# train test split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)


# column transformer for categorical and numerical features
transformer = ColumnTransformer(
    [
        ('cat', OneHotEncoder(), cat),
        ('num', StandardScaler(), num)
    ]
)


# use kernal_trick {liner | poly | rbf } with degree = 3 and C = {5,1}
pipe = Pipeline(
    [
        ("transformer", transformer),
        ("svc", SVC())   
    ]
)

pipe.fit(xtrain, ytrain)
prediction =  pipe.predict(xtest)

accuracy_score(ytest, prediction)
print(classification_report(ytest, prediction))