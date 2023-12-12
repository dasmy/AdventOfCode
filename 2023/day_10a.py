from day_10 import INPUT_TEST, INPUT_TEST_2, INPUT


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


def day_10a(inp):
    layout = inp.split('\n')

    for y, row in enumerate(layout):
        for x, cell in enumerate(row):
            if cell == 'S':
                start_x, start_y = x, y

    max_y = len(layout)
    max_x = len(layout[0])

    # find start direction
    x, y = start_x, start_y
    for dx_start, dy_start in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
        if not 0 <= x+dx_start < max_x:
            continue
        if not 0 <= y+dy_start < max_y:
            continue
        try:
            cell = layout[y+dy_start][x+dx_start]
            route(cell, dx_start, dy_start)
            dx, dy = dx_start, dy_start
            break
        except ValueError:
            pass

    x, y = start_x + dx, start_y + dy
    steps = 1
    while (x != start_x) or (y != start_y):
        assert 0 <= x < max_x
        assert 0 <= y < max_y
        cell = layout[y][x]
        dx, dy = route(cell, dx, dy)
        x += dx
        y += dy
        steps += 1

    assert steps % 2 == 0
    return steps // 2


print(day_10a(INPUT_TEST))
print(day_10a(INPUT_TEST_2))
print(day_10a(INPUT))
