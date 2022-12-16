import sys
import functools
from itertools import permutations

data = {
    line.split()[1]: {
        "rate": int(line.split()[4].split("=")[-1][:-1]),
        "nb": [nb.replace(",", "") for nb in line.split("to")[-1].split()[1:]]
    }
    for line in sys.stdin.read().strip().splitlines()
}

@functools.cache
def best(t=0, valve="AA", opened=None):
    if opened is None:
        opened = tuple()
    if t == 26:
        return 0, opened
    score = sum([data[e]["rate"] for e in opened])
    s1 = 0
    back1 = ()
    if data[valve]["rate"] and valve not in opened:
        s1, back1 = best(t + 1, valve, tuple(opened + (valve,)))
    s2, back2 = max((best(t + 1, v, opened) for v in data[valve]["nb"]), key=lambda x: x[0])
    if s1 > s2:
        return score + s1, back1
    return score + s2, back2

score, opened = best()
for e in opened:
    data[e]["rate"] = 0
best.cache_clear()
print(score + best()[0])
