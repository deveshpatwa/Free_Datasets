
from sklearn.datasets import make_moons
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC

X, y = make_moons(n_samples=100, noise=0.15), StandardScaler
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