import math
from day_12 import INPUT_TEST, INPUT


def to_bitlist(num, bits):
    assert int(math.log(num, 2)+1) <= bits
    return [1 if num & (1 << (bits-1-n)) else 0 for n in range(bits)]


def day_12a(inp: str):

    total = 0
    for line in inp.split('\n'):
        line = line.split(' ')
        pattern = line[0]
        expected_groups = [int(s) for s in line[1].split(',')]

        unclear = [idx for idx, c in enumerate(pattern) if c == '?']
        num_unclear = len(unclear)
        num_missing = sum(expected_groups) - pattern.count('#')

        if num_missing == 0:
            counter = 1
        else:
            counter = 0
            for i in range(2**num_unclear):
                if i.bit_count() == num_missing:
                    bits = to_bitlist(i, num_unclear)
                    filled_pattern = list(pattern)
                    for s, u in zip(bits, unclear):
                        filled_pattern[u] = '#' if s else '.'
                    filled_groups = list(filter(None, ''.join(filled_pattern).split('.')))
                    groups = [len(f) for f in filled_groups]
                    # print(filled_pattern, groups)
                    if groups == expected_groups:
                        counter += 1

        print(line, ' --> ', counter)
        total += counter

    return total


print(day_12a(INPUT_TEST))
print(day_12a(INPUT))
