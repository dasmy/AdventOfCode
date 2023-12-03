import re
from day_03 import INPUT_TEST, INPUT


def day_03b(inp):
    asterisk = {}
    for r, line in enumerate(inp.split('\n')):
        for c, symbol in enumerate(line):
            if symbol == '*':
                asterisk[(r, c)] = []

    number = re.compile(r'\d+')

    for r, line in enumerate(inp.split('\n')):
        for m in number.finditer(line):
            n = int(m.group())
            c1, c2 = m.start(), m.end()
            for sr in range(r-1, r+2):
                for sc in range(c1-1, c2+1):
                    if (sr, sc) in asterisk:
                        print(f'Found {n}: {asterisk[(sr, sc)]}')
                        asterisk[(sr, sc)].append(n)

    total = 0
    for gears in asterisk.values():
        if len(gears) == 2:
            print(gears)
            total += gears[0] * gears[1]

    return total


print(day_03b(INPUT_TEST))
print(day_03b(INPUT))
