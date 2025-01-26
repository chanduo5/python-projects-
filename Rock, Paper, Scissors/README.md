### Rock, Paper, Scissors Game ###

Objective: The goal of the game is to choose an option (rock, paper, or scissors) that defeats your opponent's choice according to the following rules:

>Rock crushes scissors.
>Scissors cut paper.
>Paper covers rock.


## How the Code Works: ##

1) Import the Random Module: The code uses the random module to allow the computer to make a random choice between rock, paper, and scissors.
  
  python

    import random


2)  Define the Function: The game logic is encapsulated in a function called play_rps().

  python

    def play_rps():

3)  Welcome Message and Choices: The program prints a welcome message and defines the three possible choices.

  python

    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]

4)  Computer's Random Choice: The computer randomly selects one of the choices (rock, paper, or scissors).

  python
   
    computer_choice = random.choice(choices)

5)  User's Choice: The user is prompted to input their choice.

  python

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

6)  Validate User's Choice: The program checks if the user's choice is valid. If not, it displays an error message and ends the game.

  python
   
    if user_choice not in choices:
    print("Invalid choice! Please select rock, paper, or scissors.")
    return
 
 
 7)  Display Choices: The program shows what the computer chose.

  python

    print(f"Computer chose: {computer_choice}")


8)  Determine the Winner: The game logic determines the winner based on the classic rules:

   . If the user's choice matches the computer's choice, it's a tie.

   . If the user selects the winning choice against the computer's choice, the user wins.

   . Otherwise, the computer wins.

  python


    if user_choice == computer_choice:
    print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    else:
    print("You lose!")


9)  Call the Function: The function play_rps() is called to start the game.

  python

    play_rps()



##  This is how the simple Rock, Paper, Scissors game works and how the code is structured to make the game functional. ##
