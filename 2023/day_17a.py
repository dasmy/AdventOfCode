from heapq import heapify, heappush, heappop
from day_17 import INPUT_TEST, INPUT


class State:
    def __init__(self, row, col, dr, dc, steps):
        self.row = row
        self.col = col
        self.dr = dr
        self.dc = dc
        self.steps = steps

    def __lt__(self, other):
        return self.steps < other.steps

    @property
    def __key(self):
        return (self.row, self.col, self.dr, self.dc, self.steps)

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, other):
        if isinstance(other, State):
            return self.__key == other.__key
        return NotImplemented


def day_17a(inp):
    grid = inp.split('\n')

    max_row = len(grid)
    max_col = len(grid[0])

    visited = set()
    todo = [(0, State(0, 0, 0, 0, 0))]
    heapify(todo)

    while todo:
        heat_loss, state = heappop(todo)

        if state.row + 1 == max_row and state.col + 1 == max_col:
            return heat_loss

        if state not in visited:
            visited.add(state)

            if state.steps < 3:
                new_row = state.row + state.dr
                new_col = state.col + state.dc

                if 0 <= new_row < max_row and 0 <= new_col < max_col:
                    total_heat = heat_loss + int(grid[new_row][new_col])
                    heappush(todo, (total_heat, State(new_row, new_col, state.dr, state.dc, state.steps + 1)))

            for new_dr, new_dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if (new_dr, new_dc) != (state.dr, state.dc) and (new_dr, new_dc) != (-state.dr, -state.dc):
                    new_row = state.row + new_dr
                    new_col = state.col + new_dc

                    if 0 <= new_row < max_row and 0 <= new_col < max_col:
                        total_heat = heat_loss + int(grid[new_row][new_col])
                        heappush(todo, (total_heat, State(new_row, new_col, new_dr, new_dc, 1)))

    assert False


print(day_17a(INPUT_TEST))  # 102
print(day_17a(INPUT))  # 1138
