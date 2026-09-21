
list1 = [1, 2, 3]
list2 = [4 , 5]
print(list1 + list2)
print(list1 * 2)
print(2 in list1)

list1[1] = 20
list1.insert(1, 15)
list1.append(100)
list1.remove(20)
popped = list1.pop(0)
print("Final list:", list1)

numbers = [10 ,20 ,30 ,40, 50]
print(30 in  numbers)#True if found

#Sorting
numbers = [5 ,2 , 9, 1 , 7]
numbers.sort()
print("Sorted:", numbers)

numbers = [45 , 12, 78, 34, 23, 89, 10]
print("Original Lists", numbers)

item = int(input("Enter your number: "))
if item in numbers:
    print(item,"found at index no", numbers.index(item))
else:
    print("item not found")

ascending = numbers.copy()
ascending.sort()
print(ascending)

#Sorting to descending order
decending = numbers.copy()
decending.sort(reverse = True)
print(decending)
