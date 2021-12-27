from functools import cache


REG_ID = {'w': 0, 'x': 1, 'y': 2, 'z': 3}
OPCODES = {
    'add': lambda a, b: a + b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a // b,
    'mod': lambda a, b: a % b,
    'eql': lambda a, b: 1 if a == b else 0,
}


@cache
def execute_command(registers, func, op1, op2):
    op1 = REG_ID[op1]
    op2 = registers[REG_ID[op2]] if op2 in REG_ID else int(op2)

    return set_reg(registers, op1, func(registers[op1], op2))


def set_reg(registers, reg, value):
    result = list(registers)
    result[reg] = value
    return tuple(result)


@cache
def execute_block(inp, registers, block):
    #print(f'SOB\t\t{inp}, {registers}')
    registers = set_reg(registers, 0, inp)
    #print(f'inp w {inp}\t=>\t{inp}, {registers}')
    for op, cmd in block:
        registers = cmd(registers)
        #print(f'{op}\t=>\t{inp}, {registers}')
    return registers


def do_it(input):
    command_blocks = []
    for line in input.split('\n'):
        cmd = line.split(' ')

        if cmd[0] == 'inp':
            command_blocks.append([])
            assert len(cmd) == 2
            assert cmd[1] == 'w'
        else:
            command_blocks[-1].append((
                line,
                lambda registers, cmd=cmd: execute_command(registers, OPCODES[cmd[0]], cmd[1], cmd[2])
            ))

    command_blocks = [tuple(b) for b in command_blocks]

    prev_output = {(0, 0, 0, 0): 0}
    for iblock, block in enumerate(command_blocks):
        output = {}
        for input, seq in prev_output.items():
            for digit in range(1, 10):
                out = execute_block(digit, input, block)
                inp = seq * 10 + digit
                output[out] = max(output.get(out, 0), inp)
        print(f'{iblock:2d}: {len(output)}')
        prev_output = output

    sequences = []
    for registers, seq in output.items():
        if registers[3] == 0:
            sequences.append(seq)

    print(sequences)
    print(max(sequences))


do_it(
    '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -2
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y'''
)
