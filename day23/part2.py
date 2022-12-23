import sys
from collections import deque
import itertools

s = set()

for y, line in enumerate(sys.stdin.read().splitlines()):
    for x, c in enumerate(line):
        if c == "#":
            s.add(complex(x, y))


def print_conf():
    for y in range(min(map(lambda z: int(z.imag), s)), max(map(lambda z: int(z.imag), s)) + 1):
        for x in range(min(map(lambda z: int(z.real), s)), max(map(lambda z: int(z.real), s)) + 1):
            if complex(x, y) in s:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


N = -1j
S = 1j
W = -1
E = 1

dst = {
    N: (N, N + E, N + W),
    S: (S, S + E, S + W),
    W: (W, N + W, S + W),
    E: (E, N + E, S + E),
}

q = [N, S, W, E]


def isfree(e):
    for v in dst.values():
        for d in v:
            if e + d in s:
                return False
    return True

def stuck(nps):
    for k, v in nps.items():
        if k != v:
            return False
    return True

for i in itertools.count():
    nps = dict()
    for e in s:
        if isfree(e):
            nps[e] = e
        else:
            for d in q:
                if e + dst[d][0] not in s and e + dst[d][1] not in s and e + dst[d][2] not in s:
                    nps[e] = e + d
                    break
                else:
                    nps[e] = e
    if stuck(nps):
        print(i + 1)
        break
    for e in set(s):
        if list(nps.values()).count(nps[e]) == 1:
            s.remove(e)
            s.add(nps[e])
    q = q[1:] + [q[0]]
    
