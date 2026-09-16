a = 10
b = 5

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a % b)

student = {
    "name": "Gaurav",
    "age": 26,
    "surname": "khandelwal",
    "subjects": {
        "maths": 95,
        "chem": 96,
        "phy": 99
    }
}

student.update({"city": "gurgaon"})
print(student)

sequence = {1,2,2,4,"Gaurav","Khandelwal"}
print(sequence)
print(type(sequence))

sequence = set()
print(type(sequence))

sequence = set()
sequence.add(1)
sequence.add(2)
sequence.add(3)
sequence.add(4)

print(sequence)
sequence.clear()
print(sequence)

collection = {"Kartik","Deepanshu","Mahee","Ankit"}
print(collection.pop())


series1 = {1,2,3}
series2 = {3,4,5}

print(series1.intersection(series2))

classroom = {"python","java","C++","python","javascript","java","python","java","C++","C"}
print(len(classroom))

count = 1

while count <= 5:
    print("Gaurav")
    count = count + 1

print(count)

i = 6

while i <= 100:
    print("hello", i)
    i = i + 1

#print 1 to 5 number

i = 1
while i <= 5:
    print(i)
    i = i + 1

#print reverse 5 to 1 numbers 

i = 5
while i >= 1:
    print(i)
    i = i - 1
    
print("Loop ended")

i = 1
while i <= 100:
    print(i)
    i = i + 1

i = 100
while i >= 1:
    print(i)
    i = i - 1

i = 1
while i <= 10:
    print(19*i)
    i += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at index", i)
        i = i + 1
    
i = 1
while i <= 5:
    print(i)
    i += 1


i = 1
while i <= 5:
    break
    print(i)
    i += 1



 


