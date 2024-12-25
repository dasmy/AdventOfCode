from day_25inp import INPUT
from itertools import product
import numpy as np

keys = list()
locks = list()
for item in INPUT.split("\n\n"):
    pins = [-1, -1, -1, -1, -1]
    rows = list(item.split("\n"))
    if rows[0] == "#" * 5:
        # lock
        assert rows[-1] == "." * 5
        for row in rows:
            for p, val in enumerate(row):
                if val == "#":
                    pins[p] += 1
        locks.append(np.array(pins))
    elif rows[-1] == "#" * 5:
        # key
        assert rows[-1] == "#" * 5
        for row in rows:
            for p, val in enumerate(row):
                if val == "#":
                    pins[p] += 1
        keys.append(np.array(pins))
    else:
        assert False

count = 0
for key, lock in product(keys, locks):
    if np.any(key + lock > 5):
        continue
    else:
        count += 1

print(count)
