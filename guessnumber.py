import random

number = int(random.randrange(1,100))
turns = 2
guess = 0

while turns > 0:
    print ("Turns remaining: " + str(turns))
    UserInput = input("Guess  a number between 1 and 100: ")
    if UserInput.isdigit():
        guess = int(UserInput)
    else:
        guess == 0
        print ("invalid guess")
        continue        

    if guess > 0 and guess < 100:
        if guess == number:
            print ("you guessed the number!")
            break
        elif  guess > number:
            print ("Go lower")
            turns -= 1
        elif guess < number:
            print ("go higher")
            turns -= 1
    else:
        print("invalid guess") 
if turns == 0:
    print ("you lost, Game over")
    print ("the number was: " + str(number))
    