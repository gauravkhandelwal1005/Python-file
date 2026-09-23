class Student:
    name = "Gaurav"

s1 = Student()
print(s1.name)

class Car:
    brand = "BMW"
    color = "Green"
    
car1 = Car()
print(car1.brand)
print(car1.color)

class Student:
    college = "Chandigarh University"
    
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Python is a high level programming language")
        
s1 = Student("Gaurav", 99)
print(s1.name, s1.marks)
print(s1.college)

s2 = Student("Purvi", 86)
print(s2.name, s2.marks)
print(s2.college)

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome to Python Programming", self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = Student("Gaurav", 99)
s1.welcome()
print(s1.name, s1.get_marks())

s2 = Student("Purvi", 89)
s2.welcome()
print(s2.name, s2.get_marks())

class Student():
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod
    def hello():
        print("Hello")
        
    def get_val(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi", self.name, "your average score is:", sum/3)

s1 = Student("Gaurav", [99, 98, 97])
s1.get_val()

#Abstraction in python

class Car():
    
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.acc = True
        self.brk = True
        self.clutch = True
        print("Car is started")
        
car1 = Car()
car1.start()

class Account:
    
    def __init__(self, bal , acc):
        self.balance = bal
        self.account_no = acc
        
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "debited from your account")
        print("Total balance is:", self.balance)
        
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "credited to your account")
        print("Total balance is:", self.balance)
        
    def get_balance(self):
        return self.balance
        
acc1 = Account(100000, 12345678)
print(acc1.balance)
print(acc1.account_no)
(acc1.debit(5000))
(acc1.credit(100000))
