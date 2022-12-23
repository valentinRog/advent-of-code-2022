import sys
import collections
from itertools import chain

s = {
    complex(x, y)
    for y, line in enumerate(sys.stdin.read().splitlines())
    for x, c in enumerate(line) if c == "#"
}

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

q = collections.deque([N, S, W, E])

for _ in range(10):
    nps = dict()
    c = collections.Counter()
    for e in s:
        if all(e + d not in s for d in chain.from_iterable(v for v in dst.values())):
            nps[e] = e
        else:
            for d in q:
                if all(e + p not in s for p in dst[d]):
                    nps[e] = e + d
                    c.update((e + d,))
                    break
                else:
                    nps[e] = e
    s = {nps[e] if c[nps[e]] == 1 else e for e in s}
    q.append(q.popleft())

sr = set(map(lambda z: int(z.real), s))
si = set(map(lambda z: int(z.imag), s))
print(sum(
    complex(x, y) not in s
    for y in range(min(si), max(si) + 1)
    for x in range(min(sr), max(sr) + 1)
))
