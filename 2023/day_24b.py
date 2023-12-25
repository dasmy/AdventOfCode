from sympy import var, Eq, solve
from day_24 import INPUT_TEST, INPUT


class Hailstone:
    def __init__(self, line):
        pos, vel = line.split(' @ ')
        self.x = list(map(int, pos.split(', ')))
        self.v = list(map(int, vel.split(', ')))

    def equation(self, comp: int, t: str):
        return f'{self.x[comp]} + {self.v[comp]} * {t}'

    def __repr__(self):
        return f'{self.x} + {self.v} * t'


def day_24b(inp):
    hailstones = [Hailstone(line) for line in inp.split('\n')]

    x = var('x')
    y = var('y')
    z = var('z')
    var('u')
    var('v')
    var('w')

    equations = []

    for i, hailstone in enumerate(hailstones):
        t_name = f't{i}'
        var(t_name)

        equations.append(Eq(eval(f'x + u * {t_name}'), eval(hailstone.equation(0, t_name))))
        equations.append(Eq(eval(f'y + v * {t_name}'), eval(hailstone.equation(1, t_name))))
        equations.append(Eq(eval(f'z + w * {t_name}'), eval(hailstone.equation(2, t_name))))

        # considering three lines is sufficient to get 9 eqns for the 9 unknowns
        if len(equations) >= 9:
            break

    sln = solve(equations)
    assert len(sln) == 1
    sln = sln[0]

    print(sln)
    return sln[x] + sln[y] + sln[z]


print(day_24b(INPUT_TEST))
print(day_24b(INPUT))
