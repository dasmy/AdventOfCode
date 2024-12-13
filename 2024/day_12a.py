from day_12inp import INPUT
import numpy as np
import skimage

input = np.asarray([[ord(c) - ord("A") + 1 for c in row] for row in INPUT.split("\n")])

labels, num_labels = skimage.measure.label(input, connectivity=1, return_num=True)

total_price = 0
for label in range(1, num_labels + 1):
    patches = set(tuple(map(int, p)) for p in np.argwhere(labels == label))
    area = len(patches)

    perimeter = 0
    for patch in patches:
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            neighbor = (patch[0] + dir[0], patch[1] + dir[1])
            if neighbor not in patches:
                perimeter += 1

    price = area * perimeter
    print(label, area, perimeter, price)

    total_price += price

print(total_price)
