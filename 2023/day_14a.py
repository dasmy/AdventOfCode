from collections import defaultdict
from day_14 import INPUT_TEST, INPUT


def day_14a(inp):
    rocks = defaultdict(list)
    blockers = defaultdict(list)
    lines = inp.split('\n')
    for iline, line in enumerate(lines):
        for icol, c in enumerate(line):
            if c == '#':
                blockers[icol].append(iline)
            elif c == 'O':
                rocks[icol].append(iline)
            else:
                assert c == '.'

    for icol, col in rocks.items():
        new_col = []
        for rock in col:
            while rock > 0 and rock-1 not in blockers[icol] and rock-1 not in new_col:
                rock -= 1
            new_col.append(rock)
        rocks[icol] = new_col

    total = 0
    for col in rocks.values():
        for rock in col:
            total += len(lines) - rock

    return total

print(day_14a(INPUT_TEST))
print(day_14a(INPUT))
