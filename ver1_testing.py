import numpy as np
import math
from copy import copy
from queue import PriorityQueue

misplaced_tile_heuristic = 0
euclidean_distance_heuristic = 0

# decide here heuristics
def get_cost(b1, b2):
    """
    if misplaced_tile_heuristic = 1, cost is now how many tiles are misplaced.
    if euclidean_distance_heuristic = 1, cost is now the sum of the physical distance of each tile misplaced.
    """

    if misplaced_tile_heuristic:
        counter_check = 0
        misplaced_heuristic_count = 0
        for x in range(len(b2)):
            # print(b2[x])
            for y in range(len(b2[x])): # go through each column in each row 
                # print(b2[x][y])
                counter_check +=1
                if (counter_check == 9): # when it's 9, revert back to 0 because we dont have 0
                    counter_check = 0
                if (counter_check != b2[x][y]): # if it don't match, add 1 ;D
                    # print("count check "+str(counter_check))
                    # print(b2[x][y])
                    misplaced_heuristic_count +=1
        # print("the new heuristic "+ str(misplaced_heuristic_count))
        return misplaced_heuristic_count+1 # because each move has a cost of one
                
    if euclidean_distance_heuristic:
        counter_check = 0
        euclidean_distance_heuristic_count = 0
        for x in range(len(b2)):
            # print(b2[x])
            for y in range(len(b2[x])):
                # print(b2[x][y])
                counter_check +=1
                if (counter_check == 9):
                    counter_check = 0
                if (counter_check != b2[x][y]):
                    # print("count check "+str(counter_check))
                    # print(b2[x][y])
                    if (counter_check > b2[x][y]): # to avoid duplicates
                        for findIndexX in range(len(b2)):
                            for findIndexY in range(len(b2[findIndexX])):
                                # for loop is to find the x and y location
                                if b2[findIndexX][findIndexY] == counter_check:
                                    # euclidean math stuff
                                    a = abs(findIndexX-x)
                                    b = abs(findIndexY-y)
                                    if (a != 0 or b !=0):
                                        c = math.sqrt(pow(a,2) + pow(b,2))
                                    else: #it's never in here, was just scared
                                        c = max(a,b)
                                    euclidean_distance_heuristic_count += c
                                    # print(c)
        # print(euclidean_distance_heuristic_count+1)
        return euclidean_distance_heuristic_count+1
                                
    return 1

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

# return x, y of '0' character in array
def find_num(npboard, val):
    # should only be one object so element 0, 0 only
    arrobj = np.argwhere(npboard == val)
    return arrobj[0][0], arrobj[0][1]

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

class gameBoard:
    def __init__(self, starting_board):
        # numpy array representing 3x3 grid
        self.board = starting_board
        # todo: define frontier here as queue 
    ########
    # helper functions
    ########
    def print(self):
        print(self.board)
        pass
    # todo: need to refactor to return 0 (not valid) or 1 (valid)
    # also check if one of two being swapped is 0
    def is_swap_valid(self, location1, location2):
        """
        Swap function
        Swaps two numbers in a given array

        for example: this swaps bottom right with bottom middle.
        swap(arr[2][1], arr[2][2])
        
        [[1 2 3]        [[1 2 3]
        [4 5 6]    -->   [4 5 6]
        [7 8 0]]         [7 0 8]]

        LOGIC:
        Check if one of the numbers are 0 (empty), if not, illegal move
        Can only swap with a number orthogonally
        """
        location1_x = -1
        location2_x = -1

        # find the x and y of location 1
        for i in range(len(self.board)):
            location1_y = np.where(self.board[i] == location1)
            if location1_y[0].size > 0 :
                print("x: "+ str(i) + " y: "+ str(location1_y[0][0]))
                location1_x = i
                location1_y = location1_y[0][0]
                break

        # find the x and y of location 2, can probably combine into one for loop
        for i in range(len(self.board)):
            location2_y = np.where(self.board[i] == location2)
            if location2_y[0].size > 0:
                print("x: "+ str(i) + " y: "+ str(location2_y[0][0]))
                location2_x = i
                location2_y = location2_y[0][0]
                break

        if (location1_x == location2_x and location1_y == location2_y):
            # return print("invalid, same location swap")
            return True
        
        if ( (location1_x - 1  == location2_x or  location1_x + 1  == location2_x or location1_x  == location2_x)
            and (location1_y -1 == location2_y or location1_y + 1 == location2_y or  location1_y == location2_y)):
            if (( location1_x + 1 == location2_x) and (location1_y + 1 == location2_y)):
                # print("diagonally related")
                return False
            elif (( location1_x + location1_y == location2_y + location2_x)):
                # print("reverse diagonally related") 
                return False
            else:
                # print("valid")
                return True
        else:
            return False
    ########
    # operator functions    
    ########
    # refer to moving empty space (represented by zero)
    # for example here, valid operations move_up and move_left:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 0]]

    # move 0 counter-clockwise in a 2x2 cell pattern rotates non 0 characters clockwise
    # could be defined as an operator cost of 4
    # interesting but unnecessary since it can be achieved by above 4 moves


