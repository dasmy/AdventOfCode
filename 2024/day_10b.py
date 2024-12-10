from day_10inp import INPUT
import numpy as np

input = np.array(list(list(map(int, (c for c in row))) for row in INPUT.split("\n")))


def next_step(pos, route):
    if input[*pos] == 9:
        # reached the top once
        trail = tuple(tuple(map(int, (c for c in p))) for p in route)
        print(trail)
        return set(
            [
                trail,
            ]
        )

    reached = set()
    for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        newpos = pos + dir
        if (
            newpos[0] < 0
            or newpos[1] < 0
            or newpos[0] >= input.shape[0]
            or newpos[1] >= input.shape[1]
        ):
            # out of map
            continue
        elif input[*pos] + 1 != input[*newpos]:
            # to steep
            continue
        else:
            # valid route
            reached |= next_step(newpos, route + [newpos])

    return reached


start_positions = np.argwhere(input == 0)

num_routes = 0
for pos in start_positions:
    reachable = next_step(pos, [pos])
    num_routes += len(reachable)

print(num_routes)
