from day_24inp import INPUT
import re
from collections import deque


def decode(regs, reg):
    result = 0
    for key in reversed(sorted(regs.keys())):
        if key.startswith(reg):
            print(key, regs[key])
            result = 2 * result + int(regs[key])
    return result


registers, circuits = INPUT.split("\n\n")

regs = {}
for reg in registers.split("\n"):
    r, v = reg.split(": ")
    regs[r] = True if v == "1" else False

pattern = re.compile(r"([^ ]*) (AND|OR|XOR) ([^ ]*) -> ([^ ]*)")
circs = deque()
for circ in circuits.split("\n"):
    m = pattern.match(circ)
    o1, op, o2, res = m.groups()
    circs.append((o1, op, o2, res))

while circs:
    o1, op, o2, res = circs.popleft()
    if o1 in regs and o2 in regs:
        if op == "AND":
            regs[res] = regs[o1] and regs[o2]
        elif op == "OR":
            regs[res] = regs[o1] or regs[o2]
        elif op == "XOR":
            regs[res] = regs[o1] ^ regs[o2]
        else:
            assert False
    else:
        circs.append((o1, op, o2, res))

print(decode(regs, "z"))
