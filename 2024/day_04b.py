from day_04inp import INPUT
import numpy as np

input = np.array([[char for char in row] for row in INPUT.split("\n")])

total = 0

for nrot in range(4):
    for r in range(input.shape[0] - 2):
        for c in range(input.shape[1] - 2):
            if (
                input[r, c] == "M"
                and input[r + 2, c] == "M"
                and input[r + 1, c + 1] == "A"
                and input[r, c + 2] == "S"
                and input[r + 2, c + 2] == "S"
            ):
                total += 1

    input = np.rot90(input)

print(total)
