# import imp library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import machine learning library
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder , StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_recall_curve
from sklearn.metrics import roc_curve, roc_auc_score


df=  pd.read_csv("heartattack.csv")

df.head()
df.info()
df.isnull().sum()
df.describe().round(2).T


# data cleaning 
df['BMI'] = df['BMI'].fillna(28)


# EDA
# analysis on BMI
# df.columns
# sns.histplot(data=df,x='BMI',bins=50,kde=True,hue='HeartDiseaseorAttack')
# plt.show()

df['HeartDiseaseorAttack'].value_counts() / df.shape[0] * 100


x = df.drop(columns='HeartDiseaseorAttack')
y = df['HeartDiseaseorAttack']

model = DecisionTreeClassifier(class_weight='balanced', random_state=42)

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.05,random_state=42)

model.fit(xtrain,ytrain)
prediction = model.predict(xtest)

accuracy_score(ytest,prediction)

confusion_matrix(ytest,prediction)

print(classification_report(ytest,prediction))



# change probability solution for only testing the data
# Instead of: y_pred = model.predict(X_test)
y_probs = model.predict_proba(xtest)[:, 1]
y_probs

# Lower threshold to boost recall
custom_threshold = 0.15
y_pred_custom = (y_probs >= custom_threshold).astype(int)
accuracy_score(ytest,y_pred_custom)
print(classification_report(ytest,y_pred_custom))


# add more data solution for training the data
from imblearn.over_sampling import SMOTE

smote = SMOTE(random_state=42)
xtrain_res, ytrain_res = smote.fit_resample(xtrain, ytrain)
ytrain.value_counts() / ytrain.shape[0] * 100
ytrain_res.value_counts() / ytrain_res.shape[0] * 100
model.fit(xtrain_res,ytrain_res)
prediction = model.predict(xtest)

accuracy_score(ytest,prediction)

print(classification_report(ytest,prediction))



precision, recall, thresholds = precision_recall_curve(
    ytest,
    y_probs
)

precision
recall
thresholds
average_line = precision + recall /2

plt.plot(precision,color="blue")
plt.plot(recall,color='red')
plt.plot(thresholds,color='green')
# plt.plot(average_line,color='black')
plt.show()

plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.show()

# ROC Curve
fpr, tpr, thresholds = roc_curve(ytest, y_probs)
roc_auc = roc_auc_score(ytest, y_probs)

plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()  

