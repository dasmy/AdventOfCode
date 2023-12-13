import numpy as np
from day_13 import INPUT_TEST, INPUT


def search(lines):
    pattern = np.asarray(lines, dtype=bool)
    for p, f in zip((pattern, pattern.T), (100, 1)):
        n = len(p)
        for i_split in range(1, n):
            maxlen = min(n-i_split, i_split)
            before = np.flipud(p[i_split - maxlen:i_split])
            after = p[i_split:i_split + maxlen]
            assert before.shape == after.shape
            if np.all(before == after):
                return i_split * f

    assert False


def day_13a(inp):
    total = 0
    lines = []
    for l in inp.split('\n'):
        if l:
            lines.append([s == '#' for s in l])
        else:
            total += search(lines)
            lines = []
    total += search(lines)

    return total


print(day_13a(INPUT_TEST))
print(day_13a(INPUT))
