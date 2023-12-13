import numpy as np
from day_13 import INPUT_TEST, INPUT


def search(pattern):
    answer = []
    for p, f in zip((pattern, pattern.T), (100, 1)):
        n = len(p)
        for i_split in range(1, n):
            maxlen = min(n-i_split, i_split)
            before = np.flipud(p[i_split - maxlen:i_split])
            after = p[i_split:i_split + maxlen]
            assert before.shape == after.shape
            if np.all(before == after):
                answer.append(i_split * f)

    return answer[0] if len(answer) == 1 else answer


def search_smudge(lines):
    for line in lines:
        print(''.join('#' if l else '.' for l in line))
    pattern = np.asarray(lines, dtype=bool)

    reflection = search(pattern)
    for iy in range(pattern.shape[0]):
        for ix in range(pattern.shape[1]):
            changed_pattern = pattern.copy()
            changed_pattern[iy, ix] = not changed_pattern[iy, ix]
            changed_reflection = search(changed_pattern)
            if changed_reflection:
                if changed_reflection != reflection:
                    print(ix, iy, reflection, changed_reflection)
                    if isinstance(changed_reflection, list):
                        changed_reflection.remove(reflection)
                        assert len(changed_reflection) == 1
                        changed_reflection = changed_reflection[0]
                    return changed_reflection

    assert False


def day_13a(inp):
    total = 0
    lines = []
    for l in inp.split('\n'):
        if l:
            lines.append([s == '#' for s in l])
        else:
            total += search_smudge(lines)
            lines = []
    total += search_smudge(lines)

    return total


print(day_13a(INPUT_TEST))
print(day_13a(INPUT))
