import sys

ROW = 4000000

data = []

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for line in sys.stdin.read().strip().splitlines():
    points = filter(lambda x: x[0] == "x" or x[0] == "y", line.split())
    sx, sy, bx, by = map(int, map(lambda x: x.split(
        "=")[-1].replace(",", "").replace(":", ""), points))
    data.append(((sx, sy), (bx, by), dist((sx, sy), (bx, by))))


def addt(t1, t2):
    return tuple(sum(e) for e in zip(t1, t2))

def xjump(p):
    start = p[0]
    b, d = next(((line[0], line[2]) for line in data if dist(p, line[0]) <= line[2]))
    return min(b[0] - p[0] + d - abs(p[1] - b[1]) + 1, ROW)

def dist_to_border_max(p):
    return max([abs(d - line[2]) for line in data if (d := dist(p, line[0])) <= line[2]])

y = 0
while y < ROW:
    x = 0
    arr = []
    while x < ROW:
        try:
            arr.append(dist_to_border_max((x, y)))
            x += xjump((x, y))
        except:
            print(4_000_000 * x + y)
            exit()
    y += min(arr) >> 1 or 1
