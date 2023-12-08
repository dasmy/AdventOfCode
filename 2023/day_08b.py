import re
from math import lcm
from itertools import cycle
from collections import defaultdict
from day_08 import INPUT_TEST_3, INPUT


def day_08b(inp):
    lines = inp.split('\n')
    instructions = lines[0]

    pattern = re.compile(r'(\w+) = \((\w+), (\w+)\)')

    pos = []
    network = {}
    for line in lines[2:]:
        m = pattern.match(line)
        assert m is not None
        network[m.group(1)] = (m.group(2), m.group(3))

        if m.group(1).endswith('A'):
            pos.append(m.group(1))

    steps = 0

    z_counters = {}
    z_delta = defaultdict(dict)
    p_counters = defaultdict(dict)
    p_cycle = {}

    for p0 in pos:
        steps = 0
        p = p0
        for instruction in cycle(instructions):
            if p.endswith('Z'):
                note = (instruction, p)

                for z_start, v in z_counters.items():
                    delta = steps - v
                    assert delta not in z_delta[z_start]
                    z_delta[z_start][delta] = note

                if note in z_counters:
                    # we have been here with the same instruction already - reached a cycle
                    p_cycle[(instructions[0], p0)] = steps - z_counters[note]
                    break
                else:
                    z_counters[note] = steps

                p_counters[(instructions[0], p0)][steps] = note

            if instruction == 'R':
                p = network[p][1]
            elif instruction == 'L':
                p = network[p][0]
            else:
                assert False

            steps += 1

    p_state = {}
    for p0 in pos:
        p0 = (instructions[0], p0)
        p_state[p0] = set(p_counters[p0].keys())

    print(p_state)
    print(p_cycle)

    return lcm(*p_cycle.values())


print(day_08b(INPUT_TEST_3))
print(day_08b(INPUT))
