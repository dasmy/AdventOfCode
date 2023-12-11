import numpy as np
from day_11 import INPUT_TEST, INPUT


def day_11a(inp):
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
        px[px > x] += 1

    for y in reversed(empty_y):
        py[py > y] += 1

    dx = np.abs(px[np.newaxis, :] - px[:, np.newaxis])
    dy = np.abs(py[np.newaxis, :] - py[:, np.newaxis])
    delta = dx + dy

    return np.sum(delta) // 2


print(day_11a(INPUT_TEST))
print(day_11a(INPUT))
