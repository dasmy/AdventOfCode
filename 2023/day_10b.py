import numpy as np
from day_10 import INPUT_TEST, INPUT_TEST_2, INPUT_TEST_3, INPUT_TEST_4, INPUT_TEST_5, INPUT


def route(cell, dx, dy):
    if cell == '|':
        if dx != 0 or dy == 0:
            raise ValueError
        return 0, dy
    elif cell == '-':
        if dx == 0 or dy != 0:
            raise ValueError
        return dx, 0
    elif cell == 'L':
        if dx == 0 and dy == 1:
            return +1, 0
        elif dx == -1 and dy == 0:
            return 0, -1
        else:
            raise ValueError
    elif cell == 'J':
        if dx == 0 and dy == 1:
            return -1, 0
        elif dx == 1 and dy == 0:
            return 0, -1
        else:
            raise ValueError
    elif cell == '7':
        if dx == 0 and dy == -1:
            return -1, 0
        elif dx == 1 and dy == 0:
            return 0, 1
        else:
            raise ValueError
    elif cell == 'F':
        if dx == 0 and dy == -1:
            return +1, 0
        elif dx == -1 and dy == 0:
            return 0, +1
        else:
            raise ValueError
    elif cell == '.':
        raise ValueError
    else:
        raise ValueError


def day_10b(inp):
    layout = inp.split('\n')
    layout = np.array(layout, dtype=str).view('U1').reshape((len(layout), -1))
    areas = np.zeros_like(layout, dtype=layout.dtype)
    areas[:, :] = ' '

    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == 'S':
                start_x, start_y = x, y

    max_y, max_x = layout.shape

    # find start direction
    x, y = start_x, start_y
    for dx_start, dy_start in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
        if not 0 <= x+dx_start < max_x:
            continue
        if not 0 <= y+dy_start < max_y:
            continue
        try:
            cell = layout[y+dy_start, x+dx_start]
            route(cell, dx_start, dy_start)
            dx, dy = dx_start, dy_start
            break
        except ValueError:
            pass

    x, y = start_x + dx, start_y + dy
    while (x != start_x) or (y != start_y):
        assert 0 <= x < max_x
        assert 0 <= y < max_y
        areas[y, x] = '#'

        cell = layout[y, x]
        dx, dy = route(cell, dx, dy)
        x += dx
        y += dy

    print(dx_start, dy_start, dx, dy)
    if (dx_start, dy_start) == (1, 0) and (dx, dy) == (0, -1):
        start_letter = 'F'
    elif (dx_start, dy_start) == (-1, 0) and (dx, dy) == (0, -1):
        start_letter = '7'
    else:
        # TODO: add other directions as well
        raise ValueError

    areas[start_y, start_x] = start_letter

    for corner in ('7', 'L'):  #, 'J', 'F'):
        areas[np.bitwise_and(layout == corner, areas == '#')] = corner

    dir_x = +1
    dir_y = +1
    for iy in range(areas.shape[0]):
        for ix in range(areas.shape[1]):
            if areas[iy, ix] == ' ':
                count = 0
                x = ix + dir_x
                y = iy + dir_y
                while (0 <= x < max_x) and (0 <= y < max_y):
                    if areas[y, x] == '#':
                        count += 1
                    x += dir_x
                    y += dir_y
                if count % 2 == 1:
                    areas[iy, ix] = 'I'

    for row in areas:
        print(''.join(row))

    return (areas == 'I').sum()


print(day_10b(INPUT_TEST))
print(day_10b(INPUT_TEST_2))
print(day_10b(INPUT_TEST_3))
print(day_10b(INPUT_TEST_4))
print(day_10b(INPUT_TEST_5))
print(day_10b(INPUT))
