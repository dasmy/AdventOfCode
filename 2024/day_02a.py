import numpy as np
from day_02inp import INPUT, TEST_INPUT

num_safe = 0
for report in INPUT.split("\n"):
    levels = [int(level) for level in report.split()]

    diff = np.diff(levels)

    for factor in (1, -1):
        diff *= factor

        if np.all(diff >= 1) and np.all(diff <= 3):
            num_safe += 1
            print(f"Safe: {levels}, {diff}")
            break
    else:
        print(f"Unafe: {levels}, {diff}")

print(num_safe)
