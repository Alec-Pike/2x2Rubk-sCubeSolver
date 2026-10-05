from pocketcube import PocketCube
import random
from typing import Callable, Optional, Any

class Solver:

    ALL_MOVES = {"U", "u", "R", "r", "F", "f"}

    def __init__(self, alg: Callable, initial_state: Optional[tuple[int, ...]] = PocketCube.DEFAULT_STATE):
        self.cube = PocketCube(initial_state)
        self.available_moves = set(Solver.ALL_MOVES)
        self.alg = alg


    def _make_move(self, move: str) -> bool:
        if move not in self.available_moves:
            return False

        result = self.cube.make_move(move)
        if not result:
            return False

        self.available_moves = set(Solver.ALL_MOVES)
        self.available_moves.remove(move.swapcase()) # Don't do the reverse of the move we just did!

        return True


    def is_solved(self):
        return self.cube.state == PocketCube.DEFAULT_STATE


    def scramble(self, depth: int, rand_seed: int = None) -> tuple[tuple[int, ...], list[str]]:
        if rand_seed != None:
            random.seed(rand_seed)

        # iterable and always has same ordering
        # edit suggested by Google Gemini
        all_moves = sorted(Solver.ALL_MOVES)

        moves_taken = []
        for i in range(depth):
            result = False
            move = ""
            while not result:
                move = random.choice(all_moves)
                result = self._make_move(move)
            moves_taken.append(move)

        self.available_moves = set(Solver.ALL_MOVES) # Reset moves
        self.cube.print_cube()
        return self.cube.state, moves_taken


    # method written by Google Gemini
    @staticmethod
    def get_successors(state: tuple[int, ...]) -> list[tuple[tuple[int, ...], str]]:
        """Generates reachable neighbor states and the move used to reach them."""
        all_moves = sorted(Solver.ALL_MOVES)
        successors = []
        for move in all_moves:
            temp_cube = PocketCube(state)
            temp_cube.make_move(move)
            successors.append((temp_cube.state, move))
        return successors


    # method written by Google Gemini
    def solve(self, apply_moves: bool = True, **kwargs) -> tuple[Optional[list[str]], int]:
        """Executes self.alg to solve the cube.

        Args:
            apply_moves: If True, applies the resulting move sequence to self.cube.
            **kwargs: Extra parameters passed directly to self.alg (e.g. heuristic functions).

        Returns:
            List of move characters forming the solution, or None if unsolvable.
            Integer number of nodes explored. 
        """
        if self.is_solved():
            return [], 0

        # Pass state and successor generator to the algorithm
        solution_path, nodes_explored = self.alg(
            start_state=self.cube.state,
            goal_state=PocketCube.DEFAULT_STATE,
            get_successors=Solver.get_successors,
            **kwargs
        )

        if solution_path and apply_moves:
            for move in solution_path:
                self.cube.make_move(move)
            self.available_moves = set(Solver.ALL_MOVES)

        return solution_path, nodes_explored


if __name__ == "__main__": # testing
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