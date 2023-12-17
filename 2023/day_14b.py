from functools import cache
from day_14 import INPUT_TEST, INPUT


@cache
def roll(rocks, blockers, max_col, max_row, dir):
    new_rocks = set()

    if dir == 0:  # north
        d_col = 0
        d_row = -1
        sort_by = 1
        reverse = False
    elif dir == 2:  # south
        d_col = 0
        d_row = +1
        sort_by = 1
        reverse = True
    elif dir == 1:  # east
        d_col = -1
        d_row = 0
        sort_by = 0
        reverse = False
    elif dir == 3:  # west
        d_col = +1
        d_row = 0
        sort_by = 0
        reverse = True
    else:
        raise ValueError

    for col, row in sorted(rocks, key=lambda x: x[sort_by], reverse=reverse):
        while   \
            0 <= row + d_row < max_row and  \
            0 <= col + d_col < max_col and \
            (col + d_col, row+d_row) not in blockers and  \
            (col + d_col, row+d_row) not in new_rocks:
            row += d_row
            col += d_col
        new_rocks.add((col, row))

    return tuple(new_rocks)


def compute_weight(rocks, max_row):
    total = 0
    for col, row in rocks:
        total += max_row - row
    return total


@cache
def do_cycle(rocks, blockers, max_col, max_row, num_cycles, split=10):
    if num_cycles > 1:
        assert num_cycles % split == 0
        for c in range(10):
            rocks = do_cycle(rocks, blockers, max_col, max_row, num_cycles // split)
        print(num_cycles, compute_weight(rocks, max_row))
        return rocks
    else:
        for dir in (0, 1, 2, 3):
            rocks = roll(rocks, blockers, max_col, max_row, dir)
        return rocks


def day_14b(inp):
    rocks = set()
    blockers = set()
    lines = inp.split('\n')
    for iline, line in enumerate(lines):
        for icol, c in enumerate(line):
            if c == '#':
                blockers.add((icol, iline))
            elif c == 'O':
                rocks.add((icol, iline))
            else:
                assert c == '.'

    max_row = len(lines)
    max_col = len(lines[0])

    rocks = tuple(rocks)
    blockers = tuple(blockers)

    rocks = do_cycle(rocks, blockers, max_col, max_row, 1000000000)

    return compute_weight(rocks, max_row)


print(day_14b(INPUT_TEST))
print(day_14b(INPUT))
