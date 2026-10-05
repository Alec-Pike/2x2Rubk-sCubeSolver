from solver import Solver
import algorithms


bfs_solver = Solver(algorithms.bfs)
bfs_solver.cube.print_cube()
print("-" * 20)
print("After scrambling (depth=5):")
scrambled_state, moves_taken = bfs_solver.scramble(5, rand_seed=42)
print("Moves taken:", moves_taken)
print("-" * 20)
print("BFS solution:")
print(bfs_solver.solve())
print("-" * 20)
print("DFS solution:")
dfs_solver = Solver(algorithms.dfs, initial_state=scrambled_state)
print(dfs_solver.solve(max_depth=15))
print("-" * 20)
print("A* solution:")
a_star_solver = Solver(algorithms.a_star, initial_state=scrambled_state)
print(a_star_solver.solve())