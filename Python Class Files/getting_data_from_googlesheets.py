import pandas as pd

# just replace this if you want to get data from a different Google Sheet
url = "https://docs.google.com/spreadsheets/d/196WXgqFuGi50mA5_8nYxUycwKKPwnRLE6gSUMQ2yCP8/edit?usp=sharing"

url = url.replace("/edit?usp=sharing", "/export?format=csv")
df = pd.read_csv(url)
df.head()