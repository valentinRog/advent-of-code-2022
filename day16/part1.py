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

print(data)

@functools.cache
def best(t=0, valve="AA", opened=None):
    if opened is None:
        opened = tuple()
    if t == 30:
        return 0
    score = sum([data[e]["rate"] for e in opened])
    s1 = 0
    if data[valve]["rate"] and valve not in opened:
        s1 = best(t + 1, valve, tuple(opened + (valve,)))
    s2 = max(best(t + 1, v, opened) for v in data[valve]["nb"])
    return score + max(s1, s2)
  
print(best())