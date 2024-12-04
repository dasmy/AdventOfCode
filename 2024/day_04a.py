from day_04inp import INPUT
import numpy as np

input = np.array([[char for char in row] for row in INPUT.split("\n")])

total = 0


def test(seq):
    seq = "".join(seq)
    count = sum(seq.count(word) for word in ("XMAS", "SAMX"))
    print(count, seq)
    return count


print("Rows")
for row in input:
    total += test(row)

print("Cols")
for col in input.T:
    total += test(col)

print("Diagonals")
for d in range(-len(input) + 1, len(input)):
    total += test(input.diagonal(d))

print("Anti-Diagonals")
for d in range(-len(input) + 1, len(input)):
    total += test(np.flipud(input).diagonal(d))

print(total)
