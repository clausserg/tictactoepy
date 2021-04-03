"""
Module:
useful_functions.py

This module implements functions that are useful for implementing the
TicTacToe game logic
"""


# function to create two players
def get_players():
    players = []
    while len(players) < 2:
        user = input("Name of player {}:".format(len(players) + 1))
        players.append(user)
    return players


# function to get user scoring position on board
# the function takes arguments a player and a game object
def pick_position(player, game):
    while True:
        user_pick = input("{}, next move (e.g. 31, or 11, etc.):".format(player.name))
        if game.valid_move(user_pick):
            return user_pick
            break
        else:
            print("Invalid pick!")
            print("Valid picks are: {}".format(", ".join(game.valid_positions)))
