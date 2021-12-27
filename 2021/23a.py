import numpy as np
from functools import cache


def print_state(field, rooms, c=0, total=0):
    PODS = ['.', 'A', 'B', 'C', 'D']
    print('#' * (len(field) + 2))
    print('#' + ''.join(PODS[f] for f in field) + '#')
    print('###' + ''.join(PODS[r] + '#' for r in rooms[:, 0]) + '##')
    print('  #' + ''.join(PODS[r] + '#' for r in rooms[:, 1]))
    print(f'  #########  [{c}, {total}]')


def finished(rooms):
    rooms = np.asarray(rooms)
    return np.all(rooms == [[1], [2], [3], [4]])


assert finished([[1, 1], [2, 2], [3, 3], [4, 4]])


def pack(field, rooms):
    return (tuple(field), tuple(rooms.reshape((-1))))


def unpack(fr):
    return np.asarray(fr[0]), np.asarray(fr[1]).reshape((4, 2))


@cache
def possible_moves(fr):
    field, rooms = unpack(fr)

    results = []

    # see what we can do about the rooms
    for iroom, room in enumerate(rooms, start=1):
        room_exit_on_field = 2 * iroom
        assert field[room_exit_on_field] == 0  # room exit is blocked

        if room[0] in (iroom, 0) and room[1] in (iroom, 0):
            # nothing to do in this room
            continue
        elif room[0] > 0:
            # need to move the upper pod out of this room
            pod_to_move = 0
        else:
            # need to move the lower pod out of this room, the upper position is free
            pod_to_move = 1

        energy_per_step = [1, 10, 100, 1000][room[pod_to_move] - 1]

        # move left
        for step in range(1, room_exit_on_field + 1):
            if field[room_exit_on_field - step] > 0:
                # occupied - cannot move further
                break
            elif room_exit_on_field - step in (2, 4, 6, 8):
                # this is a room exit, dont stop here
                continue
            else:
                f = field.copy()
                f[room_exit_on_field - step] = room[pod_to_move]
                r = rooms.copy()
                r[iroom - 1][pod_to_move] = 0
                c = (1 + pod_to_move + step) * energy_per_step
                results.append((f, r, c))

        # move right
        for step in range(1, len(field) - room_exit_on_field):
            if field[room_exit_on_field + step] > 0:
                # occupied - cannot move further
                break
            elif room_exit_on_field + step in (2, 4, 6, 8):
                # this is a room exit, dont stop here
                continue
            else:
                f = field.copy()
                f[room_exit_on_field + step] = room[pod_to_move]
                r = rooms.copy()
                r[iroom - 1][pod_to_move] = 0
                c = (1 + pod_to_move + step) * energy_per_step
                results.append((f, r, c))

    # see if a pod can be moved directly into its room
    for pos, iroom in enumerate(field):
        room_exit_on_field = 2 * iroom
        delta = pos - room_exit_on_field

        if iroom == 0:
            # no pod here
            continue
        elif not rooms[iroom-1][0] == 0:
            # room entry occupied
            continue
        elif not rooms[iroom-1][1] in (iroom, 0):
            # room back occupied by wrong pod
            continue
        elif delta != 0 and np.any(field[room_exit_on_field:pos:np.sign(delta)] > 0):
            # path to room exit is blocked on field
            continue
        else:
            energy_per_step = [1, 10, 100, 1000][iroom - 1]
            f = field.copy()
            f[pos] = 0
            r = rooms.copy()
            target = 1 if rooms[iroom-1][1] == 0 else 0
            r[iroom - 1][target] = iroom
            c = (1 + target + abs(delta)) * energy_per_step
            results.append((f, r, c))

    return results


def play(rooms):
    best_so_far = 999999
    distances = {}

    def move(fr, energy=0):
        field, rooms = unpack(fr)
        nonlocal best_so_far
        nonlocal distances

        if finished(rooms):
            if energy < best_so_far:
                best_so_far = energy
                print(f'New minimum: {energy}')
        else:
            for f, r, c in possible_moves(pack(field, rooms)):
                fr = pack(f, r)
                e_total = c + energy
                if e_total < distances.get(fr, 999999):
                    distances[fr] = e_total
                    if c + energy < best_so_far:
                        #print_state(f, r, c, c + energy)
                        move(pack(f, r), c + energy)

    field = np.zeros((11), dtype=int)
    rooms = np.asarray(rooms)
    move(pack(field, rooms))
    print(f'Minimum Energy: {best_so_far}')


A = 1
B = 2
C = 3
D = 4


play([[B, A], [C, D], [B, C], [D, A]])
play([[B, C], [A, D], [B, D], [C, A]])
