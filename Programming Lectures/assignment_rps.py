import random

#Define the choices for both the user and computer
choices = ["rock", "paper", "scissors"]

#This line starts a while loop that will continue indefinitely (until explicitly terminated) because the condition True is always true
while True:
    #Get the user's choice or allow them to quit by entering 'q'
    user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

    #Adding the quitting condition
    if user_choice == 'q':
        break

    #To check if the user's input is valid
    if user_choice not in choices:
        print("Invalid input. Please choose from 'rock', 'paper', or 'scissors' only.")
        continue

    #Generating a random choice for the computer
    computer_choice = random.choice(choices)

    #Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors" or \
         user_choice == "paper" and computer_choice == "rock" or \
         user_choice == "scissors" and computer_choice == "paper":
        print(f"You win! Computer chose {computer_choice}.")
    else:
        print(f"You lose! Computer chose {computer_choice}.")

#if the user choice pick q this will show as a prompt
print("Hope you had fun playing!")