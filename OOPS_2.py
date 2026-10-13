class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"student name:{self.name}, age:{self.age} ")
        
s1 = Student("Gaurav", 20)
s1.display()
