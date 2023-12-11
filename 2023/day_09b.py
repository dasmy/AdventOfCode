import numpy as np
from day_09 import INPUT_TEST, INPUT


def day_09b(inp):
    total = 0

    for line in inp.split('\n'):
        data = [np.asarray([int(s) for s in line.split(' ')], dtype=int)]
        first = []
        while not np.all(data[-1] == 0):
            first.append(data[-1][0])
            data.append(np.diff(data[-1]))

        current = 0
        for val in reversed(first):
            current = val - current

        total += current

    return total


print(day_09b(INPUT_TEST))
print(day_09b(INPUT))
