from day_20inp import INPUT
from itertools import product
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed


blocked = list()
for irow, row in enumerate(INPUT.split("\n")):
    for icol, c in enumerate(row):
        if c == "#":
            blocked.append((irow, icol))
        elif c == "S":
            start = (irow, icol)
        elif c == "E":
            end = (irow, icol)
        else:
            assert c == "."

maxx, maxy = irow, icol


def find_path(blocked):
    blocked = set(blocked)

    # Dijsktra's algorithm following https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
    dist_prev = {
        (x, y): (1e8, None)
        for (x, y) in product(range(maxx + 1), range(maxy + 1))
        if (x, y) not in blocked
    }
    dist_prev[start] = (0, None)

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
            if n in blocked:
                continue

            if n not in Q:
                continue

            alt = u_dist + 1
            if alt < dist_prev[n][0]:
                dist_prev[n] = (alt, u)

    return dist_prev[end]


if __name__ == "__main__":
    pathlen_orig, _ = find_path(blocked)

    counter = defaultdict(int)
    more_than_100 = 0

    with ProcessPoolExecutor() as pool:
        fs = {
            pool.submit(find_path, blocked=blocked[:r] + blocked[r + 1 :]): r
            for r in range(len(blocked) // 100)
        }

        for f in as_completed(fs):
            to_remove = fs[f]
            pathlen, prev = f.result()

            saved = pathlen_orig - pathlen
            print(to_remove, pathlen_orig, pathlen, saved)
            counter[saved] += 1

            if saved >= 100:
                more_than_100 += 1

    print("\n".join(f"{k} : {counter[k]}" for k in sorted(counter.keys())))

    print(more_than_100)
