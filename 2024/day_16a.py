from day_16inp import INPUT


road = set()
for r, row in enumerate(INPUT.split("\n")):
    for c, f in enumerate(row):
        if f == ".":
            road.add((r, c))
        elif f == "S":
            road.add((r, c))
            start = (r, c)
            dir = "<"
        elif f == "E":
            end = (r, c)


best_cost = 1e16

todo = {
    (start, dir, False): 0,
}

while todo:
    new_todo = {}

    def add_entry(coord, cost):
        if new_todo.get(coord, 1e16) < cost:
            pass
        else:
            new_todo[coord] = cost

    for (pos, dir, just_turned), cost_so_far in todo.items():
        if cost_so_far >= best_cost:
            continue
        elif pos == end:
            best_cost = cost_so_far
            print(cost_so_far)
        elif pos not in road:
            continue  # hit a wall
        else:
            if dir == "^":
                dr, dc = -1, 0
            elif dir == "v":
                dr, dc = 1, 0
            elif dir == "<":
                dr, dc = 0, -1
            elif dir == ">":
                dr, dc = 0, 1

            add_entry(((pos[0] + dr, pos[1] + dc), dir, False), cost_so_far + 1)

            if not just_turned:
                if dr != 0:
                    add_entry((pos, ">", True), cost_so_far + 1000)
                    add_entry((pos, "<", True), cost_so_far + 1000)
                else:
                    add_entry((pos, "^", True), cost_so_far + 1000)
                    add_entry((pos, "v", True), cost_so_far + 1000)

    todo = new_todo
