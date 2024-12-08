from collections import defaultdict
from itertools import permutations
from day_08inp import INPUT


class Vec2D:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __sub__(self, other):
        return Vec2D(self.row - other.row, self.col - other.col)

    def __add__(self, other):
        return Vec2D(self.row + other.row, self.col + other.col)

    def is_in_box(self, rows, cols):
        return self.row >= 0 and self.row < rows and self.col >= 0 and self.col < cols

    def __call__(self):
        return (self.row, self.col)


antinodes = set()
antennas = defaultdict(list)

rows = len(INPUT.split("\n"))
cols = len(INPUT.split("\n")[0])

for irow, row in enumerate(INPUT.split("\n")):
    for icol, c in enumerate(row):
        if c != ".":
            antennas[c].append(Vec2D(irow, icol))

for antenna, positions in antennas.items():
    for a, b in permutations(positions, r=2):
        delta = b - a
        if (a - delta).is_in_box(rows, cols):
            antinodes.add((a - delta)())
        if (b + delta).is_in_box(rows, cols):
            antinodes.add((b + delta)())

print(len(antinodes))
