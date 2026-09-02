import random

# Determine winner and score rules
def determine_winner(player, computer):
    if player == computer:
        return "Tie!", 0
    # Rock>scissors>paper<
    elif (player ==  "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        return "... Fine, You Win", 1
    else:
        return "HA! I Win", -1
    
# Main game loop
def play_game():
    player_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]
    end_words = ["end", "stop", "quit", "exit"]
    while True:
        # Player choice
        player_choice = input("Enter Rock, Paper, Scissors(; Or say stop to end the game: ").lower()
        if player_choice in end_words:
            print("Thanks For Playing(;")
            break
        elif player_choice not in choices:
            print("Huh? I couldnt understand that, try again?")
            continue

        # Computer Choice
        computer_choice = random.choice(choices)
        print (f"I Picked: {computer_choice}\n")

        # Determine Result
        result, score_change = determine_winner(player_choice, computer_choice)
        print(f"{result}\n")

        # Score Change
        if score_change == 1:
            player_score += 1
        elif score_change == -1:
            computer_score += 1

        print(f"Score: You - {player_score}, Me - {computer_score} (;\n")

        # Start Game
play_game()