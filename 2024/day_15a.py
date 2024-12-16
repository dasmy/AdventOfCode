from day_15inp import INPUT
import numpy as np

field, instructions = INPUT.split("\n\n")


items = {
    "#": set(),
    "O": set(),
    "@": set(),
}
for r, row in enumerate(field.split("\n")):
    for c, f in enumerate(row):
        if f != ".":
            items[f].add((r, c))

rmax = r
cmax = c


def print_items(items):
    f = np.empty((rmax + 1, cmax + 1), dtype=str)
    f[:, :] = "."
    for t, l in items.items():
        for r, c in l:
            f[r, c] = t

    print("\n".join("".join(row) for row in f))


print_items(items)

for instr in instructions:
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

    print("\n" + instr)
    to_move = [("@", items["@"].pop())]

    while True:
        to_check = to_move[-1]
        next = (to_check[1][0] + dr, to_check[1][1] + dc)
        if next in items["#"]:
            # blocked - put everything back
            for item in to_move:
                items[item[0]].add(item[1])
            break
        elif next in items["O"]:
            # collected a package
            to_move.append(("O", next))
            items["O"].remove(next)
            continue
        else:
            print(instr, to_move)
            # free spot - move everything we have
            for item in to_move:
                newpos = (item[1][0] + dr, item[1][1] + dc)
                items[item[0]].add(newpos)
            break

    print_items(items)

gps = 0
for box in items["O"]:
    gps += 100 * box[0] + box[1]

print(gps)
