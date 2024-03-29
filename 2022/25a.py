input = '''21==112=11=100-
1--0=-=22-
2121
10112
1=0=00
1=0-01-000--=122-
2111-
10-=-=2=0=-2
1=0112==2
2-2=1
210
11-111
12=2=221--00-1
1=--2-0001--=1=
10001==0001212-
12=1
11=1-=0=
1=10000102-2=
2=--221-1-00
2-10=-1-=1---2=222
1-=21022=-00=2
120=-221=2--=121
1=---00==-2020=0201
1=0=
200-=21=0---1=22
1=10-12=2-12
11210==0-=0-120
2--22=0-0=-12=1
1=-000
1=2--20=1
111---1=1-12=-=
1=-=2=1100-12==
2110=0===11-1=
10=1
1=-0
1-===102--0=1-1210-0
2010-2=1--=01--
210-11===-12
1=-2111=--1200
100
1=21--==-=-210102=
2-2=211--01
1--22=-
1121
1222=100-12002==-
1=20=1=-11112=2021
1102=0-11212
2=--==-002
2-=0=-=-
2-220--
122=02
1=012---2=0
1--=--21
1-=01202=-1
22=02
1=---2=-2202
1-==-
122-2=1-02
111-0-0120-10210
201
210=-0-==110201-11=
21
22110-2==0-0
11210=00=1-0=-022
1120==
2=--=2-011=
1--2-2--0-010=1-
1=--021-==--=102=
11=210=
2=001201
21==-0=21
1=00=
1-1
10--10000-=212--
10211
10=1=12201-112-
1=01=
122-1
202-=1222
22-111
122010-0=22121=-=-
102
1-001=0==222=2
2-0=1-1-1--
2---20=22=11212
1=0=11-2212-==-1
2=011-
1-1-01012-
21=22===-
22=20--=2=2=--021-
1===0==
2=12222100
2=
11-1==20=0-20
22120-1-11--
2-
1==1--2-==2=211
212-2=2212===-1-=-
10=
200=201=
1=21=
1==
11210=02102----2
2=-11==2121-100=-
11=-=0==
120=2==
1-1=102--2-=-=02=0
102=-1
1==202202221102=
100=12=
11-=1-12020-2=1=
10==02200=
1====02
1=-
101==2=-=-=01-=0
1-1=-1022121=-0
2212====
11=02=02===1=222-12
112=12----12
202=-1--0020
1=20-1=02000
1-
11=20120=
112==120-
22
1-1-11--2020
11='''

powers_of_five = [5**i for i in range(20)]


def snafu_to_dec(snafu):
    snafu = snafu.strip()
    result = 0
    for p, char in zip(powers_of_five, reversed(snafu)):
        if char == '=':
            result -= 2*p
        elif char == '-':
            result -= p
        elif char == '0':
            pass
        elif char == '1':
            result += p
        elif char == '2':
            result += 2*p
        else:
            raise ValueError(f'Unexpected char {char}')

    return result


def dec_to_snafu(dec):
    snafu = ''
    while dec > 0:
        digit = dec % 5
        dec //= 5
        if digit <= 2:
            snafu = str(digit) + snafu
        else:
            snafu = {3: '=', 4: '-'}[digit] + snafu
            dec += 1

    return snafu


assert snafu_to_dec('1=-0-2') == 1747
assert snafu_to_dec('12111') == 906
assert snafu_to_dec('2=0=') == 198
assert snafu_to_dec('21') == 11
assert snafu_to_dec('2=01') == 201
assert snafu_to_dec('111') == 31
assert snafu_to_dec('20012') == 1257
assert snafu_to_dec('112') == 32
assert snafu_to_dec('1=-1=') == 353
assert snafu_to_dec('1-12') == 107
assert snafu_to_dec('12') == 7
assert snafu_to_dec('1=') == 3
assert snafu_to_dec('122') == 37

assert dec_to_snafu(1) == '1'
assert dec_to_snafu(2) == '2'
assert dec_to_snafu(3) == '1='
assert dec_to_snafu(4) == '1-'
assert dec_to_snafu(5) == '10'
assert dec_to_snafu(6) == '11'
assert dec_to_snafu(7) == '12'
assert dec_to_snafu(8) == '2='
assert dec_to_snafu(9) == '2-'
assert dec_to_snafu(10) == '20'
assert dec_to_snafu(15) == '1=0'
assert dec_to_snafu(20) == '1-0'
assert dec_to_snafu(2022) == '1=11-2'
assert dec_to_snafu(12345) == '1-0---0'
assert dec_to_snafu(314159265) == '1121-1110-1=0'

sum_dec = sum(snafu_to_dec(line) for line in input.split('\n'))
print(sum_dec)
print(dec_to_snafu(sum_dec))
