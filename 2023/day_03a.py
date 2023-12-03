import re
from day_03 import INPUT_TEST, INPUT


def day_03a(inp):
    symbols = {}
    for r, line in enumerate(inp.split('\n')):
        for c, symbol in enumerate(line):
            if symbol not in '0123456789.':
                symbols[(r, c)] = symbol

    number = re.compile(r'\d+')
    total = 0

    for r, line in enumerate(inp.split('\n')):
        for m in number.finditer(line):
            n = int(m.group())
            c1, c2 = m.start(), m.end()
            for sr in range(r-1, r+2):
                for sc in range(c1-1, c2+1):
                    if (sr, sc) in symbols:
                        print(f'Found {n}: {symbols[(sr, sc)]}')
                        total += n

    return total


print(day_03a(INPUT_TEST))
print(day_03a(INPUT))
