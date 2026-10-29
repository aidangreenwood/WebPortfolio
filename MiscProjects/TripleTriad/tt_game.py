"""
Author: Aidan Greenwood

Purpose: 
Triple Triad is a game from FF8 that I love playing,
but it is a little inconvienient having to actually
play FF8 in order to play it, so I decidd that I would make
a version playable whenever.
"""

from Cards import cards_loader
from board import Board

game_board = Board()

    # Test Neighbor functionality
# game_board.place_card("card1", 0, 0)
# game_board.place_card("card2", 0, 2)

# print(game_board.neighbor_data[(0, 0)]["right"])
# print(game_board.neighbor_data[(0, 2)]["left"])

# game_board.place_card("card3", 0, 1)

# print(game_board.neighbor_data[(0, 0)]["right"])
# print(game_board.neighbor_data[(0, 2)]["left"])

# print(game_board.neighbor_data[(0, 1)]["right"])
# print(game_board.neighbor_data[(0, 1)]["left"])

    # Test card ownership
# card1 = cards_loader.cards[0]
# card2 = cards_loader.cards[0]

# card1.owner = "Player 1"
# card2.owner = "Player 2"

# print(card1.name, card1.owner)
# print(card2.name, card2.owner)

# # Change the first card's owner
# card1.owner = "Player 2"

# print(card1.name, card1.owner)
# print(card2.name, card2.owner)