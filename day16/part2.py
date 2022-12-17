import sys
import functools
from itertools import permutations

data = {
    line.split()[1]: {
        "rate": int(line.split()[4].split("=")[-1][:-1]),
        "nb": [nb.replace(",", "") for nb in line.split("to")[-1].split()[1:]]
    }
    for line in sys.stdin.read().strip().splitlines()
}

TICK = 26

def dist(a, b, s=None):
    if s is None:
        s = tuple()
    if a == b:
        return 0
    return 1 + min((dist(x, b, tuple(s + (a,))) for x in data[a]["nb"] if x not in s), default=100)


for k in data.keys():
    data[k]["dist"] = {
        o: dist(k, o)
        for o in data.keys()
    }

keys = list(filter(lambda x: data[x]["rate"] > 0, data.keys()))
path = []
arr = [(0, ["AA"])]
while len(arr):
    new_arr = []
    for e in arr:
        for k in keys:
            if k not in e[1]:
                tmp = e[1] + [k]
                cost = data[tmp[-2]]["dist"][tmp[-1]] + 1
                path.append(tmp)
                if e[0] + cost <= TICK or len(tmp) == len(keys) + 1:
                    path.append(tmp)
                if e[0] + cost < TICK and len(tmp) != len(keys) + 1:
                    new_arr.append((e[0] + cost, tmp))
    arr = list(new_arr)

def score(p):
    rates = [0]
    res = 0
    d = data[p[0]]["dist"][p[1]]
    for tick in range(TICK):
        res += sum(rates)
        if d:
            d -= 1
        else:
            p = p[1:]
            d = data[p[0]]["dist"][p[1]] if len(p) > 1 else 0
            if len(p):
                rates.append(data[p[0]]["rate"])
    return res

print(len(path))

bitset = []

path = sorted(path, key=functools.cmp_to_key(lambda x, y: score(x) - score(y)), reverse=True)

for e in path:
    n = 0
    for v in e[1:]:
        n += 1 << keys.index(v)
    bitset.append(n)

scores = [score(p) for p in path]

res = 0
for i1 in range(len(path)):
    for i2 in range(len(path)):
        if not (bitset[i1] & bitset[i2]):
            if (x := scores[i1] + scores[i2]) > res:
                res = x
            break
print(res)
