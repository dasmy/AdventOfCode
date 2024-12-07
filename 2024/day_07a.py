from day_07inp import INPUT
from itertools import product
from operator import mul, add


total = 0
for line in INPUT.split("\n"):
    expected, operands = line.split(":")
    expected = int(expected)
    operands = [int(o) for o in operands.split()]

    for operators in product((mul, add), repeat=len(operands) - 1):
        acc = operands[0]
        for operand, operator in zip(operands[1:], operators):
            acc = operator(acc, operand)
            if acc > expected:
                continue
        else:
            if acc == expected:
                total += expected
                print(f"{operands}, {operators}, {expected}")
                break

print(total)
