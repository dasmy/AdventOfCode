from day_01 import INPUT_TEST, INPUT

NUMBERS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def find_digit(line, start, dir):
    digit = None
    while digit is None:
        try:
            digit = int(line[start])
            return digit
        except ValueError:
            for c, n in NUMBERS.items():
                if line[start:].startswith(c):
                    return n

            start += dir


def day_01b(inp):
    total = 0
    for line in inp.split('\n'):
        total += 10*find_digit(line, 0, 1) + find_digit(line, -1, -1)

    return total


print(day_01b(INPUT_TEST))
print(day_01b(INPUT))
