from day_17inp import INPUT
from copy import copy
from itertools import count


r, p = INPUT.split("\n\n")

registers_orig = {}
for reg, line in zip(["A", "B", "C"], r.split("\n")):
    registers_orig[reg] = int(line.split(": ")[1])

p = p.split(": ")[1]
program = list(map(int, p.split(",")))


# 2,4  B := A % 8
# 1,1  B := B ^ 1
# 7,5  C := A / 2**B
# 1,5  B := B ^ 5
# 4,3  B := B ^ C
# 5,5  out B % 8
# 0,3  A := A / 8
# 3,0  jnz 0


def run_program(A):
    registers = copy(registers_orig)
    registers["A"] = A

    def cop(data):
        if 0 <= data <= 3:
            return data
        elif data == 4:
            return registers["A"]
        elif data == 5:
            return registers["B"]
        elif data == 6:
            return registers["C"]
        else:
            assert False

    output = []

    ip = 0

    def op(ip, instr, data):
        if instr == 0:  # adv
            registers["A"] //= 2 ** cop(data)
        elif instr == 1:  # bxl
            registers["B"] ^= data
        elif instr == 2:  # bst
            registers["B"] = cop(data) % 8
        elif instr == 3:  # jnz
            if registers["A"] != 0:
                return data
        elif instr == 4:  # bxc
            registers["B"] ^= registers["C"]
        elif instr == 5:  # out
            output.append(cop(data) % 8)
        elif instr == 6:  # bdv
            registers["A"] = registers["A"] // 2 ** cop(data)
        elif instr == 7:  # bxl
            registers["C"] = registers["A"] // 2 ** cop(data)
        else:
            assert False

        return ip + 2

    while ip < len(program):
        ip = op(
            ip,
            instr=program[ip],
            data=program[ip + 1],
        )

    return output


ideal_A = 0
step = 2
for pos in range(14, -1, -step):
    for digit in range(8**step):
        A = ideal_A + digit * 8**pos
        result = run_program(A)

        # print(pos, oct(A), A, result, result[pos:], program[pos:])

        if result[pos:] == program[pos:]:
            ideal_A = A
            print(pos, oct(ideal_A), result[pos:])
            break
    else:
        assert False

print(ideal_A)
