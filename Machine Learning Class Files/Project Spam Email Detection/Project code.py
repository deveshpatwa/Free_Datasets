# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import sklearn libraries
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv('emails.csv')

# Number of Rows: 5172 (each row represents an email)
# Number of Columns: 3002 (1 column for email name, 3000 columns for words, 1 column for labels)
# First Column: Email name (encoded with numbers for privacy)
# Last Column: Labels for prediction (1 for spam, 0 for not spam)
# Remaining Columns: 3000 most common words in the emails (after excluding non-alphabetical characters/words)

df.head()
df.info()
df.shape
df.size

# removing the first column (email name) as it is not needed for prediction
df = df.drop(columns=["Email No.","Prediction"])

df["spam"] = df["spam"].apply(lambda x: 1 if x > 0 else 0)

x = df.drop(columns="spam")
y = df["spam"]

# number of spam and non-spam emails 1-Spam and 0-Not Spam
df['spam'].value_counts()

# percentage of spam and non-spam emails
# value_counts(normalize=True) returns the proportion (or percentage) of each unique value instead of the raw count.
spam_percent = df['spam'].value_counts(normalize=True)*100
print(spam_percent)

# Visualizing the distribution of spam and non-spam emails using a bar plot
spam_percent.plot(kind='bar')
plt.xlabel('Spam')
plt.ylabel('Percentage')
plt.title('Distribution of Spam and Not Spam Emails')
plt.show()


# train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)

prediction = model.predict(x_test)

accuracy_score(y_test, prediction)

print(classification_report(y_test, prediction))


# linearsvc model 

model = LinearSVC()
model.fit(x_train,y_train)

prediction = model.predict(x_test)
accuracy_score(y_test,prediction)
print(classification_report(y_test,prediction))

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

prediction = model.predict(x_test)
accuracy_score(y_test,prediction)
print(classification_report(y_test,prediction))

