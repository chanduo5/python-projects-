import random

def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please select rock, paper, or scissors.")
        return
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

play_rps()
