import numpy as np
from day_06inp import INPUT

field = np.array([[char for char in row] for row in INPUT.split("\n")])

startpos = tuple(np.argwhere(field == "^")[0].tolist())
startdir = (-1, 0)


def rotate_90(dir):
    if dir == (-1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)


def advance(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])


num_cycles = 0
for r, c in np.argwhere(field == "."):
    input = field.copy()
    input[r, c] = "#"

    pos = startpos
    dir = startdir

    visited = set()
    visited.add((pos, dir))

    while True:
        newpos = advance(pos, dir)

        if (
            newpos[0] < 0
            or newpos[0] >= input.shape[0]
            or newpos[1] < 0
            or newpos[1] >= input.shape[1]
        ):
            # print("no cycle")
            break

        if input[*newpos] == "#":
            dir = rotate_90(dir)
        else:
            pos = newpos

            if (pos, dir) in visited:
                print(f"cycle {(pos, dir)} for obstacle at {(r, c)}")
                num_cycles += 1
                break

            visited.add((tuple(pos), tuple(dir)))

print(num_cycles)
