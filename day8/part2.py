import sys
from functools import reduce

data = list(map(lambda x: list(map(lambda y: int(y), list(x))), sys.stdin.read().splitlines()))
N = len(data)

def score(i, j):
    arr = [data[i][:j + 1][::-1], data[i][j:], [data[k][j] for k in reversed(range(i + 1))], [data[k][j] for k in range(i, N)]]
    scores = []
    for arr in arr:
        res = 0
        for x in arr[1:]:
            res += 1
            if x >= arr[0]: break
        scores.append(res)
    return reduce(lambda x, y: x * y, scores)

print(max(score(i, j) for j in range(N) for i in range(N)))
