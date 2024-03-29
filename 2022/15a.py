input = '''Sensor at x=2300471, y=2016823: closest beacon is at x=2687171, y=2822745
Sensor at x=1315114, y=37295: closest beacon is at x=1671413, y=43557
Sensor at x=1039523, y=3061589: closest beacon is at x=1570410, y=3710085
Sensor at x=214540, y=3768792: closest beacon is at x=-355567, y=3900317
Sensor at x=1641345, y=3524291: closest beacon is at x=1570410, y=3710085
Sensor at x=1016825, y=1450262: closest beacon is at x=745731, y=2000000
Sensor at x=2768110, y=3703050: closest beacon is at x=3133588, y=3984216
Sensor at x=2213658, y=3522463: closest beacon is at x=1570410, y=3710085
Sensor at x=3842967, y=3381135: closest beacon is at x=3839159, y=3421933
Sensor at x=3952516, y=2683159: closest beacon is at x=3213800, y=2708360
Sensor at x=172892, y=369117: closest beacon is at x=-228964, y=1438805
Sensor at x=3999720, y=3498306: closest beacon is at x=3839159, y=3421933
Sensor at x=1596187, y=307084: closest beacon is at x=1671413, y=43557
Sensor at x=3863253, y=3406760: closest beacon is at x=3839159, y=3421933
Sensor at x=3927553, y=3450758: closest beacon is at x=3839159, y=3421933
Sensor at x=2774120, y=3228484: closest beacon is at x=2687171, y=2822745
Sensor at x=3897140, y=3418751: closest beacon is at x=3839159, y=3421933
Sensor at x=1880329, y=2843697: closest beacon is at x=2687171, y=2822745
Sensor at x=33790, y=3243415: closest beacon is at x=-355567, y=3900317
Sensor at x=438583, y=2647769: closest beacon is at x=745731, y=2000000
Sensor at x=1540347, y=3177380: closest beacon is at x=1570410, y=3710085
Sensor at x=3120086, y=3997791: closest beacon is at x=3133588, y=3984216
Sensor at x=3428967, y=3105227: closest beacon is at x=3213800, y=2708360
Sensor at x=2898335, y=1037911: closest beacon is at x=3213800, y=2708360
Sensor at x=3456260, y=3578627: closest beacon is at x=3839159, y=3421933
Sensor at x=1859971, y=3999725: closest beacon is at x=1570410, y=3710085
Sensor at x=3147730, y=3999322: closest beacon is at x=3133588, y=3984216
Sensor at x=3920847, y=71575: closest beacon is at x=3826138, y=-255533
Sensor at x=956723, y=3999438: closest beacon is at x=1570410, y=3710085
Sensor at x=1193760, y=3758205: closest beacon is at x=1570410, y=3710085
Sensor at x=3999446, y=1929369: closest beacon is at x=3213800, y=2708360
Sensor at x=1434466, y=2254087: closest beacon is at x=745731, y=2000000
Sensor at x=200365, y=1856636: closest beacon is at x=745731, y=2000000
Sensor at x=1859710, y=31159: closest beacon is at x=1671413, y=43557
Sensor at x=3712613, y=3930105: closest beacon is at x=3133588, y=3984216
Sensor at x=1660185, y=2900: closest beacon is at x=1671413, y=43557
Sensor at x=1497065, y=93501: closest beacon is at x=1671413, y=43557
Sensor at x=3832823, y=3346266: closest beacon is at x=3839159, y=3421933'''

import re
import numpy as np


def distance(a, b):
    return np.abs(a-b).sum()


sensors = []
beacons = set()
for line in input.split("\n"):
    m = re.match(r'Sensor at x=([+\-0-9]*), y=([+\-0-9]*): closest beacon is at x=([+\-0-9]*), y=([+\-0-9]*)', line)
    pos = np.asarray([int(m.group(1)), int(m.group(2))], dtype=int)
    beacon = np.asarray([int(m.group(3)), int(m.group(4))], dtype=int)

    sensors.append({
        'pos': pos,
        'beacon': beacon,
        'range': distance(pos, beacon),
    })

    beacons.add(tuple(beacon))

y = 2000000
blocked_positions = set()
for sensor in sensors:
    vertical_distance = abs(sensor['pos'][1] - y)

    width = sensor['range'] - vertical_distance

    if width < 0:
        continue

    center = sensor['pos'][0]

    for x in range(center-width, center+width+1):
        pos = np.asarray([x, y])
        blocked_positions.add((x, y))

blocked_positions -= beacons

print(len(blocked_positions))
