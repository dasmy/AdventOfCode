from day_17inp import INPUT

r, p = INPUT.split("\n\n")

registers = {}
for reg, line in zip(["A", "B", "C"], r.split("\n")):
    registers[reg] = int(line.split(": ")[1])

p = p.split(": ")[1]
program = list(map(int, p.split(",")))

ip = 0


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


print(",".join(map(str, output)))
