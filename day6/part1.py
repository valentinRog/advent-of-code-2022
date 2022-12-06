import sys

i = N = 4
data = sys.stdin.read().strip()
while len(set(data[i - N:i])) != N:
    i += 1
print(i)
