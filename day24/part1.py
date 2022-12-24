import sys
import functools
import math
import collections
import itertools

dir = {
    ">": 1,
    "<": -1,
    "^": -1j,
    "v": 1j,
}

data = sys.stdin.read().strip().splitlines()
W = len(data[0])
H = len(data)

w = {
    (complex(x, y), dir[c])
    for y, line in enumerate(data)
    for x, c in enumerate(line) if c in "><^v"
}


def move(w):
    s = set()
    for p, d in w:
        if d == dir[">"]:
            s.add((p + d if (p + d).real < W - 1 else complex(1, p.imag), d))
        elif d == dir["<"]:
            s.add((p + d if (p + d).real else complex(W - 2, p.imag), d))
        elif d == dir["v"]:
            s.add((p + d if (p + d).imag < H - 1 else complex(p.real, 1), d))
        elif d == dir["^"]:
            s.add((p + d if (p + d).imag else complex(p.real, H - 2), d))
    return s


ws = []
for i in range(math.lcm(W - 2, H - 2)):
    ws.append({e[0] for e in w})
    w = move(w)

t0 = 1
while 1 + 1j in ws[t0]:
    t0 += 1

q = collections.deque([(1 + 1j, t0 % len(ws))])

s = set()
for t in itertools.count(t0 + 1):
    nq = collections.deque()
    while len(q):
        e = q.popleft()
        if e[0] not in ws[t % len(ws)]:
            if (e[0], t % len(ws)) not in s:
                nq.append((e[0], t % len(ws)))
                s.add((e[0], t % len(ws)))
        for d in dir.values():
            if 0 < (e[0] + d).imag < H - 1 and 0 < (e[0] + d).real < W - 1 and e[0] + d not in ws[t % len(ws)]:
                if (e[0] + d, t % len(ws)) not in s:
                    nq.append((e[0] + d, t % len(ws)))
                    s.add((e[0] + d, t % len(ws)))
    q = nq
    if complex(W - 2, H - 2) in set(e[0] for e in q):
        break


print(t + 1)