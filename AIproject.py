
import random

choices = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0
draws = 0

while True:
    print("wellcome to this funny game")
    user_choice = input("Choose rock, paper or scissors: ")
    if user_choice not in choices:
        print("invalaid option. Please try again.\n")
        continue
    
    computer_choice = random.choice(choices)
    print(f"\nYou chose {user_choice} and computer chose {computer_choice}.")
    
    if user_choice == computer_choice:
        draws += 1
        print("It's a draw!\n")
    
    elif user_choice == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You win!\n")
    
    elif user_choice == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You win!\n")
    
    elif user_choice == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You win!\n")
    
    else:
        computer_wins += 1
        print("Computer wins!\n")
    
    print(f"User wins: {user_wins}, Computer wins: {computer_wins}, Draws: {draws}\n")

