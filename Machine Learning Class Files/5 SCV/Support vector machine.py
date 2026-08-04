import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV

df = sns.load_dataset('iris')

df.head()
df.sample(10)
df.info()
df.describe().round(2)

x,y = df.drop('species', axis=1), df['species']
x
y

sns.pairplot(df, hue='species', palette='coolwarm')
plt.show()

xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)

pipe = Pipeline([('scaler', StandardScaler()), ('svc', SVC())])

pipe.fit(xtrain, ytrain)

prediction = pipe.predict(xtest)

accuracy_score(ytest, prediction)