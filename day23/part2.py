import sys
import collections
import itertools
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

for i in itertools.count():
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
    if all(k == v for k, v in nps.items()):
        print(i + 1)
        break
    s = {nps[e] if c[nps[e]] == 1 else e for e in s}
    q.append(q.popleft())
