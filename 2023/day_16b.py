from day_16 import INPUT_TEST, INPUT


def _clamp_to_range(mirrors, beams):
    max_x = len(mirrors[0])
    max_y = len(mirrors)

    return [b for b in beams if 0 <= b.x < max_x and 0 <= b.y < max_y]


class Beam:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def propagate(self, mirrors):
        m = mirrors[self.y][self.x]

        if m == '-' and self.dy != 0:
            return [
                Beam(self.x-1, self.y, -1, 0),
                Beam(self.x+1, self.y, +1, 0),
            ]
        elif m == '|' and self.dx != 0:
            return [
                Beam(self.x, self.y-1, 0, -1),
                Beam(self.x, self.y+1, 0, +1),
            ]
        elif m == '/':
            self.dx, self.dy = -self.dy, -self.dx
        elif m == '\\':
            self.dx, self.dy = self.dy, self.dx

        self.x += self.dx
        self.y += self.dy
        return [self, ]

    def __repr__(self):
        dir = {
            (0, +1): 'v',
            (0, -1): '^',
            (+1, 0): '>',
            (-1, 0): '<',
        }[(self.dx, self.dy)]
        return f'({self.x}, {self.y} {dir})'


def day_16b(inp):
    mirrors = inp.split('\n')

    max_energy = 0

    max_x = len(mirrors[0])
    max_y = len(mirrors)

    test_beams = set()
    for x in range(max_x):
        test_beams.add(Beam(x, 0, 0, +1))
        test_beams.add(Beam(x, max_y-1, 0, -1))
    for y in range(max_y):
        test_beams.add(Beam(0, y, +1, 0))
        test_beams.add(Beam(max_x-1, y, -1, 0))

    for initial_beam in test_beams:
        all_beams = {initial_beam, }
        beams_done = set()
        touched = set()

        while all_beams:
            new_beams = set()
            for beam in all_beams:
                if (beam.x, beam.y, beam.dx, beam.dy) not in beams_done:
                    touched.add((beam.x, beam.y))
                    beams_done.add((beam.x, beam.y, beam.dx, beam.dy))
                    new_beams.update(_clamp_to_range(mirrors, beam.propagate(mirrors)))
            all_beams = new_beams

        max_energy = max(max_energy, len(touched))

    return max_energy


print(day_16b(INPUT_TEST))
print(day_16b(INPUT))
