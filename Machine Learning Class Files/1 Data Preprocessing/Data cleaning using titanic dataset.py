import pandas as pd

df = pd.read_csv("titanic.csv")
df.head()

df.shape
df.info()
df.head(2).T
df.describe().round(2)

df.isnull().sum()

df['Cabin']

df['Cabin'] = df['Cabin'].fillna("No cabin")  

# check duplicates
df.duplicated().sum()

# remove duplicates 
df.drop_duplicates()




