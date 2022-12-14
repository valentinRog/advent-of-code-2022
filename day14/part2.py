import sys

data = [
    [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
     for line in sys.stdin.read().strip().splitlines()
]

X_MIN = min(min([p[0] for p in line]) for line in data) - 1000
X_MAX = max(max([p[0] for p in line]) for line in data) + 1000
Y_MIN = 0
Y_MAX = max(max([p[1] for p in line]) for line in data) + 50

W = X_MAX - X_MIN + 1
H = Y_MAX - Y_MIN + 1

m = [["." for _ in range(W)] for _ in range(H)]

for x in range(W):
    y = max(max([p[1] for p in line]) for line in data) - Y_MIN + 2
    m[y][x] = "x"

def print_m():
    for y in range(H):
        for x in range(W):
            if [x, y] == [500 - X_MIN, 0]:
                print("S", end="")
            else:
                print(m[y][x], end="")
        print()

for line in data:
    for i in range(len(line) - 1):
        px = sorted(line[i:i+2], key=lambda e: e[0])
        px1 = px[0][0] - X_MIN
        px2 = px[1][0] - X_MIN
        py = sorted(line[i:i+2], key=lambda e: e[1])
        py1 = py[0][1] - Y_MIN
        py2 = py[1][1] - Y_MIN
        for x in range(px1, px2 + 1):
            m[py1][x] = "#"
        for y in range(py1, py2 + 1):
            m[y][px1] = "#"

       
       
res = 0
while True:
    sp = [500 - X_MIN, 0]
    yo = 0
    while sp != [500 - X_MIN, 0] or not yo:
        sp[1] += 1
        yo = 1
        if m[sp[1]][sp[0]] == ".":
            continue
        elif m[sp[1]][sp[0] - 1] == ".":
            sp[0] -= 1
        elif m[sp[1]][sp[0] + 1] == ".":
            sp[0] += 1
        else:
            sp[1] -= 1
            break
    res += 1
    if sp == [500 - X_MIN, 0]:
        break
    m[sp[1]][sp[0]] = "o"
print_m()
print(res)
