import numpy as np
from day_06inp import INPUT

input = np.array([[char for char in row] for row in INPUT.split("\n")])

pos = np.argwhere(input == "^")[0]
dir = [-1, 0]


def rotate_90(dir):
    if dir == [-1, 0]:
        return [0, 1]
    elif dir == [0, 1]:
        return [1, 0]
    elif dir == [1, 0]:
        return [0, -1]
    elif dir == [0, -1]:
        return [-1, 0]


input[*pos] = "X"

while True:
    newpos = pos + dir

    if (
        newpos[0] < 0
        or newpos[0] >= input.shape[0]
        or newpos[1] < 0
        or newpos[1] >= input.shape[1]
    ):
        break

    if input[*newpos] == "#":
        dir = rotate_90(dir)
    else:
        pos = newpos
        input[*newpos] = "X"

for row in input:
    print("".join(row))

print(np.count_nonzero(input == "X"))
