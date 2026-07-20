# Object-Oriented Programming (OOPs) in Python is a programming paradigm that organizes 
# code around objects and classes rather than just functions and logic. It allows you to model 
# real-world entities (like a bank account, a car, or a user) by bundling their data (attributes) 
# and behaviors (methods) together into a single package.

# Class: 
#   A blueprint or template for creating objects. It defines the variables (attributes) and 
#   functions (methods) that the objects will have.
#   - Imagine a bank wants to create thousands of customer accounts.
#   - Instead of writing the same code thousands of times, they make one blueprint.
#   - That blueprint is called a Class.

# Object: 
#   A specific instance built from a class blueprint. It holds its own actual data.


# Four main pillars of object oriented programming :

# Encapsulation :
#   is the binding of data and the methods that operate on that data into a single 
#   unit, known as a class. It hides the internal state of an object from the outside world and only 
#   allows access through a public interface.

# Abstraction : 
#   is the concept of hiding complex implementation details and showing only the essential features 
#   of the object. It focuses on what the object does rather than how it does it.

# Inheritance :
#   is a mechanism that allows a new class to inherit properties and behaviors from an 
#   existing class. The new class is called the subclass (or child class), and the existing class 
#   is called the superclass (or parent class). This promotes code reusability.

# Polymorphism :
#   means "many forms." In OOP, it allows objects of different classes to be treated as objects 
#   of a common superclass. This means a single action can have different behaviors depending on 
#   the object it's being applied to.

# we will create a bank account class as A bank account has Account Holder Name, Account Number 
# and Balance
import os
os.system("cls")

class bank_account():
    def __init__(self,name,account_number,balance):     # constructor which runs automatically 
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def details(self):
        print("Account details are -")
        print("Name :",self.name)
        print("account No :",self.account_number)
        print("Account balance :",self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("Deposited successfull")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Can't withdwar low balance !!")
        else:
            self.balance -= amount
        print(f"{amount} withdrawn {self.balance} left")


acc1 = bank_account("rohan",4456,500)

acc1.name
acc1.account_number

acc2 = bank_account("kunal",8897,240)

acc2.name
acc2.account_number

acc2.details()
acc1.details()

acc1.deposit(2300)
acc1.details()
acc1.withdraw(555)

