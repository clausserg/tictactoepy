"""
Module:
test_board_class.py

This module contains tests for:
tictactoepy.board_class.py
"""


import pytest
from tictactoepy.board_class import Board


def test_get_players():
    """Testing the print dunder of a Board object"""

    my_board = Board()

    str1 = "  _1_ _2_ _3_ \n"
    str2 = "1|___|___|___|\n"
    str3 = "2|___|___|___|\n"
    str4 = "3|___|___|___|\n"
    assert my_board.__str__() == str1 + str2 + str3 + str4 and \
    len(my_board.valid_positions) == 9 and \
    len(my_board.positions.items()) == 9
