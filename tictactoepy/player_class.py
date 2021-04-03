"""
Module:
player_class.py

This module contains the Player class implementation for the tictactoe game!
"""


class Player:
    def __init__(self, name, xorzero):
        self.name = name
        self.xorzero = xorzero
        self.rounds_won = 0

    # a dunder to print name of this player
    def __str__(self):
        if self.rounds_won == 1:
            return "{} won {} round!".format(self.name, 1)
        else:
            return "{} won {} rounds!".format(self.name, self.rounds_won)

    # a method to count rounds won
    def won(self):
        self.rounds_won += 1
        return self.rounds_won
