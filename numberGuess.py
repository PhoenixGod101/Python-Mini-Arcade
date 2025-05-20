 # Text Based Number guess game
import random
import sys

# Setting variables
print("Please choose the minimum and maximum value for the random number.")
randomMin = int(input("Minimum: "))
randomMax = int(input("Maximum: "))
randomVal = random.randint(randomMin, randomMax)

guess = 0
count = 0
end = False

# Functions
def check():
    if guess == randomVal:
        count += 1
        end == True
        print("Well done! You succesfully guessed the correct number! The number was {}".format(randomVal))
        if count >= 2:
            print("It took you {} attempts to guess the correct number!".format(count))
        else:
            print("It took you {} attempt to guess the correct number!".format(count))
        sys.exit()

# Game
print("The random number has been selected. Make your guess!")
guess = int(input("Guess: "))