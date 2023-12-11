import numpy as np
from day_09 import INPUT_TEST, INPUT


def day_09a(inp):
    total = 0

    for line in inp.split('\n'):
        data = [np.asarray([int(s) for s in line.split(' ')], dtype=int)]
        last = []
        while not np.all(data[-1] == 0):
            last.append(data[-1][-1])
            data.append(np.diff(data[-1]))

        total += sum(last)

    return total


print(day_09a(INPUT_TEST))
print(day_09a(INPUT))
