from functools import cache
from day_12 import INPUT_TEST, INPUT


@cache
def count(remaining_pattern, expected_groups):
    if expected_groups == ():
        return 0 if '#' in remaining_pattern else 1

    n = expected_groups[0]
    res = 0
    for i in range(len(remaining_pattern)-(len(expected_groups)-1+sum(expected_groups[1:]))-(n+1)+1):
        if remaining_pattern[i+n] == '#':
            continue
        if '#' in remaining_pattern[:i]:
            break
        if '.' not in remaining_pattern[i:i+n]:
            res += count(remaining_pattern[i+n+1:], expected_groups[1:])
    return res


def day_12b(inp: str):

    total = 0
    for line in inp.split('\n'):
        line = line.split(' ')
        line[0] = '?'.join([line[0]] * 5)
        line[1] = ','.join([line[1]] * 5)

        pattern = line[0] + '.'
        expected_groups = tuple(int(s) for s in line[1].split(','))

        cnt = count(pattern, expected_groups)
        total += cnt
    return total


print(day_12b(INPUT_TEST))
print(day_12b(INPUT))
