"""
Rock, Paper, Scissors

@author: Aydin Sasanian

"""
import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower().strip()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid input.")
        continue

    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")


    if user_input == computer_pick:
        print("Draw!")

    elif (user_input == 'rock' and computer_pick == 'scissors') or \
         (user_input == 'paper' and computer_pick == 'rock') or \
         (user_input == 'scissors' and computer_pick == 'paper'):
        user_wins += 1
        print("You won!")

    else:
        computer_wins += 1
        print("You Lost!")

print("You win", user_wins, "times.")
print("Computer wins", computer_wins, "times.")
print("Goodbye!")