class gameMove:
    # add comparability
    # fix incompatibility with priority queue
    # https://stackoverflow.com/questions/9292415/i-notice-i-cannot-use-priorityqueue-for-objects
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
        print("Depth: {}".format(self.depth))
        print("Cost: {}".format(self.cost))
        print("Move: {}".format(self.move))
        # objs printed below are type numpy.ndarray
        if self.prevMove is not None:
            if(just_post is False):
                print("Pre move: \n{}".format(self.prevMove.boardAfterMove.board))
            print("Postmove: \n{}".format(self.boardAfterMove.board))
        else:
            print("Start state: \n{}".format(self.boardAfterMove.board))  
        print("---")
        return
    
    # print from start to finish the moves that were taken
    # takes gameMove object for position to start with
    # reverse traversal
    def print_path(self):
        currentgameBoard = self
        stack = []
        # append current node to stack
        stack.append(currentgameBoard)
        while currentgameBoard.prevMove is not None and currentgameBoard.move is not "start":
            currentgameBoard = currentgameBoard.prevMove
            stack.append(currentgameBoard)
        # pop from stack start to finish
        while stack:
            curnode = stack.pop()
            curnode.print()
        pass

    # return a list of gameMoves
    # because of helper functions, returns in order:
    # right, up, down, left (not present if not valid move)
    def new_gameMoves(self):
        gameMoveList = []
        initboard = self.boardAfterMove.board
        validmoves = move_math(initboard)
        # print(validmoves)
        for (dir, boardafter, cost) in validmoves:
            gameMoveList.append(gameMove(self, gameBoard(boardafter), dir, self.depth + 1, self.cost + cost))

        return gameMoveList
    
    def is_solution(self):
        return np.array_equal(self.boardAfterMove.board, np.array(np.mat('1 2 3; 4 5 6; 7 8 0')))

    def get_id(self):
        s = ""
        for x in self.boardAfterMove.board:
            s += ''.join(str(y) for y in x)
        return s

### outside of class

# def board_str_id(gameBoard):
#     # return ''.join(str(x) for x in gameBoard.board)
#     s = ""
#     for x in gameBoard.board:
#         s += ''.join(str(y) for y in x)
#     return s

# accept type gameBoard in variable startingBoard
# algorithm: ucs, euclidean, or misplaced
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

    global misplaced_tile_heuristic
    global euclidean_distance_heuristic
    # set algorith here
    if(algorithm == "ucs"):
        misplaced_tile_heuristic = 0
        euclidean_distance_heuristic = 0
    elif(algorithm == "euclidean"):
        misplaced_tile_heuristic = 0
        euclidean_distance_heuristic = 1
    elif(algorithm == "misplaced"):
        misplaced_tile_heuristic = 1
        euclidean_distance_heuristic = 0
    else:
        print("unknown algo selected???")
        exit(-1)

    # init
    # dict is hashmap in python
    seen_moves = {}
    # create first node in linked list
    firstNode = gameMove(gameMove(None, startingBoard, "start", 0, 0), startingBoard, "start", 0, 0)
    # save first board hash
    seen_moves[firstNode.get_id()] = True


    # define frontier
    frontier = PriorityQueue()

    # load queue with initial possible moves
    # move should be gameMove object
    gameBoardMoves = firstNode.new_gameMoves()
    for move in gameBoardMoves:
        # queue each move
        frontier.put((move.cost, move))
        # save board hash
        # init so should not exist
        # b_id = board_str_id(move.boardAfterMove)
        # # print(b_id)
        # seen_moves[b_id] = True
    
    # prio calculated based on cost f(n) = g(n) + h(n)
    # g(n) always 1
    # h(n) based on algorithm (always 0 if UCS)

    # return some stats
    nodes_expanded = 1 # include start
    # keep track of maximum historical queue size
    queue_histmaxsize = frontier.qsize()

    # while not solved
    while(frontier.empty() is False):
        # select move with lowest cost (priority queue)
        prio, move = frontier.get()
        # print("current move: ")
        # move.print()

        move_id = move.get_id()

        # exit condition
        # if move is solution (maybe change for a*)
        # return solution
        if(move.is_solution()):
            print("found!")
            # todo: return queue stats
            return move, (nodes_expanded, queue_histmaxsize)
        
        # move was not solution
        
        # save move id
        if(move_id in seen_moves):
            # move is seen
            # means this is creates loop
            # want acyclic (DAG)
            continue
        else:
            # hash indicates traversal of node
            seen_moves[move_id] = True
        
        
        # push new moves after taking this move
        moves = move.new_gameMoves()
        # print("adding moves")
        for newmove in moves:
            # push if key does not exist
            if(newmove.get_id() not in seen_moves):
                frontier.put((newmove.cost, newmove))   
                # newmove.print()
        # print("adding moves end")

        # maintain historically largest queue size
        if queue_histmaxsize < frontier.qsize():
            queue_histmaxsize = frontier.qsize()
        # add to expanded nodes
        nodes_expanded += 1
    # execution to this point means
    # all possible moves have been exhausted
    # no solution found
    return False, (nodes_expanded, queue_histmaxsize)
    
