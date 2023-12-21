from collections import deque
from day_21 import INPUT_TEST, INPUT


def day_21a(inp, steps):
    grid = inp.split('\n')

    for irow, r in enumerate(grid):
        for icol, c in enumerate(r):
            if c == 'S':
                row = irow
                col = icol

    max_row = len(grid)
    max_col = len(grid[0])

    todo = deque()
    todo.append((row, col, steps))
    visited = set()
    visited.add((row, col, steps))
    reachable = 0

    while todo:
        row, col, steps = todo.popleft()

        if steps == 0:
            reachable += 1
        else:
            for dr, dc in (-1, 0), (+1, 0), (0, -1), (0, +1):
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < max_row and 0 <= new_col < max_col:
                    if grid[new_row][new_col] in '.S':
                        new = (new_row, new_col, steps-1)
                        if new not in visited:
                            todo.append(new)
                            visited.add(new)

    return reachable


print(day_21a(INPUT_TEST, 6))
print(day_21a(INPUT, 64))
