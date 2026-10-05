from solver import Solver
import algorithms
from time import time

print("""
Welcome to the 2x2 Rubik's Cube solver!
Here's how it works:

The cube state is represented as a 24-element tuple of integers (0 through 5):
    0 = White  (Up)
    1 = Green  (Left)
    2 = Red    (Front)
    3 = Blue   (Right)
    4 = Orange (Back)
    5 = Yellow (Down)

The cube faces are stored in this order:
        00  01
          Up
        02  03

04  05  06  07  08  09  10  11
 Left   Front   Right    Back
12  13  14  15  16  17  18  19

        20  21
         Down
        22  23

So for example, the default solved state would be:
0, 0, 0, 0,  # Up (W)
1, 1, 2, 2, 3, 3, 4, 4,  # Upper ring (G, R, B, O)
1, 1, 2, 2, 3, 3, 4, 4,  # Lower ring (G, R, B, O)
5, 5, 5, 5,  # Down (Y)

Or as just a string of numbers:
000011223344112233445555

Please input a string of numbers in this format, or enter nothing for a random configuration:
""")
scramble_state = input("> ")
bfs_slv = None
if scramble_state == "":
    bfs_slv = Solver(algorithms.bfs)
    print("Scrambling with depth = 10")
    scramble_state, moves_taken = bfs_slv.scramble(10)
    print("Moves taken:", moves_taken)
else:
    scramble_state = tuple([int(n) for n in scramble_state])
    bfs_slv = Solver(algorithms.bfs, initial_state=scramble_state)
    print("Starting state:")
    bfs_slv.cube.print_cube()

print("-" * 50)
print("Solving with BFS...")
start_time = time()
bfs_solution, bfs_nodes = bfs_slv.solve()
bfs_time = time() - start_time
print("BFS solution:", bfs_solution)
print("Cost:", len(bfs_solution))
print("Nodes expanded:", bfs_nodes)
print("Time:", bfs_time)

print("-" * 50)
print("Solving with DFS (depth limit 15)...")
dfs_slv = Solver(algorithms.dfs, initial_state=scramble_state)
start_time = time()
dfs_solution, dfs_nodes = dfs_slv.solve(max_depth=15)
dfs_time = time() - start_time
print("DFS solution:", dfs_solution)
print("Cost:", len(dfs_solution))
print("Nodes expanded:", dfs_nodes)
print("Time:", dfs_time)

print("-" * 50)
print("Solving with A*...")
a_star_slv = Solver(algorithms.a_star, initial_state=scramble_state)
start_time = time()
a_star_solution, a_star_nodes = a_star_slv.solve()
a_star_time = time() - start_time
print("A* solution:", a_star_solution)
print("Cost:", len(a_star_solution))
print("Nodes expanded:", a_star_nodes)
print("Time:", dfs_time)