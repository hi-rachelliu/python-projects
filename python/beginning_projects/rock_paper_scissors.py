import random

t = ["rock", "paper", "scissors"]
user_choice = input("Rock, Paper, or Scissors: ").lower()
computer_choice = random.choice(t)

if user_choice == computer_choice:
    print(f"You chose: {user_choice}, the computer chose: {computer_choice}.\n")
    print ("It's a draw!")
if user_choice == "rock":
    print (f"You chose: {user_choice}, the computer chose: {computer_choice}.\n")
    if computer_choice == "paper":
        print ("You lose!")
    if computer_choice == "scissors":
        print ("You win!")
if user_choice == "paper":
    print (f"You chose: {user_choice}, the computer chose: {computer_choice}.\n")
    if computer_choice == "rock":
        print ("You win!")
    if computer_choice == "scissors":
        print ("You lose!")
if user_choice == "scissors":
    print (f"You chose: {user_choice}, the computer chose: {computer_choice}.\n")
    if computer_choice == "rock":
        print("You win!")
    if computer_choice == "paper":
        print("You lose!")
else:
    print ("Error input. Check your spelling!")
