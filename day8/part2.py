import sys
from functools import reduce
from itertools import takewhile

data = list(map(lambda x: list(map(lambda y: int(y), list(x))), sys.stdin.read().splitlines()))
N = len(data)

def north(i, j): return data[i][:j + 1][::-1]
def south(i, j): return data[i][j:]
def west(i, j): return [data[k][j] for k in reversed(range(i + 1))]
def east(i, j): return [data[k][j] for k in range(i, N)]

def score(i, j):
    scores = []
    for arr in [north(i, j), south(i, j), west(i, j), east(i, j)]:
        res = len(tuple(takewhile(lambda x: x < arr[0], arr[1:])))
        res += res < len(arr[1:])
        scores.append(res)
    return reduce(lambda x, y: x * y, scores)

print(max(score(i, j) for j in range(N) for i in range(N)))
