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


# we will create a bank account class as A bank account has Account Holder Name, Account Number 
# and Balance
print("hello")

class bank_account():
    def __init__(self,name,account_number,balance):     # constructor which runs automatically 
        self.name = name
        self.account_number = account_number
        self.balance = balance


acc1 = bank_account("rohan",4456,500)

# ---------------------------------------

class BankAccount:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def show_details(self):
        print("\n------ Account Details ------")
        print("Name       :", self.name)
        print("Account No :", self.account_no)
        print("Balance    :", self.balance)