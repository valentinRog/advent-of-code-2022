import sys

data = [
    [tuple(map(int, p.split(","))) for p in line.split(" -> ")]
     for line in sys.stdin.read().strip().splitlines()
]

X_MIN = min(min([p[0] for p in line]) for line in data)
X_MAX = max(max([p[0] for p in line]) for line in data)
Y_MIN = min(min([p[1] for p in line]) for line in data)
Y_MAX = max(max([p[1] for p in line]) for line in data)

W = X_MAX - X_MIN + 1
H = Y_MAX - Y_MIN + 1

m = [["." for _ in range(W)] for _ in range(H)]

def print_m():
    for y in range(H):
        for x in range(W):
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
            
print_m()
