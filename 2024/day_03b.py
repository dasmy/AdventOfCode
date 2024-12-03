from day_03inp import INPUT
import re


pattern = re.compile(r"(?:(don't)\(\)|(do)\(\)|(mul)\(([0-9]*),([0-9]*)\))")

total = 0
active = True
for m in re.finditer(pattern, INPUT):
    if m.group(1) == "don't":
        active = False
    elif m.group(2) == "do":
        active = True
    elif m.group(3) == "mul":
        if active:
            a = int(m.group(4))
            b = int(m.group(5))
            total += a * b
    else:
        assert False

print(total)
