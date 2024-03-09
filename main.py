import random

def get_player_choice():
    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return player_choice

def get_comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, comp_choice):
    if player_choice == comp_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and comp_choice == 'scissors') or \
         (player_choice == 'paper' and comp_choice == 'rock') or \
         (player_choice == 'scissors' and comp_choice == 'paper'):
        return "You win!" 
    else:
        return "Computer wins!  better luck next time"

def start_game():
    print("Let's play Rock, Paper, Scissors!")
    player_choice = get_player_choice()
    comp_choice = get_comp_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {comp_choice}")
    print(determine_winner(player_choice, comp_choice))

start_game()