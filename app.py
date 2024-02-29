# Let's create a game of rock, paper, scissors
# The winner of the game is determined by three simple rules
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# The player can choose from the following options: rock, paper, or scissors
# The player should be warned if they enter an invalid option
# At each round, the player must enter one option in the list and be informed of the result if they won, lost or got a tie with the opponent
# By the end of each round, the player should be asked if they want to play again
# Display the player's score and the opponent's score at the end of each round
# The game must handle user inputs, putting them in lowercase and informing if the user entered an invalid option
# The game must handle the opponent's choice randomly
# The game must handle the player's choice and inform the result of the game
# The game must handle the player's score and the opponent's score
# The game must handle the player's choice to play again
# The game must handle the player's choice to stop playing

import random
input("Welcome to the game of rock, paper, scissors. Press enter to start the game.")
player_score = 0
opponent_score = 0

while True:
    player_choice = input("Enter your choice: rock, paper, or scissors: ").lower()
    opponent_choice = random.choice(["rock", "paper", "scissors"])
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid option. Please enter rock, paper, or scissors.")
    elif player_choice == opponent_choice:
        print(f"Opponent chose {opponent_choice}. It's a tie!")
    elif (player_choice == "rock" and opponent_choice == "scissors") or (player_choice == "scissors" and opponent_choice == "paper") or (player_choice == "paper" and opponent_choice == "rock"):
        player_score += 1
        print(f"Opponent chose {opponent_choice}. You win!")
    else:
        opponent_score += 1
        print(f"Opponent chose {opponent_choice}. You lose!")
    print(f"Player score: {player_score}. Opponent score: {opponent_score}.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
# If the player wins display "You win!"
# If the player loses display "You lose!"
# If the player gets a tie display "It's a tie!"
# If the player enters an invalid option display "Invalid option. Please enter rock, paper, or scissors."

if(player_score > opponent_score):
    print("You win!")
elif(player_score < opponent_score):   
    print("You lose!")
else:
    print("It's a tie!")
print(f"Player score: {player_score}. Opponent score: {opponent_score}.")
print("Thank you for playing the game of rock, paper, scissors.")
