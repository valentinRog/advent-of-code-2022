import sys

data = list(map(lambda x: list(map(lambda y: int(y), list(x))), sys.stdin.read().splitlines()))
s = set()
N = len(data)

for j in range(N):
    prev_max = -1
    for i in range(N):
        if data[i][j] > prev_max:
            s.add((i, j))
            prev_max = data[i][j]
for j in range(N):
    prev_max = -1
    for i in reversed(range(N)):
        if data[i][j] > prev_max:
            s.add((i, j))
            prev_max = data[i][j]
for i in range(N):
    prev_max = -1
    for j in range(N):
        if data[i][j] > prev_max:
            s.add((i, j))
            prev_max = data[i][j]
for i in range(N):
    prev_max = -1
    for j in reversed(range(N)):
        if data[i][j] > prev_max:
            s.add((i, j))
            prev_max = data[i][j]
        
print(len(s))