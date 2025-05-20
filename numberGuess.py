# Text Based Number guess game
import random
import sys

# Setting variables
print("Please choose the minimum and maximum value for the random number.\n")
randomMin = int(input("Minimum: "))
randomMax = int(input("Maximum: "))
randomVal = random.randint(randomMin, randomMax)

guess = 0
count = 0
end = False

# Functions
def check():
    global count, end
    if guess == randomVal:
        count += 1
        end = True
        print("\nWell done! You succesfully guessed the correct number! The number was {}".format(randomVal))
        if count >= 2:
            print("\nIt took you {} attempts to guess the correct number!\n".format(count))
        else:
            print("\nIt took you {} attempt to guess the correct number!\n".format(count))
        sys.exit()
    else:
        count += 1
        end = False
        print("\nNot quite! Try guessing again :)")

# Game
print("\nThe random number has been selected. Make your guess!")

while end == False:
    guess = int(input("Guess: "))
    check()