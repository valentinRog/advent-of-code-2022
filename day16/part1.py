import sys
import functools
import collections

data = {
    line.split()[1]: {
        "rate": int(line.split()[4].split("=")[-1][:-1]),
        "nb": [nb.replace(",", "") for nb in line.split("to")[-1].split()[1:]]
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

T = 30


@functools.cache
def dfs(t=0, valve="AA", opened=0):
    if t == T:
        return 0
    score = sum(
        data[e]["rate"]
        for i, e in enumerate(valves) if opened & 1 << i
    )
    res = (T-t)*score
    for v in filter(lambda x: not opened & 1 << x, range(len(valves))):
        d = min(dist(valve, valves[v]) + 1, T - t)
        res = max(res, dfs(t + d, valves[v], opened | 1 << v) + d*score)
    return res


print(dfs())
