from Exercise201 import Rocket, RocketBoard  # RocketList

board = RocketBoard(3)

board.rockets[0].position = 50
""" print(board.rockets[0].altitude) """
print(RocketBoard.getdistance(board[0], board[1]))