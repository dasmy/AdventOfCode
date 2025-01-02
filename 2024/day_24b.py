from day_24inp import INPUT
import re

registers, circuits = INPUT.split("\n\n")

regs = {}
for reg in registers.split("\n"):
    r, v = reg.split(": ")
    regs[r] = True if v == "1" else False

zmax = 0
pattern = re.compile(r"([^ ]*) (AND|OR|XOR) ([^ ]*) -> ([^ ]*)")
circs = set()
for circ in circuits.split("\n"):
    m = pattern.match(circ)
    o1, op, o2, res = m.groups()
    circs.add((o1, op, o2, res))
    if res[0] == "z":
        zmax = max(zmax, int(res[1:]))


def find_next_op(o):
    for o1, op, o2, _ in circs:
        if o in (o1, o2):
            return op

    return "NOT FOUND"


bad = set()
for o1, op, o2, res in circs:
    # z registers must result from an XOR (except for the highest one)
    if res[0] == "z" and int(res[1:]) != zmax and op != "XOR":
        print(o1, op, o2, res)
        bad.add(res)

    # XOR is either used with x or y as input or with z as output
    if (
        op == "XOR"
        and res[0] != "z"
        and o1[0] not in ("x", "y")
        and o2[0] not in ("x", "y")
    ):
        print(o1, op, o2, res)
        bad.add(res)

    # AND results produce individual carry contributions and have to go into OR
    if op == "AND" and "x00" not in (o1, o2):
        if (next := find_next_op(res)) != "OR":
            print(o1, op, o2, res, next)
            bad.add(res)

    # XOR results never go into OR (OR is only used for carry)
    if op == "XOR":
        if (next := find_next_op(res)) == "OR":
            print(o1, op, o2, res, next)
            bad.add(res)

print(",".join(sorted(bad)))
