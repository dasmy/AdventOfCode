import numpy as np
from day_02inp import INPUT, TEST_INPUT

num_safe = 0
for report in INPUT.split("\n"):
    all_levels = [int(level) for level in report.split()]

    for skip in range(len(all_levels)):
        levels = all_levels[:skip] + all_levels[skip + 1 :]

        diff = np.diff(levels)

        for factor in (1, -1):
            diff *= factor

            if np.count_nonzero(diff < 1) < 1 and np.count_nonzero(diff > 3) < 1:
                num_safe += 1
                print(f"Safe: {levels}, {diff}")
                break
        else:
            continue
        break

print(num_safe)
