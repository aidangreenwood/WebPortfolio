"""
This module will load card data from JSON
and create Card objects using the class
defined in card.py.
"""

import json
from pathlib import Path
from card import Card

current_folder = Path(__file__).parent
card_data_path = current_folder / "card_data.json"

cards = []

with open(card_data_path, "r") as file:
    data = json.load(file)

cards_data = data["cards"]

# Using the cards data make objects
# that would be usable by the main
# game loop.

for card in cards_data:

    new_card = Card(
    card["name"],
    card["top"],
    card["right"],
    card["bottom"],
    card["left"],
    card["element"],
    card["image_path"],
    card["mod_result"]
    )

    cards.append(new_card)
