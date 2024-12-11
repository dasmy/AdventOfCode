from day_11inp import INPUT


stones = list(map(int, INPUT.split()))

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str_stone := str(stone)) % 2 == 0:
            split = len(str_stone) // 2
            new_stones.append(int(str_stone[:split]))
            new_stones.append(int(str_stone[split:]))
        else:
            new_stones.append(2024 * stone)

    stones = new_stones
    print(i, len(stones))
