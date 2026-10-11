#Guess the Number

import random

target = random.randint(1, 100)

while True:
    userchoice = int(input("Guess your target: "))
    if userchoice == target:
        print("Sucess : Correct Guess! ")
        break
    elif(userchoice < target):
        print("your number was too small. Take a bigger guess")
    else:
        print("your number was too big. Take a smaller guess")
        
print("----GAMEOVER----")



        