import numpy as np
from game_logic import gameBoard
from game_logic import solve
from rich import print as rprint
from rich.console import Console
from rich.text import Text
from rich.table import Table
import time

"""
Create the gameboard organized as with numpy:

[[1 2 3]
 [4 5 6]
 [7 8 0]]

Where 0 is the empty space.
"""

console = Console()

console.rule("")
text = Text("Welcome to our CS170 Project\n 8 Puzzle Solver\n made by \nPatrick L. (SID 862074479) \nNathan C. (SID 862292286) \nGency D. (SID 862243418)\nand Ivy D. (SID 862226470)")
# text.stylize("bold magenta", 66-9-4, 66-4)
# text.stylize("bold magenta", 90, 110)
text.stylize("bold magenta", 30, 30+16)
console.print(text, justify = "center")

test_case_1 = np.array(np.mat('1 2 3; 4 5 6; 7 8 0')) # trivial / completed
test_case_2 = np.array(np.mat('1 2 0; 4 5 3; 7 8 6')) # easy
test_case_3 = np.array(np.mat('8 7 1; 6 0 2; 5 4 3')) # oh boy
test_case_4 = np.array(np.mat('1 2 3; 4 5 6; 7 0 8')) # very easy
test_case_5 = np.array(np.mat('0 1 2; 4 5 3; 7 8 6')) # doable
test_case_6 = np.array(np.mat('1 2 3; 4 5 6; 8 7 0')) # IMPOSSIBLE

# lol
test_cases = [test_case_1, test_case_4, test_case_2, test_case_5, test_case_3, test_case_6]
# text = Text("")
console.print("\n")
console.rule("\n[bold magenta]8 PUZZLE SOLVER OPTIONS")

option = console.input("\nType '1' to use a default puzzle, or '2' to enter your own puzzle, or '3' to use a premade puzzle: ")

