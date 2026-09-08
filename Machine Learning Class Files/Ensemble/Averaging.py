from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

# 1. Load data and split
X, y = fetch_california_housing(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Define base regressors
reg1 = Ridge(random_state=42)
reg2 = RandomForestRegressor(n_estimators=50, random_state=42)
reg3 = KNeighborsRegressor(n_neighbors=5)

# 3. Create the Averaging Regressor
# VotingRegressor automatically averages the predictions of base models
voting_reg = VotingRegressor(
    estimators=[("ridge", reg1), ("rf", reg2), ("knn", reg3)]
)

# 4. Train the ensemble
voting_reg.fit(X_train, y_train)

# 5. Evaluate
y_pred = voting_reg.predict(X_test)
mean_squared_error(y_test, y_pred)
mean_absolute_error(y_test, y_pred)
r2_score(y_test, y_pred)