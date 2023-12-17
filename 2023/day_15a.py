from day_15 import INPUT_TEST, INPUT


def compute_hash(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256

    return total


def day_15a(inp):
    total = 0
    for item in inp.split(','):
        total += compute_hash(item)
    return total


print(day_15a(INPUT_TEST))
print(day_15a(INPUT))
