import sys

ROW = 4000000
# ROW = 20

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


y = 0
while y < ROW:
    print(y, end="\r")
    x = 0
    jumpy = -1
    while x < ROW:
        jump = 1
        stop = True
        ds = [abs(d - line[2]) for line in data if (d := dist((x, y), line[0])) <= line[2]]
        if not len(ds):
            print((x, y))
            print(4000000 * x + y)
            exit()
        x += max(ds) or 1
        jump = max(ds) or 1
        if jumpy == -1 or jump < jumpy:
            jumpy = jump
    y += jumpy >> 1 or 1
