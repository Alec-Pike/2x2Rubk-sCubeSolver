from collections import deque
import heapq
from typing import Callable, Optional, Any

# All functions written by Google Gemini

def bfs(
    start_state: tuple[int, ...],
    goal_state: tuple[int, ...],
    get_successors: Callable
) -> Optional[list[str]]:
    """Breadth-First Search implementation."""
    if start_state == goal_state:
        return []

    queue = deque([(start_state, [])])
    visited = {start_state}

    while queue:
        current_state, path = queue.popleft()

        for next_state, move in get_successors(current_state):
            if next_state == goal_state:
                return path + [move]
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))

    return None


def dfs(
    start_state: tuple[int, ...],
    goal_state: tuple[int, ...],
    get_successors: Callable,
    max_depth: Optional[int] = None
) -> Optional[list[str]]:
    """Depth-First Search (DFS) / Depth-Limited Search (DLS).

    Args:
        start_state: Starting cube state tuple.
        goal_state: Target solved cube state tuple.
        get_successors: Function generating (next_state, move) tuples.
        max_depth: Optional integer limit on search depth. If set, limits path length.

    Returns:
        List of move strings if a path is found, otherwise None.
    """
    path_visited = {start_state}

    def _dfs(current_state: tuple[int, ...], path: list[str]) -> Optional[list[str]]:
        if current_state == goal_state:
            return path

        # Halt search along this branch if max depth is reached
        if max_depth is not None and len(path) >= max_depth:
            return None

        for next_state, move in get_successors(current_state):
            # Avoid cycles along the current branch path
            if next_state not in path_visited:
                path_visited.add(next_state)
                
                result = _dfs(next_state, path + [move])
                if result is not None:
                    return result
                
                # Backtrack when exiting branch
                path_visited.remove(next_state)

        return None

    return _dfs(start_state, [])


def a_star(
    start_state: tuple[int, ...],
    goal_state: tuple[int, ...],
    get_successors: Callable,
    heuristic: Optional[Callable[[tuple[int, ...], tuple[int, ...]], float]] = None
) -> Optional[list[str]]:
    """A* Search algorithm."""
    if heuristic is None:
        # Simple heuristic: mismatched sticker count divided by max stickers affected per turn (8)
        heuristic = lambda s, g: sum(a != b for a, b in zip(s, g)) / 8.0

    if start_state == goal_state:
        return []

    counter = 0  # Priority queue tie-breaker
    open_set = [(heuristic(start_state, goal_state), 0, counter, start_state, [])]
    g_scores = {start_state: 0}

    while open_set:
        _, g, _, current_state, path = heapq.heappop(open_set)

        if current_state == goal_state:
            return path

        if g > g_scores.get(current_state, float("inf")):
            continue

        for next_state, move in get_successors(current_state):
            tentative_g = g + 1
            if tentative_g < g_scores.get(next_state, float("inf")):
                g_scores[next_state] = tentative_g
                h = heuristic(next_state, goal_state)
                counter += 1
                heapq.heappush(
                    open_set,
                    (tentative_g + h, tentative_g, counter, next_state, path + [move])
                )

    return None