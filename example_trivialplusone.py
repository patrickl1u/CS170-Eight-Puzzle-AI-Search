import numpy as np
from game_logic import gameBoard, gameMove
from game_logic import solve

# Example of how the program should solve for
#   trivial case but one move off using ucs 

# initialize 
startBoard = gameBoard(np.array(np.mat('1 2 3; 4 5 0; 7 8 6')))

lastmove = solve(startBoard)

print("\nsolution: \n")
lastmove.print_path()
# firstNode = gameMove(None, startBoard, "start", 0, 0)

# firstNode.print()

# # first move
# move = "down"
# cost = 1 # all cost is 1 in UCS
# # board after performing move
# curboard = gameBoard(np.array(np.mat('1 2 3; 4 5 0; 7 8 6')))
# move1 = gameMove(firstNode, curboard, move, firstNode.depth + 1, cost)

# move1.print()

# # second move
# move = "down" 
# cost = 1 
# curboard = gameBoard(np.array(np.mat('1 2 3; 4 5 6; 7 8 0')))
# move2 = gameMove(move1, curboard, move, move1.depth + 1, cost)

# move2.print()
# print("printing iaowsejtwaet")
# move2.print_path()

# print(move2.boardAfterMove.board)