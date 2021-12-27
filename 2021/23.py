import numpy as np
from functools import cache


def print_state(field, rooms, c=0, total=0):
    PODS = ['.', 'A', 'B', 'C', 'D']
    print('#' * (len(field) + 2))
    print('#' + ''.join(PODS[f] for f in field) + '#')
    print('###' + ''.join(PODS[r] + '#' for r in rooms[:, 0]) + '##')
    for s in range(1, 4):
        print('  #' + ''.join(PODS[r] + '#' for r in rooms[:, s]))
    print(f'  #########  [{c}, {total}]')


def finished(rooms):
    rooms = np.asarray(rooms)
    return np.all(rooms == [[1], [2], [3], [4]])


assert finished([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])


def pack(field, rooms):
    return (tuple(field), tuple(rooms.reshape((-1))))


def unpack(fr):
    return np.asarray(fr[0]), np.asarray(fr[1]).reshape((4, -1))


@cache
def possible_moves(fr):
    field, rooms = unpack(fr)
    room_depth = rooms.shape[1]

    results = []

    # see what we can do about the rooms
    for iroom, room in enumerate(rooms, start=1):
        room_exit_on_field = 2 * iroom
        assert field[room_exit_on_field] == 0  # room exit is blocked

        for pod_to_move in range(room_depth):
            if room[pod_to_move] == 0:
                # spot in room empty - look further down
                continue
            elif np.all(room[pod_to_move:] == iroom):
                # from this spot on only proper pods are in the room - room is finished so far
                break
            else:
                # need to move this pod because it does not belong here or anybody below does not
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

                # do not look further down in the room
                break

    # see if a pod can be moved directly into its room
    for pos, iroom in enumerate(field):
        room_exit_on_field = 2 * iroom
        delta = pos - room_exit_on_field

        if iroom == 0:
            # no pod here
            continue
        elif not np.all(np.logical_or(rooms[iroom-1] == 0, rooms[iroom-1] == iroom)):
            # still some wrong pod in the room - cannot move in there
            continue
        elif delta != 0 and np.any(field[room_exit_on_field:pos:np.sign(delta)] > 0):
            # path to room exit is blocked on field
            continue
        else:
            energy_per_step = [1, 10, 100, 1000][iroom - 1]
            # move as far down in the room as possible
            target = np.argwhere(rooms[iroom-1] == 0).flatten().max()
            f = field.copy()
            f[pos] = 0
            r = rooms.copy()
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
                # print(f'New minimum: {energy}')
        else:
            for f, r, c in possible_moves(pack(field, rooms)):
                fr = pack(f, r)
                e_total = c + energy
                if e_total < distances.get(fr, 999999):
                    distances[fr] = e_total
                    if c + energy < best_so_far:
                        # print_state(f, r, c, c + energy)
                        move(pack(f, r), c + energy)

    field = np.zeros((11), dtype=int)
    rooms = np.asarray(rooms)
    move(pack(field, rooms))
    print(f'Minimum Energy: {best_so_far}')


A = 1
B = 2
C = 3
D = 4

print('Part One:')
play([[B, A], [C, D], [B, C], [D, A]])
play([[B, C], [A, D], [B, D], [C, A]])

print('Part Two:')
play([[B, D, D, A], [C, C, B, D], [B, B, A, C], [D, A, C, A]])
play([[B, D, D, C], [A, C, B, D], [B, B, A, D], [C, A, C, A]])
