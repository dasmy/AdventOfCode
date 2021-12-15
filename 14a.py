from collections import defaultdict


def compute_polymerization(steps, template, rules):
    rules = dict(tuple(rule.split(' -> ')) for rule in rules.split('\n'))

    current_template = template
    for step in range(steps):
        molecule = []
        for i in range(len(current_template)):
            chars = current_template[i:i+2]
            molecule.append(chars[0])
            try:
                molecule.append(rules[chars])
            except KeyError:
                pass
        current_template = ''.join(molecule)
        print(f'Step: {step}: {current_template}')

    counters = defaultdict(lambda: 0)
    for char in current_template:
        counters[char] += 1

    maximum = 0
    minimum = len(current_template)
    for count in counters.values():
        maximum = max(maximum, count)
        minimum = min(minimum, count)

    print(f'Max {maximum}, Min {minimum}, Diff {maximum-minimum}')


compute_polymerization(
    10,
    'NNCB',
    '''CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
)

compute_polymerization(
    10,
    'VCOPVNKPFOOVPVSBKCOF',
    '''NO -> K
PO -> B
HS -> B
FP -> V
KN -> S
HV -> S
KC -> S
CS -> B
KB -> V
OB -> V
HN -> S
OK -> N
PC -> H
OO -> P
HF -> S
CB -> C
SB -> V
FN -> B
PH -> K
KH -> P
NB -> F
KF -> P
FK -> N
FB -> P
FO -> H
CV -> V
CN -> P
BN -> N
SC -> N
PB -> K
VS -> N
BP -> P
CK -> O
PS -> N
PF -> H
HB -> S
VN -> V
OS -> V
OC -> O
BB -> F
SK -> S
NF -> F
FS -> S
SN -> N
FC -> S
BH -> N
HP -> C
VK -> F
CC -> N
SV -> H
SO -> F
HH -> C
PK -> P
NV -> B
KS -> H
NP -> H
VO -> C
BK -> V
VV -> P
HK -> B
CF -> B
BF -> O
OV -> B
OH -> C
PP -> S
SP -> S
CH -> B
OF -> F
NK -> F
FV -> F
KP -> O
OP -> O
SS -> P
CP -> H
BO -> O
KK -> F
HC -> N
KO -> V
CO -> F
NC -> P
ON -> P
KV -> C
BV -> K
HO -> F
PV -> H
VC -> O
NH -> B
PN -> H
VP -> O
NS -> N
NN -> S
BS -> H
SH -> P
VB -> V
VH -> O
FH -> K
FF -> H
SF -> N
BC -> H
VF -> P'''
)
