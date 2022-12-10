import sys

x = 1
v = []
for line in sys.stdin.read().splitlines():
    v += [x] if line == "noop" else [x, x]
    if line.startswith("add"):
        x += int(line.split()[1]) 
print(sum(v[i - 1] * i for i in range(20, 220 + 1, 40)))
