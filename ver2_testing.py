#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math
from copy import copy
from queue import PriorityQueue

misplaced_tile_heuristic = 0
euclidean_distance_heuristic = 0

#######
### get_cost
#######


# def get_cost(b1, b2):
#     if misplaced_tile_heuristic:
#         misplaced_heuristic_count = sum(1 for i, j in zip(b1.flat, b2.flat) if i != j)
#         return misplaced_heuristic_count + 1

#     if euclidean_distance_heuristic:
#         euclidean_distance_heuristic_count = 0
#         for i in range(1, 9):
#             a_x, a_y = np.argwhere(b1 == i)[0]
#             b_x, b_y = np.argwhere(b2 == i)[0]
#             euclidean_distance_heuristic_count += math.sqrt((a_x - b_x)**2 + (a_y - b_y)**2)
#         return euclidean_distance_heuristic_count + 1
    
#     return 1

# def get_cost(b1, b2):
#     if misplaced_tile_heuristic:
#         return sum(1 for i, j in zip(b1.flatten(), b2.flatten()) if i != j)
#     elif euclidean_distance_heuristic:
#         cost = 0
#         for i, row in enumerate(b2):
#             for j, val in enumerate(row):
#                 if val != 0:
#                     target_i, target_j = divmod(val-1, 3)
#                     cost += math.sqrt((i-target_i)**2 + (j-target_j)**2)
#         return cost
#     else:
#         return 1

# def get_cost(b1, b2):
#     if misplaced_tile_heuristic:
#         return sum(1 for i in range(9) if b1[i] != b2[i])
#     if euclidean_distance_heuristic:
#         total_distance = 0
#         for i in range(9):
#             x1, y1 = divmod(b1.index(i), 3)
#             x2, y2 = divmod(b2.index(i), 3)
#             total_distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#         return total_distance
#     return 1

# def get_cost(b1, b2):
#     if misplaced_tile_heuristic:
#         return sum([1 for i in range(9) if b1.index(i) != b2.index(i)]) + 1
#     if euclidean_distance_heuristic:
#         euclidean_distance_heuristic_count = 0
#         for i in range(1, 9):
#             b1_x, b1_y = divmod(b1.index(i), 3)
#             b2_x, b2_y = divmod(b2.index(i), 3)
#             euclidean_distance_heuristic_count += math.sqrt((b1_x - b2_x) ** 2 + (b1_y - b2_y) ** 2)
#         return euclidean_distance_heuristic_count + 1
#     return 1

# def get_cost(b1, b2):
#     if misplaced_tile_heuristic:
#         return sum([1 for i, j in zip(b1.flatten(), b2.flatten()) if i != j])

#     if euclidean_distance_heuristic:
#         distance = 0
#         for i, row in enumerate(b2):
#             for j, val in enumerate(row):
#                 if val == 0:
#                     continue
#                 x, y = divmod(val - 1, len(row))
#                 distance += math.sqrt((i - x) ** 2 + (j - y) ** 2)
#         return distance

#     return 1

def get_cost(b1, b2):
    """
    if misplaced_tile_heuristic = 1, cost is now how many tiles are misplaced.
    if euclidean_distance_heuristic = 1, cost is now the sum of the physical distance of each tile misplaced.
    """
    if misplaced_tile_heuristic:
        misplaced_heuristic_count = sum(1 for x, y in zip(b1.ravel(), b2.ravel()) if x != y and y != 0)
        return misplaced_heuristic_count + 1

    if euclidean_distance_heuristic:
        euclidean_distance_heuristic_count = sum(math.sqrt(pow((np.where(b2 == i)[0][0] - np.where(b1 == i)[0][0]), 2) + pow((np.where(b2 == i)[1][0] - np.where(b1 == i)[1][0]), 2)) for i in range(1, 9))
        return euclidean_distance_heuristic_count + 1

    return 1


#######
### end get_cost, start swap
#######

# - swap does not work replaced here w/ v1
# #todo

# swap 0 and something
def swap(self, p1, p2):
    # print("preswap: \n")
    # print(self)
    z_x, z_y = p1
    a_x, a_y = p2
    newboard = self
    newboard[z_x, z_y] = self[a_x, a_y]
    newboard[a_x, a_y] = 0
    # print("postswap: \n{}".format(newboard))
    return newboard

# def swap(board, pos1, pos2):
#     x1, y1 = pos1
#     x2, y2 = pos2
#     board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
#     return board


#######
# end swap, begin movement related
#######



