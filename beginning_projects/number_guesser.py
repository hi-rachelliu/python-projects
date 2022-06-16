import math
import random

print("Welcome to number guesser game!")
minimum = int(input("Minimum: "))
maximum = int(input("Maximum: "))
number = random.randint(minimum, maximum)

print("You have 3 chances to guess the number!")

count = 0
while count < 3:
    count += 1
    user_number = int(input("Guess the number: "))
    if user_number > number:
        print("Try again! You guessed too high!")
    if user_number < number:
        print("Try Again! You gussed too low!")

if count == 3:
    print ("The number is "  + str(number))
    print ("Better luck next time!")