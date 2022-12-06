import sys

i = N = 14
data = sys.stdin.read().strip()
while len(set(data[i - N:i])) != N:
    i += 1
print(i)
