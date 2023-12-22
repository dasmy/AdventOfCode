import re
import itertools
from string import ascii_uppercase
from collections import defaultdict
from copy import copy
from day_22 import INPUT_TEST, INPUT


def iter_all_strings():
    for size in itertools.count(1):
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)


class Brick:
    PATTERN = re.compile(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)')

    def __init__(self, id, line):
        self.id = id
        m = self.PATTERN.match(line)
        assert m is not None
        self.x = (int(m.group(1)), int(m.group(4)) + 1)
        self.y = (int(m.group(2)), int(m.group(5)) + 1)
        self.z = (int(m.group(3)), int(m.group(6)) + 1)
        assert self.x[0] < self.x[1]
        assert self.y[0] < self.y[1]
        assert self.z[0] < self.z[1]

    @property
    def layers(self):
        yield from range(self.z[0], self.z[1]+1)

    @property
    def upper(self):
        return self.z[1]

    @property
    def lower(self):
        return self.z[0]

    def drop(self):
        if self.lower == 1:
            return False
        else:
            self.z = (self.z[0] - 1, self.z[1] - 1)
            return True

    def undrop(self):
        self.z = (self.z[0] + 1, self.z[1] + 1)

    def intersects(self, other: 'Brick'):
        if self.x[1] <= other.x[0] or other.x[1] <= self.x[0]:
            return False
        elif self.y[1] <= other.y[0] or other.y[1] <= self.y[0]:
            return False
        elif self.z[1] <= other.z[0] or other.z[1] <= self.z[0]:
            return False
        else:
            return True

    def __repr__(self):
        return f'{self.id}   x: {self.x[0]} - {self.x[1]}   y: {self.y[0]} - {self.y[1]}   z: {self.z[0]} - {self.z[1]}'


def day_22a(inp):
    bricks = [Brick(i, line) for i, line in zip(iter_all_strings(), inp.split('\n'))]
    dropped_bricks = []
    dropped_tops = defaultdict(list)
    supports = defaultdict(list)
    supported_by = defaultdict(list)

    for brick in sorted(bricks, key=lambda b: b.lower):
        new_brick = copy(brick)

        while new_brick.drop():
            supported = False
            for other in dropped_tops[new_brick.lower + 1]:
                if new_brick.intersects(other):
                    supports[other.id].append(new_brick.id)
                    supported_by[new_brick.id].append(other.id)
                    supported = True
            if supported:
                new_brick.undrop()
                break

        dropped_bricks.append(new_brick)
        dropped_tops[new_brick.upper].append(new_brick)

    total = len(dropped_bricks)
    for brick in dropped_bricks:
        print(f'Checking brick {brick.id}, it supports {supports[brick.id]}')
        for other_id in supports[brick.id]:
            if len(supported_by[other_id]) == 1:
                print(f'    Supports brick {other_id} alone.')
                total -= 1
                break

    return total


print(day_22a(INPUT_TEST))
print(day_22a(INPUT))
