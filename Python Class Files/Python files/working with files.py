# open the file
import os

for i in os.listdir():
    print(i)

with open("file",mode="r") as file:
    file.read()


