"""
Module:
board_class.py

This module contains the Board class implementation for the tictactoe game!
"""


class Board:
    def __init__(self):
        # playing board
        self.antet = "  _1_ _2_ _3_ \n"
        self.row_1 = "1|___|___|___|\n"
        self.row_2 = "2|___|___|___|\n"
        self.row_3 = "3|___|___|___|\n"
        # available spots for scoring
        self.valid_positions = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]
        # translate between user input positions to positions on board
        self.positions = {
            "11": "13", "12": "17", "13": "111",
            "21": "23", "22": "27", "23": "211",
            "31": "33", "32": "37", "33": "311"
        }

    # print board
    def __str__(self):
        return self.antet + self.row_1 + self.row_2 + self.row_3

    # method to check if a scoring position is available
    def valid_move(self, board_position):
        return board_position in self.valid_positions

    # method to score X or 0 on the board
    def score(self, board_position, xorzero):
        if board_position[0] == '1':
            scoring_row = list(self.row_1)
            scoring_row[int(self.positions[board_position][1:])] = xorzero.lower()
            self.row_1 = "".join(scoring_row)
        elif board_position[0] == '2':
            scoring_row = list(self.row_2)
            scoring_row[int(self.positions[board_position][1:])] = xorzero.lower()
            self.row_2 = "".join(scoring_row)
        else:
            scoring_row = list(self.row_3)
            scoring_row[int(self.positions[board_position][1:])] = xorzero.lower()
            self.row_3 = "".join(scoring_row)

        # invalid this board position since it has been used
        self.valid_positions.remove(board_position)

    # method to check for game over conditions
    def over(self):
        for idx in [self.row_1[3] + self.row_1[7] + self.row_1[11], \
                    self.row_2[3] + self.row_2[7] + self.row_2[11], \
                    self.row_3[3] + self.row_3[7] + self.row_3[11], \
                    self.row_1[3] + self.row_2[3] + self.row_3[3], \
                    self.row_1[7] + self.row_2[7] + self.row_3[7], \
                    self.row_1[11] + self.row_2[11] + self.row_3[11], \
                    self.row_1[3] + self.row_2[7] + self.row_3[11], \
                    self.row_1[11] + self.row_2[7] +self.row_3[3]]:
            if idx in ["xxx", "000"]:
                return True
        if len(self.valid_positions) == 0:
            return "DRAW"
        return False

