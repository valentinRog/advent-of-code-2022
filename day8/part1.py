import sys

data = list(map(lambda x: list(map(lambda y: int(y), list(x))), sys.stdin.read().splitlines()))
s = set()
N = len(data)

NORTH = [[(i, j) for i in range(N)] for j in range(N)]
SOUTH = [[(N - 1 - i, j) for i in range(N)] for j in range(N)]
WEST = [[(i, j) for j in range(N)] for i in range(N)]
EST =[[(i, N - 1 - j) for j in range(N)] for i in range(N)]

for x in NORTH + SOUTH + WEST + EST:
    prev = -1
    for p in x:
        if data[p[0]][p[1]] > prev:
            prev = data[p[0]][p[1]]
            s.add(p)
print(len(s))