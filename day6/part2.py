import sys

N = 14
data = sys.stdin.read().strip()
print(next(i + N for i in range(len(data) - N) if len(set(data[i:i + N])) == N))
