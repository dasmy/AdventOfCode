from day_18inp import DIMENSIONS, INPUT
from itertools import product

maxlen = 1024
corrupted = set(tuple(map(int, row.split(","))) for row in INPUT.split("\n")[:maxlen])
maxx, maxy = DIMENSIONS

maxroute = (maxx + 1) * (maxy + 1) + 1
pos = (0, 0)
target = (maxx, maxy)

# Dijsktra's algorithm following https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
dist_prev = {
    (x, y): (maxroute, None)
    for (x, y) in product(range(maxx + 1), range(maxy + 1))
    if (x, y) not in corrupted
}
dist_prev[pos] = (0, None)

Q = set(dist_prev.keys())

while Q:
    u = min([k for k in Q], key=lambda x: dist_prev[x][0])
    u_dist, u_prev = dist_prev[u]
    Q.remove(u)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = u[0] + dx, u[1] + dy
        if not (0 <= nx <= maxx and 0 <= ny <= maxy):
            continue

        n = (nx, ny)
        if n in corrupted:
            continue

        if n not in Q:
            continue

        alt = u_dist + 1
        if alt < dist_prev[n][0]:
            dist_prev[n] = (alt, u)

print(dist_prev[target])
