import sys
import functools
import collections

data = {
    line.split()[1]: {
        "rate": int(line.split()[4].split("=")[-1][:-1]),
        "nb": [nb.replace(",", "") for nb in line.split("to")[-1].split()[1:]],
    }
    for line in sys.stdin.read().strip().splitlines()
}


@functools.cache
def dist(a, b):
    q = collections.deque([(a, 0)])
    visited = set()
    while True:
        node, d = q.popleft()
        if b in data[node]["nb"]:
            return d + 1
        for node in filter(lambda e: e not in visited, data[node]["nb"]):
            q.append((node, d + 1))
            visited.add(node)


valves = [k for k, v in data.items() if v["rate"]]

T = 26
paths = []


def dfs(t=0, valve="AA", opened=0, score=0):
    if t == T:
        paths.append((score, opened))
        return
    s = sum(data[e]["rate"] for i, e in enumerate(valves) if opened & 1 << i)
    for v in filter(lambda x: not opened & 1 << x, range(len(valves))):
        d = min(dist(valve, valves[v]) + 1, T - t)
        dfs(t + d, valves[v], opened | 1 << v, score + d * s)
    paths.append((score + (T - t) * s, opened))


dfs()
paths.sort(reverse=True)
res = 0

for s1, o1 in paths:
    for s2, o2 in paths:
        if not o1 & o2:
            res = max(res, s1 + s2)
            break
        if s1 + s2 < res:
            break
print(res)
