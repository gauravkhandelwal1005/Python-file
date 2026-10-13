try:
    num1 = int(input("Enter your number: "))
    num2 =  int(input("Enter your number: "))
    result = num1/num2
except(ZeroDivisionError):
    print("Error: Cannot divide by zero!")
except(ValueError):
    print("Error: Inalid Input! Must be integer.")
else:
    print("Result is:", result)
finally:
    print("code excution completed")
    
