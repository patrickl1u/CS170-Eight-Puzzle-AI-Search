import numpy as np
from game_logic import gameBoard, gameMove
from game_logic import solve
"""
Create the gameboard organized as with numpy:

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Where 0 is the empty space.
"""
game_start_state = np.array(np.mat('1 2 3; 4 5 6; 7 8 0'))


# exit()
gboard = gameBoard(game_start_state)
status = gboard.is_swap_valid(game_start_state[0][0], game_start_state[0][2])
print(status)
status = gboard.is_swap_valid(game_start_state[0][1], game_start_state[0][2])
print(status)

exit()


# example game 
# demo of function usage
# from 'easy' sate

# solve in two moves:
#   down, down

startBoard = gameBoard(np.array(np.mat('1 2 0; 4 5 3; 7 8 6')))
firstNode = gameMove(None, startBoard, "start", 0, 0)

firstNode.print()

# first move
move = "down"
cost = 1 # all cost is 1 in UCS
# board after performing move
curboard = gameBoard(np.array(np.mat('1 2 3; 4 5 0; 7 8 6')))
move1 = gameMove(firstNode, curboard, move, firstNode.depth + 1, cost)

move1.print()

# second move
move = "down" 
cost = 1 
curboard = gameBoard(np.array(np.mat('1 2 3; 4 5 6; 7 8 0')))
move2 = gameMove(move1, curboard, move, move1.depth + 1, cost)

move2.print()


# default or specify graph
# select algorithm
# find solution
# solve(game_start_state) # probably should comment until done
# - maybe print steps
# return solution
# - expaded a total of X nodes
# - maximum number of Y nodes in queue at any given time
# - goal node depth: Z nodes



"""
Six Test Cases
Trivial, Easy, Oh Boy, Very Easy, Doable, Impossible
Refer to report guidelines to see how they look

"""
test_case_1 = np.array(np.mat('1 2 3; 4 5 6; 7 8 0')) # trivial / completed
test_case_2 = np.array(np.mat('1 2 0; 4 5 3; 7 8 6')) # easy
test_case_3 = np.array(np.mat('8 7 1; 6 0 2; 5 4 3')) # oh boy
test_case_4 = np.array(np.mat('1 2 3; 4 5 6; 7 0 8')) # very easy
test_case_5 = np.array(np.mat('0 1 2; 4 5 3; 7 8 6')) # doable
test_case_6 = np.array(np.mat('1 2 3; 4 5 6; 8 7 0')) # IMPOSSIBLE
goal_state = np.array(np.mat('1 2 3; 4 5 6; 7 8 0')) # compare with game board to check if finished


