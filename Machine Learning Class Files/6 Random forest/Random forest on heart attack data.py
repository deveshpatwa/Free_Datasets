# import data analysis libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import machine learning libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# The n_jobs parameter tells Scikit-Learn the number of CPU cores to use for training and predictions (–1 tells Scikit-Learn to use all available cores):

# about the data
# HeartDiseaseorAttack — Heart disease or heart attack (0=No, 1=Yes)
# HighBP — High blood pressure (0=No, 1=Yes)
# HighChol — High cholesterol (0=No, 1=Yes)
# CholCheck — Cholesterol check in last 5 years (0=No, 1=Yes)
# BMI — Body Mass Index
# Smoker — Smoker (0=No, 1=Yes)
# Stroke — History of stroke (0=No, 1=Yes)
# Diabetes — Diabetes status
# PhysActivity — Physical activity (0=No, 1=Yes)
# HvyAlcoholConsump — Heavy alcohol consumption (0=No, 1=Yes)
# MentHlth — Poor mental health days (0–30)
# PhysHlth — Poor physical health days (0–30)
# Sex — Sex (0=Female, 1=Male)
# Age — Age group (1=18–24 ... 13=80+)
# Education — Education level (1=Lowest, 6=Highest)
# Income — Income category (1=Lowest, 8=Highest)

df = pd.read_csv("heart_attack.csv")
df.head().T
df.describe().T
df.columns
df.info()
df.isnull().sum()

# data clean for BMI
df['BMI'] = df['BMI'].fillna(27)



x = df.drop(columns='HeartDiseaseorAttack')
y = df['HeartDiseaseorAttack']

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(class_weight="balanced")

model.fit(xtrain,ytrain)

prediction = model.predict(xtest)
accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))




# now we will fit model using SMOTE
# Another popular approach is SMOTE (Synthetic Minority Over-sampling Technique).
# It creates synthetic examples of the minority class.

from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)

Xtrain_resampled, ytrain_resampled = smote.fit_resample(
    xtrain,
    ytrain
)

model.fit(Xtrain_resampled, ytrain_resampled)

prediction = model.predict(xtest)
accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))