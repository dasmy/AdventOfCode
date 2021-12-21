import numpy as np


def simulate(target_x, target_y):

    vx_ = np.arange(0, target_x[1]+1, 1)
    vy_ = np.arange(np.min(target_y), 1000, 1)
    vx, vy = np.meshgrid(vx_, vy_)

    x = np.zeros_like(vx)
    y = np.zeros_like(vy)

    y_max = np.zeros_like(vy)

    found = np.zeros_like(vx, dtype=bool)

    while not np.all(y < np.min(target_y)):
        x += vx
        y += vy
        vx -= np.sign(vx)
        vy -= 1

        y_max = np.maximum(y, y_max)

        in_x = np.logical_and(target_x[0] <= x, x <= target_x[1])
        in_y = np.logical_and(target_y[0] <= y, y <= target_y[1])
        found[np.logical_and(in_x, in_y)] = True

    vx, vy = np.meshgrid(vx_, vy_)

    hits = np.asarray([[vx[tuple(f)], vy[tuple(f)]] for f in np.argwhere(found)])
    max_y_at = np.argmax(hits[:, 1])
    print(f'Found {len(hits)} hits. Maximum height with initial velocity {hits[max_y_at]}, Height: {y_max[found].max()}')


simulate((20, 30), (-10, -5))
simulate((25, 67), (-260, -200))


