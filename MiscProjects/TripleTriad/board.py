"""
This module creates the board for the game
"""
wall = 10
neighbors = {
    (0, 0): {
        "top": wall,
        "right": (0, 1),
        "bottom": (1, 0),
        "left": wall
    },
    (0, 1): {
        "top": wall,
        "right": (0, 2),
        "bottom": (1, 1),
        "left": (0, 0)
    },
    (0, 2): {
        "top": wall,
        "right": wall,
        "bottom": (1, 2),
        "left": (0, 1)
    },
    (1, 0): {
        "top": (0, 0),
        "right": (1, 1),
        "bottom": (2, 0),
        "left": wall
    },
    (1, 1): {
        "top": (0, 1),
        "right": (1, 2),
        "bottom": (2, 1),
        "left": (1, 0)
    },
    (1, 2): {
        "top": (0, 2),
        "right": wall,
        "bottom": (2, 2),
        "left": (1, 1)
    },
    (2, 0): {
        "top": (1, 0),
        "right": (2, 1),
        "bottom": wall,
        "left": wall
    },
    (2, 1): {
        "top": (1, 1),
        "right": (2, 2),
        "bottom": wall,
        "left": (2, 0)
    },
    (2, 2): {
        "top": (1, 2),
        "right": wall,
        "bottom": wall,
        "left": (2, 1)
    }
}

class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

        self.neighbor_data = {}

    # Validates that a card placement is A. within the board
    # and B. that the spot selcted, does'nt alredy have a card.
    def is_valid_position(self, row, column):
        if row < 0 or row >= 3 or column < 0 or column >= 3:
            return False

        if self.board[row][column] is not None:
            return False

        return True

    # Will use is valid postion, then places a card in the
    # selected spot is deemed valid.
    def place_card(self, card, row, column):
        if not self.is_valid_position(row, column):
            return False

        self.board[row][column] = card
        self.get_neighbors(row, column)
        self.update_neighbor_data()
        return True


    def get_neighbors(self, row, column):
        cards_neighbors = neighbors[(row, column)]

        card_neighbors = {}
        for direction, neighbor in cards_neighbors.items():
            if neighbor == 10:
                card_neighbors[direction] = 10

            else:
                neighboring_card = self.board[neighbor[0]][neighbor[1]]
                card_neighbors[direction] = neighboring_card

        self.neighbor_data[(row, column)] = card_neighbors    
        return card_neighbors


    def update_neighbor_data(self):
        for positions in list(self.neighbor_data):
            row, column = positions
            self.get_neighbors(row, column)
