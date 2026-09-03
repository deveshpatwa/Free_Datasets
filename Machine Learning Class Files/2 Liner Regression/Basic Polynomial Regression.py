import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LinearRegression


df = pd.read_csv("car_average.csv")
df.head()

# sns.scatterplot(data=df,x="horsepower",y='mpg')
# plt.show()

x = df[['horsepower']]
y = df['mpg']

# rough
x['horsepower_sqr'] = x['horsepower'] ** 2
# x['horsepower_power3'] = x['horsepower'] ** 3
# x['horsepower_power4'] = x['horsepower'] ** 4
# x['horsepower_power5'] = x['horsepower'] ** 5
# x['horsepower_power6'] = x['horsepower'] ** 6
# x['horsepower_power7'] = x['horsepower'] ** 7
# x['horsepower_power8'] = x['horsepower'] ** 8
x


model = LinearRegression()
model.fit(x,y)

prediction = model.predict(x)

sns.scatterplot(data=df,x="horsepower",y='mpg')
sns.lineplot(data=df,x="horsepower",y=prediction,color='red')
plt.show()