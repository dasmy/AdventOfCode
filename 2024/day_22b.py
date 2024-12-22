from day_22inp import INPUT
from collections import defaultdict
import numpy as np

secret = np.array(list(map(int, INPUT.split("\n"))))

last_digits = [secret % 10]

for _ in range(2000):
    secret ^= secret * 2**6  # 64
    secret %= 2**24  # 16777216
    secret ^= secret // 2**5  # 32
    secret %= 2**24  # 16777216
    secret ^= secret * 2**11  # 2048
    secret %= 2**24  # 16777216

    last_digits.append(secret % 10)

last_digits = np.array(last_digits).T
diffs = np.diff(last_digits, axis=1)

total = defaultdict(int)
for deltas, digits in zip(diffs, last_digits):
    options = dict()
    for col in range(4, len(deltas)):
        sequence = tuple(map(int, deltas[col - 4 : col]))
        if sequence not in options:
            price = digits[col]
            options[sequence] = int(price)

    for sequence, price in options.items():
        total[sequence] += price

optimum = max(total, key=total.get)
print(optimum, total[optimum])
