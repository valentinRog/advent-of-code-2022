import sys
from itertools import count

data = [
    [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
     for line in sys.stdin.read().strip().splitlines()
]

Y_MAX = max(max([p[1] for p in line]) for line in data)

s = set()
for line in data:
    for i in range(len(line) - 1):
        px = sorted(line[i:i+2], key=lambda e: e[0])
        px1 = px[0][0]
        px2 = px[1][0]
        py = sorted(line[i:i+2], key=lambda e: e[1])
        py1 = py[0][1]
        py2 = py[1][1]
        for x in range(px1, px2 + 1):
            s.add((x, py1))
        for y in range(py1, py2 + 1):
            s.add((px1, y))

n = 0
while True:
    sp = [500, 0]
    while (500, 0) not in s:
        sp[1] += 1
        s.add((sp[0], Y_MAX + 2))
        s.add((sp[0] - 1, Y_MAX + 2))
        s.add((sp[0] + 1, Y_MAX + 2))
        if tuple(sp) not in s:
            continue
        elif (sp[0] - 1, sp[1]) not in s:
            sp[0] -= 1
        elif (sp[0] + 1, sp[1]) not in s:
            sp[0] += 1
        else:
            sp[1] -= 1
            break
    if (500, 0) in s:
        break
    s.add(tuple(sp))
    n += 1
print(n)
