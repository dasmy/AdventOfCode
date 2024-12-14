import re
from operator import mul
from functools import reduce
from collections import defaultdict
from day_14inp import INPUT

xmax, ymax = 101, 103
steps = 100

pattern = re.compile(r"p=([\-0-9]*),([\-0-9]*) v=([\-0-9]*),([\-0-9]*)")

quadrants = defaultdict(lambda: 0)

for robot in INPUT.split("\n"):
    m = pattern.match(robot)
    x, y, vx, vy = map(int, m.groups())

    x_end = (x + vx * steps) % xmax
    y_end = (y + vy * steps) % ymax

    print(x, y, vx, vy, x_end, y_end)

    if x_end < xmax // 2:
        qx = -1
    elif x_end > xmax // 2:
        qx = 1
    else:
        qx = 0

    if y_end < ymax // 2:
        qy = -1
    elif y_end > ymax // 2:
        qy = 1
    else:
        qy = 0

    if qx != 0 and qy != 0:
        quadrants[(qx, qy)] += 1

print(reduce(mul, quadrants.values()))
