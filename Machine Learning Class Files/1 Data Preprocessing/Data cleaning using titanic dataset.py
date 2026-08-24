import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# getting the data and reading it ---------------->
df = pd.read_csv("titanic.csv")
df.head()


# column info

# | PassengerId | A unique ID assigned to each passenger. It has no effect on survival and is mainly used for identification.                    | `1`, `892`                                               |
# | Survived    | Whether the passenger survived the disaster. This is the target variable in ML.                                                | `0 = No`, `1 = Yes`                                      |
# | Pclass      | Passenger class (ticket class). It indicates the socioeconomic status of the passenger.                                        | `1 = First Class`, `2 = Second Class`, `3 = Third Class` |
# | Name        | Full name of the passenger, often including title (Mr., Mrs., Miss., etc.).                                                    | `Braund, Mr. Owen Harris`                                |
# | Sex         | Gender of the passenger.                                                                                                       | `male`, `female`                                         |
# | Age         | Age of the passenger in years. Some values are missing.                                                                        | `22`, `38`, `NaN`                                        |
# | SibSp       | Number of siblings and spouses aboard the Titanic.                                                                             | `1` means one sibling or spouse was traveling with them. |
# | Parch       | Number of parents and children aboard the Titanic.                                                                             | `2` means two parents/children were traveling with them. |
# | Ticket      | Ticket number assigned to the passenger. It is usually treated as a categorical feature or dropped because of high uniqueness. | `A/5 21171`                                              |
# | Fare        | The ticket price paid by the passenger.                                                                                        | `7.25`, `71.2833`                                        |
# | Cabin       | Cabin number where the passenger stayed. Many values are missing because not every passenger had an assigned cabin.            | `C85`, `B28`, `NaN`                                      |
# | Embarked    | Port where the passenger boarded the Titanic.                                                                                  | `C`, `Q`, `S`                                            |


df.shape
df.info()
df.head(2).T
df.describe().round(2)


# Dealing with null values ------------------>
df.isnull().sum()

df['Cabin']

df['Cabin'] = df['Cabin'].fillna("No cabin")  

# Embarked column 
df['Embarked']
df['Embarked'].value_counts()
df['Embarked'] = df['Embarked'].fillna("S")




# Dealing with dulicate data ------------->
# 1. check duplicates
df.duplicated().sum()

# 2. remove duplicates 
df.drop_duplicates()



# dealing with outliers using IQR method ------------->

df.info()
df.isnull().sum()

# removing outlets from Age column  ------------------->
df['Age'].describe()
sns.boxplot(x=df['Age'])
plt.show()

q1 = df['Age'].quantile(0.25)
q1
q3 = df['Age'].quantile(0.75)
q3
iqr = q3-q1
iqr
lb = q1-iqr*1.5 
lb
ub = q3+iqr*1.5
ub

# check outliers
df[df['Age'] > ub]


df['new_age'] = np.where(df['Age'] > ub , ub,df['Age'])

df[['Age','new_age']].describe()

# filling null values in age columns
df['Age'] = df['Age'].fillna(df['Age'].median())



# removing outliers using Winsorizatoin method 
from feature_engine.outliers import Winsorizer

winsor = Winsorizer(capping_method="iqr",tail="both")
df['age_w1'] = winsor.fit_transform(df['Age'].to_numpy().reshape((-1,1)))

winsor = Winsorizer(capping_method="quantiles",tail="both",fold=0.05)
df['age_w2'] = winsor.fit_transform(df['Age'].to_numpy().reshape((-1,1)))

df[['Age','new_age','age_w1','age_w2']].describe()

df.head()

# EDA ------------------>

# Exploratory Data Analysis (EDA) is an approach used by data scientists to analyze and summarize the main characteristics of a dataset. It relies heavily on visual methods and summary statistics to discover patterns, spot errors or outliers, and check assumptions before building formal models.

df.head()
df['Survived']

df['Survived'].value_counts()

# show them in percentage %
df['Survived'].value_counts() / df['Survived'].size * 100

df.columns

# analysis on pclass
df.pivot_table(index='Pclass',columns='Survived',values='PassengerId',aggfunc="count")


# Analysis on gender
df.pivot_table(index='Sex',columns='Survived',values='PassengerId',aggfunc="count")


# Analysis on age 
sns.histplot(data=df,x="Age",kde=True,hue="Survived")
plt.show()

def age_cat(age):
    if age<12:
        return "child"
    elif age<20:
        return "teen"
    elif age < 50:
        return "adult"
    else:
        return "old"

df["age_cat"] = df['Age'].apply(age_cat)
df.pivot_table(index='age_cat',columns='Survived',values='PassengerId',aggfunc="count")

# Analysis on cabin
df.pivot_table(index='Cabin',columns='Survived',values='PassengerId',aggfunc="count")

# clean cabin column
df['Cabin'] = df['Cabin'].apply(lambda x : x[0])

df.columns
x = df[['Pclass', 'Sex', 'Age', 'SibSp','Parch', 'Fare', 'Cabin', 'Embarked']]
y = df['Survived']

x
y

# Dividing data for train test split 
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest =  train_test_split(x,y,test_size=0.2,random_state=42)


