import sys
import itertools

data = sys.stdin.read().strip()

N_ROCK = int(1e12)

rocks = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (1, 0), (0, 1), (1, 1)},
]

s = set()

def falling0():
    return (2, max((p[1] + 1 for p in s), default=0) + 3)

def addt(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def down(rock):
    if not min(p[1] for p in rock):
        raise Exception
    for p in rock:
        if addt(p, (0, -1)) in s:
            raise Exception
    rock = {addt(p, (0, -1)) for p in rock}
    return rock

def left(rock):
    if min(p[0] for p in rock):
        if not {addt(p, (-1, 0)) for p in rock}.intersection(s):
            return {addt(p, (-1, 0)) for p in rock}
    return rock

def right(rock):
    if max(p[0] for p in rock) < 6:
        if not {addt(p, (1, 0)) for p in rock}.intersection(s):
            return {addt(p, (1, 0)) for p in rock}
    return rock

def minimize():
    conf = tuple(max((p[1] for p in s if p[0] == x), default=0) for x in range(7))
    h_min = min(conf) - 30
    return set((p for p in s if p[1] > h_min)) if h_min > 0 else s

def hg():
    return max((p[1] for p in s), default=0) + 1

def top():
    res = []
    for x in range(7):
        res.append(max((p[1] for p in s if p[0] == x), default=0))
    y_min = min(res)
    res = map(lambda x: x - y_min, res)
    return tuple(res)

move = {
    "<": left,
    ">": right
}

def drop(rock, it, i2):
    rock = {addt(p, falling0()) for p in rock}
    while True:
        dir = next(it)
        i2 +=1
        i2 %= len(data)
        rock = move[dir](rock)
        try:
            rock = down(rock)
        except:
            break
    return rock, i2


it = itertools.cycle(iter(data))
it_rock = itertools.cycle(iter(rocks))
i = N_ROCK
i1 = i2 = 0
conf = dict()
h = 0
while i:
    rock, i2 = drop(next(it_rock), it, i2)
    s |= rock
    s = minimize()
    if not h:
        if tuple(top() + (i1, i2)) in conf.keys():
            e = conf[tuple(top() + (i1, i2))]
            di = abs(i - e[0])
            dh = abs(hg() - e[1])
            h = (i // di) * dh
            i %= di
        conf[tuple(top() + (i1, i2))] = (i, hg())
    i -= 1
    i1 +=1
    i1 %= len(rocks)
print(hg() + h)
