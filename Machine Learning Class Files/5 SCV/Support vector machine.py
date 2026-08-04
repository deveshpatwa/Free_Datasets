# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import necessary libraries for machine learning
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import GridSearchCV

# Load the iris dataset
df = sns.load_dataset('iris')

df.head()
df.sample(10)
df.info()
df.describe().round(2)

# rough sample testing
df
x= df.loc[:, ['petal_length', 'petal_width']]
x
y = df.loc[:, 'species']
y

svm_clf = Pipeline([
("scaler", StandardScaler()),
("linear_svc", LinearSVC(C=1, loss="hinge")),  # if you scale the data using the StandardScaler. Also make sure you set the loss hyperparameter to "hinge"
])
svm_clf.fit(x, y)
svm_clf.predict([[5.5, 1.7]])



# real data
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




# more rough testing
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
X, y = make_moons(n_samples=100, noise=0.15)
polynomial_svm_clf = Pipeline([
("poly_features", PolynomialFeatures(degree=3)),
("scaler", StandardScaler()),
("svm_clf", LinearSVC(C=10, loss="hinge"))
])
polynomial_svm_clf.fit(X, y)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm")
plt.show()


# plot it perfectly with decision boundary
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1.5, 2.5, 500)
x2 = np.linspace(-1, 1.5, 500)

xx, yy = np.meshgrid(x1, x2)

X_new = np.c_[xx.ravel(), yy.ravel()]

y_pred = polynomial_svm_clf.predict(X_new)
y_pred = y_pred.reshape(xx.shape)

plt.figure(figsize=(8,5))

plt.contourf(xx, yy, y_pred,
             cmap=plt.cm.Pastel1,
             alpha=0.7)

plt.scatter(X[y==0,0], X[y==0,1],
            marker="s",
            color="blue")

plt.scatter(X[y==1,0], X[y==1,1],
            marker="^",
            color="green")

plt.xlabel("$x_1$", fontsize=14)
plt.ylabel("$x_2$", fontsize=14)

plt.xlim(-1.5,2.5)
plt.ylim(-1,1.5)

plt.show()