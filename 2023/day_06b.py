from math import sqrt
from day_06 import INPUT_TEST, INPUT


def day_06b(inp):
    lines = inp.split('\n')
    T = int(lines[0][10:].replace(' ', ''))
    s0 = int(lines[1][10:].replace(' ', ''))
    vc = 1

    delta = sqrt(T*T/4-s0/vc)
    u = int(T/2 + delta)
    l = int(T/2 - delta)

    return u - l


print(day_06b(INPUT_TEST))
print(day_06b(INPUT))
