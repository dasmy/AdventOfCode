from copy import copy
from collections import deque
from day_23 import INPUT_TEST, INPUT


def day_23a(inp):
    grid = inp.split('\n')
    row = 0
    col = grid[row].find('.')
    assert col != -1

    max_row = len(grid)
    max_col = len(grid[0])

    DIRS = {
        '>': [(0, +1), ],
        '<': [(0, -1), ],
        'v': [(+1, 0), ],
        '^': [(-1, 0), ],
        '.': [(-1, 0), (+1, 0), (0, -1), (0, +1)],
        '#': []
    }

    maxsteps = 0
    todo = deque()
    todo.append((row, col, 0, set()))
    while todo:
        row, col, steps, done = todo.popleft()
        done = copy(done)
        done.add((row, col))

        if row + 1 == max_row:
            print(steps)
            maxsteps = max(steps, maxsteps)
        else:
            for drow, dcol in DIRS[grid[row][col]]:
                nextrow = row + drow
                nextcol = col + dcol

                if 0 <= nextrow < max_row and 0 <= nextcol < max_col:
                    if (nextrow, nextcol) not in done and grid[nextrow][nextcol] != '#':
                        todo.append((row+drow, col+dcol, steps+1, done))

    return maxsteps


print(day_23a(INPUT_TEST))
print(day_23a(INPUT))
