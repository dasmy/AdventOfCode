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


best_cost = (1e16, set())

todo = {
    (start, dir, False): (0, set()),
}

while todo:
    new_todo = {}

    def add_entry(coord, cost, visited):
        try:
            existing_cost, existing_visited = new_todo[coord]

            if existing_cost < cost:
                pass  # drop path
            elif existing_cost == cost:
                # add existing path
                new_todo[coord] = (cost, existing_visited | visited)
            else:
                # replace existing path
                new_todo[coord] = (cost, visited)
        except KeyError:
            # insert new path
            new_todo[coord] = (cost, visited)

    for (pos, dir, just_turned), (cost_so_far, visited) in todo.items():
        if cost_so_far > best_cost[0]:
            continue
        elif pos == end:
            if cost_so_far == best_cost[0]:
                # add path
                best_cost = (cost_so_far, best_cost[1] | visited)
            else:
                # replace path
                best_cost = (cost_so_far, visited)

            print(cost_so_far, visited)
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

            v = visited | {pos}

            add_entry(((pos[0] + dr, pos[1] + dc), dir, False), cost_so_far + 1, v)

            if not just_turned:
                if dr != 0:
                    add_entry((pos, ">", True), cost_so_far + 1000, v)
                    add_entry((pos, "<", True), cost_so_far + 1000, v)
                else:
                    add_entry((pos, "^", True), cost_so_far + 1000, v)
                    add_entry((pos, "v", True), cost_so_far + 1000, v)

    todo = new_todo


print(best_cost[0], len(best_cost[1]) + 1)
