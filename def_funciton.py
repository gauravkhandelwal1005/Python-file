#1.Dictionary literals - dictionary banana
student = {"name": "Gaurav", "age": 20,"city": "Delhi"}
print(student)

#2.Adding text
student["course"] = "B.Tech"
print("After adding:", student)

#3.Removing keys
del student["city"]
print("After removing:", student)

#4.Aceesing values
print("Name is:", student["name"])
print("Age is:", student.get("age"))

#5.Reeplacing values
student["age"]
print("After replacing age:", student)

#6.Traversing dictionary(har key ko ghumna)
for key in student:(", student[key])

def add(a, b):
    return a + b

add(10 , 20)

def greek(name):
    print("Hello",name)
greek("Gaurav")

def input_marks():
    return [50, 60, 70]

def calculate_total(marks):
    return sum(marks)

def show_result(total):
    print("Total marks :", total)

#main program 
m = input_marks()
t = calculate_total(m)
show_result(t)

def avg(a, b, c):
    total = a + b + c
    avg = total / 3
    return avg

print(avg(15 , 25, 35))
print(avg(35 , 56 , 96))

#without function - Redundancy (same code 3 times)

print("Area of house 1:", 10*20)
print("Area of house 2:", 15*20)
print("Area of house 3:", 20*20)

#With function - Redundancy hidden
def area(l, b):
    return l * b

print(area(10, 20))
print(area(15, 20))
print(area(20, 20))


    
