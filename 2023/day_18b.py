import numpy as np
from day_18 import INPUT_TEST, INPUT


def day_18b(inp):
    x, y = 0, 0
    p_x, p_y = [x, ], [y, ]

    for line in inp.split('\n'):
        _, _, hex = tuple(line.split(' '))

        hex = hex.strip('()#')

        steps = int(hex[:5], base=16)
        dir = 'RDLU'[int(hex[-1])]

        if dir == 'R':
            x += steps
        elif dir == 'L':
            x -= steps
        elif dir == 'U':
            y -= steps
        elif dir == 'D':
            y += steps
        else:
            assert False

        p_x.append(x)
        p_y.append(y)

    assert x == 0
    assert y == 0

    p_x = np.asarray(p_x, dtype=int)
    p_y = np.asarray(p_y, dtype=int)

    min_x, max_x = p_x.min(), p_x.max()
    min_y, max_y = p_y.min(), p_y.max()

    p_x -= min_x
    max_x -= min_x

    p_y -= min_y
    max_y -= min_y

    points = []
    for point in zip(p_x, p_y):
        points.append(point)

    # compute area with shoelace formula
    area = 0
    for a, b in zip(points, points[1:]):
        area += a[0] * b[1] - a[1] * b[0]
    area /= 2

    # compute perimeter
    perimeter = 0
    for a, b in zip(points, points[1:]):
        perimeter += abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Pick's theorem for computing integer
    content = area + perimeter / 2 + 1

    return int(content)


print(day_18b(INPUT_TEST))
print(day_18b(INPUT))
