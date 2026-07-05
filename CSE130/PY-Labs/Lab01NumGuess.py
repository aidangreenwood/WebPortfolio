# 1. Name: 
#    Aidan Greenwood
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This programm will ask you to input a number, and as you do it will give you hints to help you guess the number
# 4. What was the hardest part? Be as specific as possible.
#    This assignmet went really well for me as I have alread done an assignment like exactly like this before.
#    The hardest part for me was the list because I forgot for one second how to use append.
# 5. How long did it take for you to complete the assignment?
#    ~36 min

import random

# Game introduction.
print("\nWelcome to the number guessing game!\n" \
"The goal of the game is to guess the number I choose in the least number of guesses you can.\n" \
"Ready?")

# Prompt the user for how difficult the game will be. Ask for an integer.
print("-----------------------")
print("Difficulty...")
difficulty = int(input("Input a positive integer, this will be how high from 1 I will be able to pick my secret number from. "))

# Generate a random number between 1 and the chosen value.
secret_num = random.randint(1, difficulty)

# Give the user instructions as to what he or she will be doing.
print(f"I have my number, now guess numbers between 1 and {difficulty} until you guess my number, and I'll give you hints as you go.\n")

# Initialize the sentinal and the array of guesses.
guesses = 0
guess = 0
guess_numbers = []

# Play the guessing game.
while guess != secret_num:
    # Prompt the user for a number.
    guess = int(input("Type in your guess: "))

    # Store the number in an array so it can be displayed later.
    guesses += 1
    guess_numbers.append(guess)

    # Make a decision: was the guess too high, too low, or just right.
    if guess > secret_num:
        print("Your guess was too high, try a lower number.\n")
    elif guess < secret_num:
        print("Your guess was too low, try a bigger number.\n")

# Give the user a report: How many guesses and what the guesses where.
print("-------------------")
print(f"You got my number, it was {secret_num}!")
print(f"You guessed my number in {guesses} tries.")
print(f"All the numbers you tried were: {guess_numbers}")
