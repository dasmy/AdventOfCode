import re
import numpy as np
from day_14inp import INPUT

xmax, ymax = 101, 103

pattern = re.compile(r"p=([\-0-9]*),([\-0-9]*) v=([\-0-9]*),([\-0-9]*)")

for steps in range(100000):
    field = np.zeros((xmax, ymax), dtype=str)
    field[:, :] = "."

    for robot in INPUT.split("\n"):
        m = pattern.match(robot)
        x, y, vx, vy = map(int, m.groups())

        x_end = (x + vx * steps) % xmax
        y_end = (y + vy * steps) % ymax

        field[x_end, y_end] = "*"

    for row in field:
        if np.count_nonzero(row == "*") > 15:
            for col in field.T:
                if np.count_nonzero(col == "*") > 15:
                    print("\n".join("".join(row) for row in field.T))
                    print(steps)
                    input()
                    break
            else:
                continue
            break
