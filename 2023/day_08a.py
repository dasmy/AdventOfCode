import re
from itertools import cycle
from day_08 import INPUT_TEST, INPUT, INPUT_TEST_2


def day_08a(inp):
    lines = inp.split('\n')
    instructions = lines[0]

    pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')

    network = {}
    for line in lines[2:]:
        m = pattern.match(line)
        assert m is not None
        network[m.group(1)] = (m.group(2), m.group(3))

    steps = 0
    pos = 'AAA'
    target = 'ZZZ'
    for instruction in cycle(instructions):
        if pos == target:
            break

        if instruction == 'R':
            pos = network[pos][1]
        elif instruction == 'L':
            pos = network[pos][0]
        else:
            assert False

        steps += 1

    return steps


print(day_08a(INPUT_TEST))
print(day_08a(INPUT_TEST_2))
print(day_08a(INPUT))
