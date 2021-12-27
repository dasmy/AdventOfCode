
def block(w, z, div_z_26, n1, n2):
    ''' mul x 0
        add x z
        mod x 26
        if [div_z_26]:
            div z 26
        add x [n1]
        eql x w
        eql x 0
        mul y 0
        add y 25
        mul y x
        add y 1
        mul z y
        mul y 0
        add y w
        add y [n2]
        mul y x
        add z y'''
    x = ((z % 26) + n1) != w

    if div_z_26:
        z = z // 26

    if x:
        z *= 26
        z += w + n2

    return z


BLOCKS = [
    (False, 10, 10),
    (False, 13, 5),
    (False, 15, 12),
    (True, -12, 12),
    (False, 14, 6),
    (True, -2, 4),
    (False, 13, 15),
    (True, -12, 3),
    (False, 15, 7),
    (False, 11, 11),
    (True, -3, 2),
    (True, -13, 12),
    (True, -12, 4),
    (True, -13, 11)
]


prev_out = {0: 0}
for iblock, (div_z_26, n1, n2) in enumerate(BLOCKS):
    out = {}
    for digit in range(9, 0, -1):
        print(digit, end=' ')
        for z, s in prev_out.items():
            r = block(digit, z, div_z_26, n1, n2)
            out[r] = min(out.get(r, 1000000000000000), 10*s+digit)
    print(f'\n{iblock}: {len(out)}')
    prev_out = out

print(f'Minimum valid serial number: {out[0]}')
