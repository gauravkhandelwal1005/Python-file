i = 1
while i <= 10:
  if(i % 2 == 0):
    i += 1
    continue
  print(i)
  i += 1

i = 1 
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1

i = 1 
while i <= 10:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

nums = [1 ,2 ,3 ,4, 5]

for i in nums:
    print(i)

str = ("Gaurav khandelwal")

for char in str:
    if(char == 'h'):
        print("h is found")
        break
    print(char)

print("END")

nums = [1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100]

for i in nums:
    print(i)

nums = (1 ,4 ,9 ,16 ,25 ,36 ,49 ,64 ,81 ,100)

x = 49
idx = 0

for var in nums:
    if(var == x):
        print("found is idx", idx)
    idx += 1

for i in range(10):
    print(i)

for i in range(2 , 10):
    print(i)

for i in range(2 , 10 ,2):
    print(i)

for i in range(1 , 100):
    print(i)

for i in range(100 , 0 , -1):
    print(i)

n = int(input("Enter your number: "))

for i in range(1 , 11):
    print(n * i)

