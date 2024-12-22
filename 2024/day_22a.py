from day_22inp import INPUT
import numpy as np

secret = np.array(list(map(int, INPUT.split("\n"))))

for _ in range(2000):
    secret ^= secret * 2**6  # 64
    secret %= 2**24  # 16777216
    secret ^= secret // 2**5  # 32
    secret %= 2**24  # 16777216
    secret ^= secret * 2**11  # 2048
    secret %= 2**24  # 16777216

print(secret)
print(secret.sum())
