from day_20inp import INPUT
from itertools import combinations


field = set()
for irow, row in enumerate(INPUT.split("\n")):
    for icol, c in enumerate(row):
        if c == "#":
            continue
        elif c == "S":
            start = (irow, icol)
        elif c == "E":
            end = (irow, icol)
        else:
            assert c == "."
        field.add((irow, icol))


dist = {
    start: 0,
}

todo = set([start])

while todo:
    current = todo.pop()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next = current[0] + dx, current[1] + dy
        if next not in field:
            continue
        elif next in dist:
            continue
        else:
            dist[next] = dist[current] + 1
            todo.add(next)

max_cheat = 20
min_save = 100
count = 0
for (c1, d1), (c2, d2) in combinations(dist.items(), r=2):
    if (delta := sum(abs(ca - cb) for ca, cb in zip(c1, c2))) <= max_cheat:
        if (saved := d2 - d1 - delta) >= min_save:
            print(delta, saved)
            count += 1

print(count)
