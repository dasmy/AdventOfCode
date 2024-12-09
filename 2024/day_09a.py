from day_09inp import INPUT

from collections import deque
from itertools import cycle

disk = deque()

i_file = 0
for is_file, length in zip(cycle((True, False)), map(int, INPUT)):
    if is_file:
        for _ in range(length):
            disk.append(i_file)
        i_file += 1
    else:
        for _ in range(length):
            disk.append(-1)

print(len(disk))

for pos in range(len(disk)):
    try:
        if disk[pos] == -1:
            while (new_file := disk.pop()) == -1:
                pass

            disk[pos] = new_file
    except IndexError:
        # reached end
        break

print(len(disk))

checksum = 0
for pos, file in enumerate(disk):
    if file != -1:
        checksum += pos * file

print(checksum)
