from day_01 import INPUT_TEST, INPUT


def find_digit(line, start, dir):
    digit = None
    while digit is None:
        try:
            digit = int(line[start])
        except ValueError:
            start += dir
        else:
            return digit


def day_01a(inp):
    total = 0
    for line in inp.split('\n'):
        total += 10*find_digit(line, 0, 1) + find_digit(line, -1, -1)

    return total


print(day_01a(INPUT_TEST))
print(day_01a(INPUT))
