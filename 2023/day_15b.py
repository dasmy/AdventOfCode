from collections import defaultdict
from day_15 import INPUT_TEST, INPUT


def compute_hash(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256

    return total


def day_15a(inp):
    boxes = defaultdict(list)
    for item in inp.split(','):
        if item.endswith('-'):
            label = item[:-1]
            box = compute_hash(label)
            boxes[box] = [i for i in boxes[box] if i[0] != label]
        else:
            item = item.split('=')
            label = item[0]
            focal_length = int(item[1])
            box = compute_hash(label)
            for i, it in enumerate(boxes[box]):
                if it[0] == label:
                    boxes[box][i] = (label, focal_length)
                    break
            else:
                boxes[box].append((label, focal_length))

    total = 0
    for box, content in boxes.items():
        box_total = 0
        for ilens, lens in enumerate(content, 1):
            box_total += ilens * lens[1]

        total += (box + 1) * box_total

    return total


print(day_15a(INPUT_TEST))
print(day_15a(INPUT))
