import sys
import itertools
from operator import itemgetter

data = [
    [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
     for line in sys.stdin.read().strip().splitlines()
]

s = set()
for line in data:
    for i in range(len(line) - 1):
        px = sorted(map(itemgetter(0), line[i:i+2]))
        py = sorted(map(itemgetter(1), line[i:i+2]))
        for x in range(px[0], px[1] + 1):
            s.add((x, py[0]))
        for y in range(py[0], py[1] + 1):
            s.add((px[0], y))

Y_MAX = max(s, key=lambda x: x[1])[1]

def fall(sp=(500, 0)):
    for d in ((0, 1), (-1, 1), (1, 1)):
        s.add((sp[0] + d[0], Y_MAX + 2))
        if (p := tuple(sum(x) for x in zip(sp, d))) not in s:
            return fall(p)
    return sp

for n in itertools.count():
    if ((500, 0) in s):
        break
    s.add(fall())
print(n)
