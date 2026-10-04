from collections import deque
import heapq
from typing import Callable, Optional, Any


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
    get_successors: Callable
) -> Optional[list[str]]:
    """Depth-First Search implementation."""
    pass #TODO


def a_star(
    start_state: tuple[int, ...],
    goal_state: tuple[int, ...],
    get_successors_fn: Callable,
    heuristic_fn: Optional[Callable[[tuple[int, ...], tuple[int, ...]], float]] = None
) -> Optional[list[str]]:
    """A* Search algorithm."""
    if heuristic_fn is None:
        # Simple heuristic: mismatched sticker count divided by max stickers affected per turn (8)
        heuristic_fn = lambda s, g: sum(a != b for a, b in zip(s, g)) / 8.0

    if start_state == goal_state:
        return []

    counter = 0  # Priority queue tie-breaker
    open_set = [(heuristic_fn(start_state, goal_state), 0, counter, start_state, [])]
    g_scores = {start_state: 0}

    while open_set:
        _, g, _, current_state, path = heapq.heappop(open_set)

        if current_state == goal_state:
            return path

        if g > g_scores.get(current_state, float("inf")):
            continue

        for next_state, move in get_successors_fn(current_state):
            tentative_g = g + 1
            if tentative_g < g_scores.get(next_state, float("inf")):
                g_scores[next_state] = tentative_g
                h = heuristic_fn(next_state, goal_state)
                counter += 1
                heapq.heappush(
                    open_set,
                    (tentative_g + h, tentative_g, counter, next_state, path + [move])
                )

    return None