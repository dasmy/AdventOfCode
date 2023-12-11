import numpy as np
from day_11 import INPUT_TEST, INPUT


def day_11b(inp, expansion = 1):
    lines = inp.split('\n')
    field = np.zeros((len(lines), len(lines[0])), dtype=bool)

    px, py = [], []
    for y, (f, l) in enumerate(zip(field, lines)):
        for x, c in enumerate(l):
            if c == '#':
                f[x] = True
                px.append(x)
                py.append(y)
            else:
                assert c == '.'

    px = np.asarray(px)
    py = np.asarray(py)

    empty_y = []
    for irow, row in enumerate(field):
        if np.all(row == False):
            empty_y.append(irow)

    empty_x = []
    for icol, col in enumerate(field.T):
        if np.all(col == False):
            empty_x.append(icol)

    for x in reversed(empty_x):
        px[px > x] += expansion - 1

    for y in reversed(empty_y):
        py[py > y] += expansion - 1

    dx = np.abs(px[np.newaxis, :] - px[:, np.newaxis])
    dy = np.abs(py[np.newaxis, :] - py[:, np.newaxis])
    delta = dx + dy

    return np.sum(delta) // 2


print(day_11b(INPUT_TEST, expansion=2))
print(day_11b(INPUT_TEST, expansion=10))
print(day_11b(INPUT_TEST, expansion=100))
print(day_11b(INPUT_TEST, expansion=1000000))
print(day_11b(INPUT, expansion=1000000))
