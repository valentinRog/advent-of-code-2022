import sys

m = sys.stdin.read().strip()
W, H = m.index("\n"), m.count("\n")
m = m.replace("\n", "")
E = m.index("E")
m = m.replace("S", "a").replace("E", "z")

fs = [
    [lambda p: p - W, lambda p: p // W],
    [lambda p: p + W, lambda p: p // W < H - 1],
    [lambda p: p - 1, lambda p: p % W],
    [lambda p: p + 1, lambda p: p % W != W - 1]
]

res = -1
for s in [i for i, c in enumerate(m) if c == "a"]:
    paths = [s]
    cost = [-1 if i != s else 0 for i in range(len(m))]
    while len(paths) and cost[E] == -1:
        p = min([path for path in paths if cost[path] != -1], key=lambda path: cost[path])
        for f in fs:
            if f[1](p) and cost[f[0](p)] == -1 and ord(m[p]) + 1 >= ord(m[f[0](p)]):
                paths.append(f[0](p))
                cost[f[0](p)] = cost[p] + 1
        paths.remove(p)
    if res == -1 or (cost[E] != -1 and cost[E] < res):
        res = cost[E]
print(res)