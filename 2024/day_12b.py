from day_12inp import INPUT
import numpy as np
import skimage
from collections import defaultdict

input = np.asarray([[ord(c) - ord("A") + 1 for c in row] for row in INPUT.split("\n")])

labels, num_labels = skimage.measure.label(input, connectivity=1, return_num=True)


def count_segments(fences):
    fences.sort()
    segments = 1
    last = fences[0]
    for fence in fences[1:]:
        if fence - last > 1:
            segments += 1
        last = fence
    return segments


total_price = 0
for label in range(1, num_labels + 1):
    patches = set(tuple(map(int, p)) for p in np.argwhere(labels == label))
    area = len(patches)

    perimeter = 0
    fences = defaultdict(lambda: defaultdict(list))
    for patch in patches:
        for dir in [(1, 0), (-1, 0)]:
            neighbor = (patch[0] + dir[0], patch[1] + dir[1])
            if neighbor not in patches:
                fences[dir][patch[0] + 0.5 * dir[0]].append(patch[1] + 0.5 * dir[1])

        for dir in [(0, 1), (0, -1)]:
            neighbor = (patch[0] + dir[0], patch[1] + dir[1])
            if neighbor not in patches:
                fences[dir][patch[1] + 0.5 * dir[1]].append(patch[0] + 0.5 * dir[0])

    for fencing in fences.values():
        for fences in fencing.values():
            perimeter += count_segments(fences)

    price = area * perimeter
    print(label, area, perimeter, price)

    total_price += price

print(total_price)
