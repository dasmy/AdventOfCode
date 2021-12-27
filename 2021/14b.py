from collections import defaultdict
import numpy as np


def compute_polymerization(steps, template, rules):
    rules = dict(tuple(rule.split(' -> ')) for rule in rules.split('\n'))

    pairs = defaultdict(lambda: 0)
    for i in range(len(template)):
        chars = template[i:i+2]
        pairs[chars] += 1

    for step in range(steps):
        new_pairs = defaultdict(lambda: 0)
        for pair, count in pairs.items():
            try:
                insertion = rules[pair]
                new_pairs[pair[0] + insertion] += count
                new_pairs[insertion + pair[1]] += count
            except KeyError:
                new_pairs[pair] += count
        pairs = new_pairs

    counter = np.zeros((26,), dtype=int)
    for pair, count in pairs.items():
        for char in pair:
            counter[ord(char) - ord('A')] += count

    counter //= 2

    maximum = counter[counter > 0].max()
    minimum = counter[counter > 0].min()

    print(f'Max {maximum}, Min {minimum}, Diff {maximum-minimum}')


compute_polymerization(
    40,
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
    40,
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
