import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 1. Load data and train a simple model
iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

# 2. Save the trained model as a .pkl file
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model saved successfully as model.pkl")