# def find_num(npboard, val):
#     # should only be one object so element 0, 0 only
#     arrobj = np.argwhere(npboard == val)
#     return arrobj[0][0], arrobj[0][1]

def find_num(npboard, val):
    return np.where(npboard == val)[0][0], np.where(npboard == val)[1][0]


#######
# end movement related, begin #todo
#######

def move_up(npboard):
    before = np.ndarray.copy(npboard)
    z_x, z_y = find_num(npboard, 0)
    if z_x == 0: 
        return False, -1
    after = swap(npboard, (z_x, z_y), (z_x-1, z_y))
    cost = get_cost(before, after)
    return after, cost

def move_down(npboard):
    before = np.ndarray.copy(npboard)
    z_x, z_y = find_num(npboard, 0)
    if z_x == 2: 
        return False, -1
    after = swap(npboard, (z_x, z_y), (z_x+1, z_y))
    cost = get_cost(before, after)
    return after, cost

def move_left(npboard):
    before = np.ndarray.copy(npboard)
    z_x, z_y = find_num(npboard, 0)
    if z_y == 0: 
        return False, -1
    after = swap(npboard, (z_x, z_y), (z_x, z_y-1))
    cost = get_cost(before, after)
    return after, cost

def move_right(npboard):
    before = np.ndarray.copy(npboard)
    z_x, z_y = find_num(npboard, 0)
    if z_y == 2: 
        return False, -1
    after = swap(npboard, (z_x, z_y), (z_x, z_y+1))
    cost = get_cost(before, after)
    return after, cost

# return list of tuples:
# str direction, boardaftermove, cost
def move_math(npboard):
    valid_moves = ["left", "up", "down", "right"]
    movelist = []
    while len(valid_moves) is not 0:
        move = valid_moves.pop()
        result = np.empty_like(npboard)
        cost = -1
        if(move == "up"):
            result, cost = move_up(np.ndarray.copy(npboard))
        elif(move == "down"):
            result, cost = move_down(np.ndarray.copy(npboard))
        elif(move == "left"):
            result, cost = move_left(np.ndarray.copy(npboard))
        elif(move == "right"):
            result, cost = move_right(np.ndarray.copy(npboard))
        if(result is not False):
            movelist.append((move, result, cost))
    return movelist

#######
# end #todo, begin gameBoard
#######

class gameBoard:
    def __init__(self, starting_board):
        # numpy array representing 3x3 grid
        self.board = starting_board
        # todo: define frontier here as queue 
    def print(self):
        print(self.board)
        pass

    def is_swap_valid(self, location1, location2):
        def get_location(n):
            for i, row in enumerate(self.board):
                if n in row:
                    return i, np.where(row == n)[0][0]

        location1_x, location1_y = get_location(location1)
        location2_x, location2_y = get_location(location2)

        if location1_x == location2_x and location1_y == location2_y:
            # return print("invalid, same location swap")
            return True

        if abs(location1_x - location2_x) + abs(location1_y - location2_y) != 1:
            return False

        if (location1_x + location1_y == location2_x + location2_y) or \
                (location1_x - location1_y == location2_x - location2_y):
            return False

        return True
    
#######
# end gameBoard, begin gameMove
#######
    
class gameMove:
    def __lt__(self, other):
        selfPriority = (self.cost)
        otherPriority = (other.cost)
        return selfPriority < otherPriority
    def __init__(self, prevMove, boardAfterMove, move, depth, cost):
        # gameMove before move
        # type:  gameMove
        self.prevMove = prevMove
        # resulting board after move
        # type: gameBoard
        self.boardAfterMove = boardAfterMove
        # move that took place
        # type: string 
        #   up, down, left, right, and start
        self.move = move
        # cost at this node
        self.cost = cost
        # depth after move
        self.depth = depth
        # just_post prints only board after move is made
        # set to False to print before/after
    def print(self, just_post=True):
        print("Depth:", self.depth)
        print("Cost:", self.cost)
        print("Move:", self.move)
        if self.prevMove is not None:
            if not just_post:
                print("Pre move:\n", self.prevMove.boardAfterMove.board)
            print("Post move:\n", self.boardAfterMove.board)
        else:
            print("Start state:\n", self.boardAfterMove.board)
        print("---")

    def print_path(self):
        stack = [self]
        while self.prevMove is not None and self.move != "start":
            self = self.prevMove
            stack.append(self)
        for node in reversed(stack):
            node.print()


# def new_gameMoves2(self):
#     gameMoveList = [gameMove(self, gameBoard(boardafter), dir, self.depth + 1, self.cost + cost) 
#         for (dir, boardafter, cost) in validmoves]
#     return gameMoveList

