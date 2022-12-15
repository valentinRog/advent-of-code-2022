import sys

ROW = 2000000

data = []

for line in sys.stdin.read().strip().splitlines():
    points = filter(lambda x: x[0] == "x" or x[0] == "y", line.split())
    sx, sy, bx, by = map(int, map(lambda x: x.split("=")[-1].replace(",", "").replace(":", ""), points))
    data.append(((sx, sy),(bx, by)))

sensor = set()
beacon = set()
for line in data:
    sensor.add(line[0])
    beacon.add(line[1])

def addt(t1, t2):
    return tuple(sum(e) for e in zip(t1, t2))

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

res = set()
for line in data:
    dist_to_beacon = dist(line[0], line[1])
    dist_to_line = abs(line[0][1] - ROW)
    x = line[0][0]
    i = 0
    while dist_to_line + i <= dist_to_beacon:
        if (x + i, ROW) not in (sensor | beacon):
            res.add(x + i)
        if (x - i, ROW) not in (sensor | beacon):
            res.add(x - i)
        i += 1

print(len(res))