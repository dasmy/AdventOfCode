from collections import deque
import numpy as np
from day_21 import INPUT_TEST, INPUT


def day_21a(grid, maxsteps):
    for irow, r in enumerate(grid):
        for icol, c in enumerate(r):
            if c == 'S':
                row = irow
                col = icol

    max_row = len(grid)
    max_col = len(grid[0])

    todo = deque()
    todo.append((row, col, maxsteps))
    visited = set()
    visited.add((row, col, maxsteps))
    reachable = 0

    while todo:
        row, col, steps = todo.popleft()

        if steps == 0:
            reachable += 1
        else:
            for dr, dc in (-1, 0), (+1, 0), (0, -1), (0, +1):
                new_row = row + dr
                new_col = col + dc

                if grid[new_row % max_row][new_col % max_col] in '.S':
                    new = (new_row, new_col, steps-1)
                    if new not in visited:
                        todo.append(new)
                        visited.add(new)

    return reachable


def day_21b(inp, max_steps):
    grid = inp.split('\n')
    max_row = len(grid)
    max_col = len(grid[0])

    assert max_row == max_col

    start = max_steps % max_row

    reachable = []
    incr, iincr = None, None

    while start <= max_steps:
        if incr is None:
            # we know, the numbers grow quadratic --> search for a cycle, i.e. a constant second derivative
            reachable.append(day_21a(grid, start))
            # print(start, reachable)
            if len(reachable) >= 4:
                delta = np.diff(reachable)
                ddelta = np.diff(reachable, 2)
                print("        ", delta, ddelta)
                if ddelta[-1] == ddelta[-2]:
                    iincr = ddelta[-1]
                    incr = delta[-1]
                    print(f'Found ddiff increment: {iincr}')
        else:
            incr += iincr
            reachable.append(reachable[-1] + incr)

        start += max_row

    return reachable[-1]


print(day_21b(INPUT_TEST, 6))
print(day_21b(INPUT_TEST, 10))
print(day_21b(INPUT_TEST, 50))
print(day_21b(INPUT_TEST, 100))
print(day_21b(INPUT_TEST, 500))
print(day_21b(INPUT_TEST, 1000))
print(day_21b(INPUT_TEST, 5000))
print(day_21b(INPUT, 26501365))
