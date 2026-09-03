import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score , mean_absolute_error , root_mean_squared_error

df = pd.read_csv('car_average.csv')
df.head()

sns.scatterplot(data=df, y='weight', x='horsepower')
plt.show()

x = df['horsepower']
y = df['weight']

model = LinearRegression()
model.fit(x.values.reshape(-1, 1), y)
prediction = model.predict(x.values.reshape(-1, 1))

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# plot
plt.scatter(x, y, label='Data points')
plt.plot(x, model.predict(x.values.reshape(-1, 1)), color='red', label='Regression line')
plt.xlabel('Horsepower')
plt.ylabel('Weight')
plt.legend()
plt.show()

# predict weight for a car with 200 horsepower
model.predict([[180]])

y
prediction

mean_absolute_error(y, prediction)
mean_squared_error(y, prediction)
root_mean_squared_error(y, prediction)
r2_score(y, prediction)