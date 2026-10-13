class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"student name:{self.name}, age:{self.age} ")
        
s1 = Student("Gaurav", 20)
s1.display()

class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance: ${self.balance}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. Remaining Balance: ${self.balance}")
        else:
            print("Insufficient Balance")
            
acc = BankAccount("Gaurav", 100000000)
acc.deposit(5000000)
acc.withdraw(1000000)
