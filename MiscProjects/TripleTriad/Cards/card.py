"""
This module contains the Card class.
"""

class Card:
    def __init__(self, name, top, right, bottom, left, element, image_path, mod_result):
        self.name = name
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.element = element
        self.image_path = image_path
        self.mod_result = mod_result