if ((int(option) == 1 )or (int(option) ==2) or (int(option) == 3) or (int(option) == 4)):
    if int(option) == 1:
        console.print("[bold navy_blue]Use Default Puzzle Option")
        console.print("The default puzzle is [bold navy_blue]'oh boy':")
        game_start_state = np.array(np.mat('8 7 1; 6 0 2; 5 4 3'))
        console.print(game_start_state, justify="center") # could probably justify left
        option = console.input("\nType '1' for UCS\nType '2' for A* with the Misplaced Tile heuristic\nType '3' for A* with the Euclidean Distance heuristic\n")
        option = int(option)
        if option == 1:
            algorithm="ucs"
            console.rule("\n[bold red]UCS Chosen")
        elif option == 2:
            algorithm = "misplaced"  
            console.rule("\n[bold blue]Misplaced Tile Heuristic Chosen")
        elif option == 3:
            algorithm = "euclidean"
            console.rule("\n[bold orange1]Euclidean Distance Heuristic Chosen")
        else:
            console.print("invalid input, exiting...")
            exit()
    elif int(option) == 2:
        console.print("[bold navy_blue]Enter Your Own Puzzle Option")
        console.print("To make your own puzzle do: '8 7 1; 6 0 2; 5 4 3'\nit will look like")
        console.print(np.array(np.mat('8 7 1; 6 0 2; 5 4 3')))
        input = console.input("\n Type your input: ")
        game_start_state = np.array(np.mat(input))
        console.print("Your puzzle will look like: \n", game_start_state)
        option = console.input("\nType '1' for UCS\nType '2' for A* with the Misplaced Tile heuristic\nType '3' for A* with the Euclidean Distance heuristic\n")
        option = int(option)
        if option == 1:
            algorithm="ucs"
            console.rule("\n[bold red]UCS Chosen")
        elif option == 2:
            algorithm = "misplaced"  
            console.rule("\n[bold blue]Misplaced Tile Heuristic Chosen")
        elif option == 3:
            algorithm = "euclidean"
            console.rule("\n[bold orange1]Euclidean Distance Heuristic Chosen")
        else:
            console.print("invalid input, exiting...")
            exit()
    elif int(option) == 3:
        console.print("[bold navy_blue]Choose a premade puzzle:", justify="center")
        table = Table(title="There are 6 to choose from:", show_header=False)
        # console.print("There are 6 to choose from:")
        # table.add_column()
        # table.add_column()
        table.add_row(f"1 trivial / completed:\n{test_case_1}" ,f"4 very easy:\n{test_case_4}")
        table.add_row(f"2 easy:\n{test_case_2}", f"5 doable:\n{test_case_5}")
        table.add_row(f"3 oh boy:\n{test_case_3}", f"6[bold green] IMPOSSIBLE[/bold green]:\n{test_case_6}")
        console.print(table, justify="center")
        input = console.input("Choose one of the six: ")
        input = int(input)
        if input == 1:
            game_start_state = test_case_1
        elif input == 2:
            game_start_state = test_case_2
        elif input == 3:
            game_start_state = test_case_3
        elif input == 4:
            game_start_state = test_case_4
        elif input == 5:
            game_start_state = test_case_5
        elif input == 6:
            game_start_state = test_case_6

        
        console.print("Your puzzle will look like: \n", game_start_state)
        option = console.input("\nType '1' for UCS\nType '2' for A* with the Misplaced Tile heuristic\nType '3' for A* with the Euclidean Distance heuristic\n")
        option = int(option)
        if option == 1:
            algorithm="ucs"
            console.rule("\n[bold red]UCS Chosen")
        elif option == 2:
            algorithm = "misplaced"  
            console.rule("\n[bold blue]Misplaced Tile Heuristic Chosen")
        elif option == 3:
            algorithm = "euclidean"
            console.rule("\n[bold orange1]Euclidean Distance Heuristic Chosen")
        else:
            console.print("invalid input, exiting...")
            exit()
    elif int(option) == 4:
        console.rule("\n[bold yellow]Benchmark all")
        # for each test case 1-6 run UCS, misplaced, euclidean
        for i in range(len(test_cases)):
            print("test {}".format(i))
            start_time = time.perf_counter()
            board = gameBoard(test_cases[i])
            lastmove, stats = solve(board, "ucs")
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print("\tucs\n\t\tnodes_expanded: {}\n\t\tqueue max: {}".format(stats[0], stats[1]))
            print(f"\t\tElapsed time: {elapsed_time} seconds")

            start_time = time.perf_counter()
            lastmove, stats = solve(board, "misplaced")
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print("\tmisplaced\n\t\tnodes_expanded: {}\n\t\tqueue max: {}".format(stats[0], stats[1]))
            print(f"\t\tElapsed time: {elapsed_time} seconds")

            start_time = time.perf_counter()
            lastmove, stats = solve(board, "euclidean")
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print("\teuclidean\n\t\tnodes_expanded: {}\n\t\tqueue max: {}".format(stats[0], stats[1]))
            print(f"\t\tElapsed time: {elapsed_time} seconds")
        exit()
    with console.status("Running algorithm", spinner="simpleDotsScrolling"):
        start_time = time.perf_counter()
        board = gameBoard(game_start_state)
        lastmove, stats = solve(board, algorithm)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        if lastmove is False:
            print("no solution found!")
        else:
            print("soln found!")
            lastmove.print_path()
        print("nodes expanded: {}\nqueue max: {}".format(stats[0], stats[1]))
        print("algo: " + algorithm)
        exit()
    

else:
    print("here")



exit()

# works
# game_start_state = np.array(np.mat('1 2 3; 4 5 6; 7 0 8'))

# also works
# game_start_state = np.array(np.mat('1 2 3; 4 5 6; 0 7 8'))

# works
# game_start_state = np.array(np.mat('0 1 2; 4 5 3; 7 8 6'))

# works? need to verify soln
game_start_state = np.array(np.mat('8 7 1; 6 0 2; 5 4 3'))

# should quit once all possible states are expanded
# game_start_state = test_case_6 = np.array(np.mat('1 2 3; 4 5 6; 8 7 0')) # IMPOSSIBLE


# init
board = gameBoard(game_start_state)

# ucs, misplaced, or euclidean
algorithm="euclidean"
lastmove, stats = solve(board, algorithm)

if lastmove is False:
    print("no solution found!")
else:
    print("soln found!")
    lastmove.print_path()
print("nodes expanded: {}\nqueue max: {}".format(stats[0], stats[1]))
print("algo: " + algorithm)
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


