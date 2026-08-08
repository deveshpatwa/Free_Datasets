import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

# data file

df = pd.read_csv(r"C:\Users\deves\Documents\GitHub\Free_Datasets\Data Sets\store.csv")

# barh chart formating

plt.figure(figsize=(9,6))

df.groupby("sub_category")['sales'].sum().sort_values().plot(kind="barh",color="gray")

plt.title("Sub category wise total sales",size=15,color="blue",fontweight="bold")
plt.xlabel("Sales")
plt.ylabel("Sub category")
plt.show()

# pie chart 
df.category.value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("Category wise sales")
plt.show()

df.category.value_counts().to_excel("chart.xlsx")