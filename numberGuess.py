 # Text Based Number guess game
import random

# Setting variables
print("Please choose the minimum and maximum value for the random number.")
RandomMin = int(input("Minimum: "))
RandomMax = int(input("Maximum: "))
RandomVal = random.randint(RandomMin, RandomMax)

Guess = 0
Count = 0

# Game
print("The random number has been selected. Make your guess!")
Guess = int(input("Guess: "))