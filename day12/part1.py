import sys

m = sys.stdin.read().strip()
W, H = m.index("\n"), m.count("\n")
m = m.replace("\n", "")
S, E = m.index("S"), m.index("E")
m = m.replace("E", "z")
m = m.replace("S", "a")

fs = [
    [lambda p: p - W, lambda p: p // W],
    [lambda p: p + W, lambda p: p // W < H - 1],
    [lambda p: p - 1, lambda p: p % W],
    [lambda p: p + 1, lambda p: p % W != W - 1]
]

paths = [S]
cost = [-1 if i != S else 0 for i in range(len(m))]
while cost[E] == -1:
    p = min([path for path in paths if cost[path] != -1], key=lambda path: cost[path])
    for f in fs:
        if f[1](p) and cost[f[0](p)] == -1 and ord(m[p]) + 1 >= ord(m[f[0](p)]):
            paths.append(f[0](p))
            cost[f[0](p)] = cost[p] + 1
    paths.remove(p)
print(cost[E])