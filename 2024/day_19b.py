from day_19inp import INPUT
from functools import cache

towels, designs = INPUT.split("\n\n")
towels = set(towels.split(", "))


@cache
def test(sub):
    if sub == "":
        return 1

    total = 0
    for towel in towels:
        if sub.startswith(towel):
            total += test(sub[len(towel) :])

    return total


count = 0
for design in designs.split("\n"):
    this_count = test(design)
    print(f"{this_count:20d}: {design}")
    count += this_count

print(count)
