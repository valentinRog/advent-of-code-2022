import sys
from operator import getitem
import itertools

data = sys.stdin.read().strip()

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

def print_config(s):
    for y in reversed(range(30)):
        for x in range(7):
            if (x, y) in s:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print("-------")

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

move = {
    "<": left,
    ">": right
}

it = itertools.cycle(iter(data))
i = 0
for rock in itertools.cycle(rocks):
    rock = {addt(p, falling0()) for p in rock}
    while True:
        dir = next(it)
        rock = move[dir](rock)
        # print_config(s | rock)
        try:
            rock = down(rock)
        except:
            break
        # print_config(s | rock)
    s |= rock
    print(i, end="\r")
    i += 1
    if i == 2022:
        break

print(max(p[1] for p in s) + 1)
