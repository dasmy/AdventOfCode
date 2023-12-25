from math import isclose
from day_24 import INPUT_TEST, INPUT


class Hailstone:
    def __init__(self, line):
        pos, vel = line.split(' @ ')
        self.x = list(map(int, pos.split(', ')))
        self.v = list(map(int, vel.split(', ')))

    def __repr__(self):
        return f'{self.x} + {self.v} * t'

    def intersect(self, other):
        # x1 + t*v1 = x2 + u*v2
        #
        # x11 + t v11 = x21 + u v21  --> t = (x21 - x11 + u v21) / v11 = (x21-x11)/v11 + u v21/v11; u = t v11/v21 - (x21-x11)/v21
        # x12 + t v12 = x22 + u v22  --> t = (x22 - x12 + u v22) / v12 = (x22-x12)/v12 + u v22/v12; u = t v12/v22 - (x22-x12)/v22
        #
        # --> u = ( (x21-x11)/v11 - (x22-x12)/v12 ) / (v22/v12 - v21/v11)
        # --> t = ( (x21-x11)/v21 - (x22-x12)/v22 ) / (v11/v21 - v12/v22)

        x21_m_x11 = other.x[0] - self.x[0]
        x22_m_x12 = other.x[1] - self.x[1]

        denom = (other.v[1]/self.v[1] - other.v[0]/self.v[0])
        num = (x21_m_x11 / self.v[0] - x22_m_x12 / self.v[1])

        if denom == 0:
            # lines are parallel
            if num == 0:
                # lines are collinear/identical
                return True
            else:
                # lines are parallel and will never touch
                return 0, 0, -1, -1
        else:
            u = num / denom
            t = (x21_m_x11 / other.v[0] - x22_m_x12 / other.v[1]) / (self.v[0]/other.v[0] - self.v[1]/other.v[1])

            x = self.x[0] + t * self.v[0]
            y = self.x[1] + t * self.v[1]

            assert isclose(x, other.x[0] + u * other.v[0])
            assert isclose(y, other.x[1] + u * other.v[1])

            return x, y, t, u


def day_24a(inp, lims):
    hailstones = [Hailstone(line) for line in inp.split('\n')]

    count = 0
    for i in range(0, len(hailstones)):
        for j in range(i+1, len(hailstones)):
            x, y, t, u = hailstones[i].intersect(hailstones[j])

            if not t >= 0:
                continue

            if not u >= 0:
                continue

            if not lims[0] <= x <= lims[1]:
                continue

            if not lims[0] <= y <= lims[1]:
                continue

            count += 1

    return count


print(day_24a(INPUT_TEST, lims=(7, 27)))
print(day_24a(INPUT, lims=(200000000000000, 400000000000000)))
