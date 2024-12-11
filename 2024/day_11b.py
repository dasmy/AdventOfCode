from day_11inp import INPUT

stones = list(map(int, INPUT.split()))


def _blink(stone, count):
    if count == 0:
        return 1
    else:
        if stone == 0:
            return blink(1, count - 1)
        elif len(str_stone := str(stone)) % 2 == 0:
            split = len(str_stone) // 2
            return blink(int(str_stone[:split]), count - 1) + blink(
                int(str_stone[split:]), count - 1
            )
        else:
            return blink(2024 * stone, count - 1)


cache = {}


def blink(stone, count):
    try:
        result = cache[(stone, count)]
        print((stone, count), result)
    except KeyError:
        result = _blink(stone, count)
        cache[(stone, count)] = result

    return result


total = 0
for stone in stones:
    total += blink(stone, 75)

print(total)
