import sys
from itertools import chain

data = list(map(lambda x: list(map(lambda y: int(y), list(x))), sys.stdin.read().splitlines()))
s = set()
N = len(data)

def north(i, j): return (i, j)
def south(i, j): return (N - 1 - i, j)
def west(i, j): return (j, i)
def east(i, j): return (j, N - 1 - i)
def g(f): return ([f(i, j) for i in range(N)] for j in range(N))

for x in chain(g(north), g(south), g(west), g(east)):
    prev = -1
    for p in x:
        if data[p[0]][p[1]] > prev:
            prev = data[p[0]][p[1]]
            s.add(p)
print(len(s))