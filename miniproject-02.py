#random number game
import random
val = random.randint(1,100)
while True:
    num = int(input("Enter the number or press Q to exit = ")) 
    if(num == "Q"):
        break
    if(num == val):
        print("sucess : Correct Guess!!")
        break
    elif(num > val):
        print("your num was bigger. Take the smaller guess....")
    else:
        print("your num was smaller. Take the bigger guess....")

print("-----GAME OVER----")
