from day_09inp import INPUT

from itertools import cycle

disk = []


def disk_to_string(disk):
    result = ""
    for block in disk:
        char = f"[{'.' if block[0] == -1 else block[0]}]"
        # char = "." if block[0] == -1 else str(block[0])
        result += char * block[1]

    return result


i_file = 0
for is_file, length in zip(cycle((True, False)), map(int, INPUT)):
    if is_file:
        disk.append((i_file, length))
        i_file += 1
    else:
        disk.append((-1, length))

print(len(disk))

pos = len(disk) - 1
# print(disk_to_string(disk))
while pos >= 0:
    file = disk[pos]

    if file[0] == -1:
        pos -= 1
    else:
        for pos_free in range(pos):
            free_block = disk[pos_free]
            if free_block[0] == -1 and (r := free_block[1] - file[1]) >= 0:
                disk[pos] = (-1, file[1])
                disk[pos_free] = file
                if r > 0:
                    disk.insert(pos_free + 1, (-1, r))
                else:
                    pos -= 1

                # print(disk_to_string(disk))
                break
        else:
            pos -= 1

print(len(disk))
print(disk_to_string(disk))

checksum = 0
pos = 0
for file, length in disk:
    if file != -1:
        for i in range(pos, pos + length):
            checksum += i * file
    pos += length

print(checksum)
