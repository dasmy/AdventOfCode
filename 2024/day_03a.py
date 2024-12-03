from day_03inp import INPUT
import re


pattern = re.compile(r"mul\(([0-9]*),([0-9]*)\)")

total = 0
for m in re.finditer(pattern, INPUT):
    a = int(m.group(1))
    b = int(m.group(2))
    total += a * b

print(total)
