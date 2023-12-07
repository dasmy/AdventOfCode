from day_06 import INPUT_TEST, INPUT


def distance_travelled(tc, T, vc=1):
    return vc * tc * (T - tc)


def day_06a(inp):
    lines = inp.split('\n')
    times = [int(i) for i in filter(None, lines[0][10:].split(' '))]
    distances = [int(i) for i in filter(None, lines[1][10:].split(' '))]

    margin = 1
    for T, s0 in zip(times, distances):
        c = 0
        for tc in range(T+1):
            s = distance_travelled(tc, T)
            if s > s0:
                c += 1

        margin *= c

    return margin


print(day_06a(INPUT_TEST))
print(day_06a(INPUT))
