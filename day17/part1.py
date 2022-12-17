import sys
import itertools

data = sys.stdin.read().strip()

N_ROCK = 2022

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
    h_min = min(conf) - 5
    return set((p for p in s if p[1] > h_min)) if h_min > 0 else s

def hg():
    return max((p[1] for p in s), default=0) + 1

move = {
    "<": left,
    ">": right
}

def drop(rock, it):
    rock = {addt(p, falling0()) for p in rock}
    while True:
        dir = next(it)
        rock = move[dir](rock)
        try:
            rock = down(rock)
        except:
            break
    return rock


it = itertools.cycle(iter(data))
it_rock = itertools.cycle(iter(rocks))
i = N_ROCK
while i:
    s |= drop(next(it_rock), it)
    s = minimize()
    print(i, end="\r")
    i -= 1
print(hg())
