"""
Author: Aidan Greenwood

Note: This was developed back when I was on my laptop, and had 
an emoji keyboard.

Purpose: To solve any given wordle using elimination.
My original intention was to try making it both a solver
and a game, but that was too much work for me, who didn't
know how to code yet, so there are reminnets of that original
idea, but many are unfunctional. I plan on remaking this.
"""

import random
import string
from collections import Counter
from pathlib import Path


class WordleGame:
    def __init__(self, word_list):
        self.target_word = random.choice(word_list)  # Randomly select a target word
        self.word_list = sorted(word_list)  # Sort the word list alphabetically
        self.eliminated_letters = set()  # Letters completely excluded from future guesses
        self.correct_letters = {}  # Correct letters at specific positions
        self.possible_letters = set()  # Letters that must be used but not in the same position
        self.guaranteed_letters = set()  # Letters that must appear in future guesses
        self.subgame = {}  # Tracks eliminated positions for letters marked with ❔
        self.guessed_words = set()  # Words already guessed
        self.max_guesses = 6
        self.guesses_left = self.max_guesses

        # Letter pool: Tracks status of each letter in the alphabet
        self.letter_pool = {letter: "unknown" for letter in string.ascii_lowercase}  # "unknown", "eliminated", or "confirmed"

    def display_rules(self):
        rules = """
        Welcome to Wordle Assistant!
        1. The computer will guess a word.
        2. You provide feedback using the following symbols:
            - Correct letter in the correct position. : 1
            - Letter not in the word. : 2
            - Correct letter in the wrong position. : 3
        3. Feedback format example for the word "stone":
            - "stare" -> "12322"
            - "tried" -> "32222"
        4. The game automatically eliminates invalid guesses based on feedback and subgame rules.
        """
        print(rules)

    def update_subgame(self, guess, feedback):
        """Update the subgame with eliminated positions for ❔ letters."""
        for i, feedback_symbol in enumerate(feedback):
            if feedback_symbol == "3":
                letter = guess[i]
                if letter not in self.subgame:
                    self.subgame[letter] = [False] * 5  # Initialize with all positions as valid
                self.subgame[letter][i] = True  # Mark the position as eliminated

    def process_feedback(self, guess, feedback):
        """
        Update the game's knowledge base based on feedback, including the subgame logic for ❔ letters.
        """
        for i, feedback_symbol in enumerate(feedback):
            letter = guess[i]

            if feedback_symbol == "1":
                self.correct_letters[i] = letter
                self.guaranteed_letters.add(letter)
                self.letter_pool[letter] = "confirmed"

            elif feedback_symbol == "3":
                self.possible_letters.add(letter)
                self.guaranteed_letters.add(letter)
                self.update_subgame(guess, feedback)

            elif feedback_symbol == "2":
                if letter in self.correct_letters.values() or letter in self.possible_letters:
                    # Don't eliminate letters already confirmed in the word
                    continue
                self.eliminated_letters.add(letter)
                self.letter_pool[letter] = "eliminated"

    def is_valid_guess(self, guess):
        """Validate if a guess is consistent with the knowledge base, including subgame rules."""
        for i, letter in enumerate(guess):
            # Check if the letter is eliminated
            if letter in self.eliminated_letters:
                return False

            # Check if the letter must appear in the correct position
            if i in self.correct_letters and self.correct_letters[i] != letter:
                return False

            # Check subgame: ensure ❔ letters are not in eliminated positions
            if letter in self.subgame and self.subgame[letter][i]:
                return False

            # Check if the letter must appear in the word
            if letter in self.possible_letters and letter not in guess:
                return False

        # Ensure all guaranteed letters are present in the guess
        for letter in self.guaranteed_letters:
            if letter not in guess:
                return False

        return True

    def guess_word(self):
        """Select the next guess, prioritizing words with the most diverse letters."""
        # Always use specific first two guesses
        if len(self.guessed_words) == 0 and "slate" in self.word_list:
            self.guessed_words.add("slate")
            return "slate"

        elif len(self.guessed_words) == 1 and "bourn" in self.word_list:
            self.guessed_words.add("bourn")
            return "bourn"

        # Otherwise use normal logic
        possible_words = [w for w in self.word_list if self.is_valid_guess(w)]
        if not possible_words:
            return None

        def diversity_score(word):
            return len(set(word))  # Fewer repeated letters preferred

        next_guess = sorted(possible_words, key=diversity_score, reverse=True)[0]
        self.guessed_words.add(next_guess)
        return next_guess

    def play_game(self):
        self.display_rules()
        while self.guesses_left > 0:
            print(f"\nGuesses left: {self.guesses_left}")
            guess = self.guess_word()
            if guess is None:
                print("IDK Bruh")
                break

            print(f"\nComputer's guess: {guess}")
            feedback = input(f"Provide feedback for the guess '{guess}' (e.g., 12322): ")
            if feedback == "11111":
                print(f"Ha I'm Smarter Then You")
                break

            self.process_feedback(guess, feedback)
            self.guesses_left -= 1

            # Display the subgame state for ❔ letters
            print("\nSubgame state (eliminated positions for ❔ letters):")
            for letter, positions in self.subgame.items():
                eliminated = ["❌" if pos else "❔" for pos in positions]
                print(f"  {letter}: {''.join(eliminated)}")

        if self.guesses_left == 0:
            print(f"Game Over!")


def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return sorted([line.strip() for line in file.readlines()])  # Sort words alphabetically


word_list = load_word_list('WebPortfolio/MiscProjects/Wordle/sgb-words.txt')
game = WordleGame(word_list)
game.play_game()