# def new_gameMoves3(self):
#     gameMoveList = []
#     for (dir, boardafter, cost) in move_math(self.boardAfterMove.board):
#         gameMoveList.append(gameMove(self, gameBoard(boardafter), dir, self.depth + 1, self.cost + cost))

    def new_gameMoves(self):
        valid_moves = move_math(self.boardAfterMove.board)
        game_moves = [gameMove(self, gameBoard(board_after), direction, self.depth + 1, self.cost + move_cost) for direction, board_after, move_cost in valid_moves]
        return game_moves

    def is_solution(self):
        return np.array_equal(self.boardAfterMove.board, np.array(np.mat('1 2 3; 4 5 6; 7 8 0')))

    def get_id(self):
        return ''.join(str(y) for y in self.boardAfterMove.board)

#######
# end gameMove, begin solve
#######


# def solve(startingBoard, algorithm="ucs"):
#     """
#     Solve using specified algorithm:
#     - UCS: each move has cost of 1 
#     - A* with Misplaced Tile Heuristic
#     - A* with Euclidean Distance Heuristic
#     """

#     global misplaced_tile_heuristic
#     global euclidean_distance_heuristic
#     # set algorith here
#     if(algorithm == "ucs"):
#         misplaced_tile_heuristic = 0
#         euclidean_distance_heuristic = 0
#     elif(algorithm == "euclidean"):
#         misplaced_tile_heuristic = 0
#         euclidean_distance_heuristic = 1
#     elif(algorithm == "misplaced"):
#         misplaced_tile_heuristic = 1
#         euclidean_distance_heuristic = 0
#     else:
#         print("unknown algo selected???")
#         exit(-1)

#     seen_moves = {gameMove(None, startingBoard, "start", 0, 0).get_id(): True}
#     frontier = PriorityQueue()
#     gameBoardMoves = seen_moves.keys()
#     for move in gameBoardMoves:
#         frontier.put((move.cost, move))
#     nodes_expanded, queue_histmaxsize = 1, frontier.qsize()
#     while not frontier.empty():
#         prio, move = frontier.get()
#         if move.is_solution():
#             return move, (nodes_expanded, queue_histmaxsize)
#         move_id = move.get_id()
#         if move_id in seen_moves:
#             continue
#         seen_moves[move_id] = True
#         for newmove in move.new_gameMoves():
#             if newmove.get_id() not in seen_moves:
#                 frontier.put((newmove.cost, newmove))   
#         nodes_expanded += 1
#         if queue_histmaxsize < frontier.qsize():
#             queue_histmaxsize = frontier.qsize()
#     return False, (nodes_expanded, queue_histmaxsize)


def solve(startingBoard, algorithm="ucs"):
    """
    Solve using specified algorithm:
    - UCS
        each move has cost of 1 
        enqueue valid moves w/ priority queue?
        worst case n^4
    - A* with Misplaced Tile Heuristic
    - A* with Euclidean Distance Heuristic
        - not manhattan distance?         
    """
    if algorithm == "ucs":
        misplaced_tile_heuristic = 0
        euclidean_distance_heuristic = 0
    elif algorithm == "euclidean":
        misplaced_tile_heuristic = 0
        euclidean_distance_heuristic = 1
    elif algorithm == "misplaced":
        misplaced_tile_heuristic = 1
        euclidean_distance_heuristic = 0
    else:
        print("Unknown algorithm selected.")
        exit(-1)

    seen_moves = {}
    firstNode = gameMove(gameMove(None, startingBoard, "start", 0, 0), startingBoard, "start", 0, 0)
    seen_moves[firstNode.get_id()] = True
    frontier = PriorityQueue()
    gameBoardMoves = firstNode.new_gameMoves()
    for move in gameBoardMoves:
        frontier.put((move.cost, move))

    nodes_expanded = 1
    queue_histmaxsize = frontier.qsize()

    while not frontier.empty():
        prio, move = frontier.get()
        move_id = move.get_id()

        if move.is_solution():
            return move, (nodes_expanded, queue_histmaxsize)
        
        if move_id in seen_moves:
            continue
        else:
            seen_moves[move_id] = True
        
        moves = move.new_gameMoves()
        for newmove in moves:
            if newmove.get_id() not in seen_moves:
                frontier.put((newmove.cost, newmove))
                
        if queue_histmaxsize < frontier.qsize():
            queue_histmaxsize = frontier.qsize()
        nodes_expanded += 1

    return False, (nodes_expanded, queue_histmaxsize)
