from day_13inp import INPUT
import re
from pyscipopt import Model


pattern = re.compile(r"(?:Button A|Button B|Prize): X[\+=]([0-9]*), Y[\+=]([0-9]*)")


def splitline(line):
    m = pattern.match(line)
    return tuple([int(m.group(1)), int(m.group(2))])


total_tokens = 0
for claw_machine in INPUT.split("\n\n"):
    claw_machine = claw_machine.split("\n")

    Ax, Ay = splitline(claw_machine[0])
    Bx, By = splitline(claw_machine[1])
    Tx, Ty = splitline(claw_machine[2])

    model = Model("Claw Machine")
    a = model.addVar("a", vtype="INTEGER")
    b = model.addVar("b", vtype="INTEGER")
    model.setObjective(3 * a + 1 * b)
    model.addCons(a * Ax + b * Bx == Tx)
    model.addCons(a * Ay + b * By == Ty)
    model.optimize()
    sol = model.getBestSol()
    if model.getStatus() != "infeasible":
        sol_a = int(sol[a])
        sol_b = int(sol[b])

        tokens = 3 * sol_a + 1 * sol_b
        total_tokens += tokens

print(total_tokens)
