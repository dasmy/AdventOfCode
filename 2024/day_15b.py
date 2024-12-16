from day_15inp import INPUT
import numpy as np
from itertools import chain

field, instructions = INPUT.split("\n\n")


items = {
    "#": set(),
    "[": set(),
    "]": set(),
    "@": set(),
}
for r, row in enumerate(field.split("\n")):
    for c, f in enumerate(row):
        if f == "#":
            items["#"].add((r, 2 * c + 0))
            items["#"].add((r, 2 * c + 1))
        elif f == "O":
            items["["].add((r, 2 * c + 0))
            items["]"].add((r, 2 * c + 1))
        elif f == "@":
            items["@"].add((r, 2 * c + 0))

rmax = r
cmax = 2 * c + 1

checksum = {f: len(c) for f, c in items.items()}


def print_items(items, instr):
    f = np.empty((rmax + 1, cmax + 1), dtype=str)
    f[:, :] = " "
    for t, l in items.items():
        for r, c in l:
            f[r, c] = instr if t == "@" else t

    print("\n".join("".join(row) for row in f))


for istep, instr in enumerate(instructions):
    if instr == "^":
        dr, dc = -1, 0
    elif instr == "v":
        dr, dc = 1, 0
    elif instr == "<":
        dr, dc = 0, -1
    elif instr == ">":
        dr, dc = 0, 1
    else:
        continue

    print_items(items, instr)
    print(f"\n{istep} - {instr}")
    this_checksum = {f: len(c) for f, c in items.items()}
    if checksum != this_checksum:
        print(f"error: {this_checksum}")

    to_move = {
        "payload": set(),
        "front": set([("@", next(iter(items["@"])))]),
    }

    while True:
        if not to_move["front"]:
            # free path - move everything we have
            # print(instr, to_move)
            for item in to_move["payload"]:
                items[item[0]].remove(item[1])

            for item in to_move["payload"]:
                newpos = (item[1][0] + dr, item[1][1] + dc)
                items[item[0]].add(newpos)
        else:
            new_front = set()

            for to_check in to_move["front"]:
                nextpos = (to_check[1][0] + dr, to_check[1][1] + dc)

                if nextpos in items["#"]:
                    # blocked - put everything back
                    for item in chain.from_iterable(to_move.values()):
                        items[item[0]].add(item[1])
                    break

                elif nextpos in items["["]:
                    to_move["payload"].add(to_check)

                    if dr == 0:
                        to_move["payload"].add(("[", nextpos))
                    else:
                        new_front.add(("[", nextpos))

                    nextpos = (nextpos[0], nextpos[1] + 1)
                    assert nextpos in items["]"]
                    to_check = ("]", nextpos)
                    new_front.add(to_check)

                elif nextpos in items["]"]:
                    to_move["payload"].add(to_check)

                    if dr == 0:
                        to_move["payload"].add(("]", nextpos))
                    else:
                        new_front.add(("]", nextpos))

                    nextpos = (nextpos[0], nextpos[1] - 1)
                    assert nextpos in items["["]
                    to_check = ("[", nextpos)
                    new_front.add(to_check)
                else:
                    to_move["payload"].add(to_check)

            else:
                to_move["front"] = new_front
                continue

        break


gps = 0
for box in items["["]:
    gps += 100 * box[0] + box[1]

print(gps)
