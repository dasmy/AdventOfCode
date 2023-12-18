import numpy as np
from day_18 import INPUT_TEST, INPUT


def day_18a(inp):
    x, y = 0, 0
    p_x, p_y = [x, ], [y, ]
    colors = []
    for line in inp.split('\n'):
        dir, steps, color = tuple(line.split(' '))

        for _ in range(int(steps)):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y -= 1
            elif dir == 'D':
                y += 1
            else:
                assert False

            p_x.append(x)
            p_y.append(y)
            colors.append(color.strip('()'))

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

    points = set()
    for point in zip(p_x, p_y):
        points.add(point)

    area = len(points)
    for p_y in range(max_y + 1):
        for p_x in range(max_x + 1):
            if (p_x, p_y) not in points:
                count = 0
                x, y = p_x, p_y
                while x <= max_x and y <= max_y:
                    x += 1
                    y += 1
                    if (x, y) in points:
                        if (x, y+1) in points and (x-1, y) in points:
                            pass  # upper right corner
                        elif (x, y-1) in points and (x+1, y) in points:
                            pass  # lower left corner
                        else:
                            count += 1
                if count % 2 == 1:
                    # point is inside
                    area += 1

    return area


print(day_18a(INPUT_TEST))
print(day_18a(INPUT))
