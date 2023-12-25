from copy import copy
from collections import deque
from day_23 import INPUT_TEST, INPUT


def day_23b(inp):
    grid = inp.split('\n')
    row = 0
    col = grid[row].find('.')
    assert col != -1

    max_row = len(grid)
    max_col = len(grid[0])

    maxsteps = 0
    todo = deque()
    todo.append((row, col, 0, (-1, -1), set()))
    while todo:
        row, col, steps, prev, done = todo.pop()
        done = copy(done)
        done.add((row, col))

        if row + 1 == max_row:
            print('--x ', steps, maxsteps)
            maxsteps = max(steps, maxsteps)
        else:
            while True:
                assert grid[row][col] != '#'
                nextposs = []
                for drow, dcol in (-1, 0), (+1, 0), (0, -1), (0, +1):
                    nextrow = row + drow
                    nextcol = col + dcol
                    nextpos = (nextrow, nextcol)

                    if nextpos == prev:
                        continue
                    if nextpos in done:
                        continue
                    if grid[nextrow][nextcol] == '#':
                        continue

                    nextposs.append((*nextpos, steps+1, (row, col), done))

                if len(nextposs) == 1:
                    row, col, steps, prev, done = nextposs[0]
                    done.add((row, col))

                    if row + 1 == max_row:
                        maxsteps = max(steps, maxsteps)
                        print('--> ', steps, maxsteps)
                        break
                else:
                    todo.extend(nextposs)
                    break

    return maxsteps


print(day_23b(INPUT_TEST))
print(day_23b(INPUT))
