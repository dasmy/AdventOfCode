import numpy as np
from itertools import count


def compute_flashes(input):
    input = np.asarray(input)

    for i_step in count(1):
        input += 1

        flashed = np.zeros_like(input, dtype=bool)
        while True:
            flash_ready = np.logical_and(input > 9, np.logical_not(flashed))
            if np.count_nonzero(flash_ready) == 0:
                break

            flashed = np.logical_or(flashed, flash_ready)

            activation = np.zeros_like(input)
            for fl in np.argwhere(flash_ready):
                activation[max(fl[0]-1, 0):fl[0]+2, max(fl[1]-1, 0):fl[1]+2] += 1

            input += activation

        input[flashed] = 0
        if np.count_nonzero(flashed) == np.prod(input.shape):
            break

    print(f'All flashed at {i_step}')


compute_flashes([
    [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
    [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
    [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
    [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
    [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
    [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
    [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
    [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
    [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
    [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
])

compute_flashes([
    [5, 2, 1, 2, 1, 6, 6, 7, 1, 6],
    [1, 5, 6, 7, 3, 2, 2, 5, 8, 1],
    [2, 2, 6, 8, 4, 6, 1, 5, 4, 8],
    [3, 4, 8, 1, 5, 6, 1, 7, 4, 4],
    [6, 2, 4, 8, 3, 4, 2, 2, 4, 8],
    [6, 5, 2, 6, 6, 6, 7, 3, 6, 8],
    [5, 6, 2, 7, 3, 3, 5, 7, 7, 5],
    [8, 1, 2, 4, 5, 1, 1, 7, 5, 4],
    [4, 6, 1, 4, 1, 3, 7, 6, 8, 3],
    [4, 7, 2, 4, 5, 6, 1, 1, 5, 6],
])
