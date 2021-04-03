"""Main module.

A tictactoe program written, for fun, while following the
'Complete Python Developer Certification Course' by Imtiaz Ahmad, on UDEMY.
"""

from board_class import Board
from player_class import Player
from functions import get_players, pick_position
from random import shuffle


# game logic for TicTacToe
if __name__ == '__main__':
    print("Welcome to TicTacToe. Have fun!")


    # define a variable to break out of the game
    playing = True

    # get player names, we will build player objects in the while loop
    players = get_players()
    xorzero = ['x', '0']

    # start the game
    while playing:
        # randomize which player goes first and wether he plays with 'x' or '0'
        shuffle(players)
        shuffle(xorzero)

        # create player objects
        player_one = Player(players[0], xorzero[0])
        player_two = Player(players[1], xorzero[1])
        print("{} goes first, playing with {}!".format(player_one.name, player_one.xorzero))

        # create board and print it to the players
        game = Board()
        print(game)

        # count the rounds
        round_count = 0

        # get into the actual game
        while True:
            round_count += 1

            # involve both players in the game alternatively
            if round_count == 1:
                player = player_one
            elif round_count > 1 and round_count %2 == 0:
                player = player_two
            else:
                player = player_one

            # ask current player his move
            # the function will deal with the move being valid or not
            next_move = pick_position(player, game)

            # score player position on board and print the board again
            game.score(next_move, player.xorzero)
            print(game)

            # check win conditions or draw
            # we could also check for draw in round count is 9 and no win condition
            if game.over() == True:
                print("{}, YOU WON!".format(player.name))
                player.won()
                break
            elif game.over() == "DRAW":
                print("DRAW! Nobody wins this game.")
                break

        # ask players if they want to play another round
        while True:
            play_again = input("Go for another round(yes/no)?")
            if play_again[0].lower() == 'y':
                playing = True
                break
            elif play_again[0].lower() == 'n':
                print("Alright!")
                print(player_one)
                print(player_two)
                print("See you next time!")
                playing = False
                break
            else:
                print("Oups, I didn't get that, type 'yes' or 'no'!")
