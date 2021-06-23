from Exercise201 import Rocket, RocketBoard  # RocketList

board = RocketBoard(10)

board.rockets[0].position = 50
""" print(board.rockets[0].altitude) """
print(RocketBoard.getdistance(board[0], board[1]))
print(len(board))
