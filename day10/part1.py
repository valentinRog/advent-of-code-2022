import sys

x = 1
v = []
for line in sys.stdin.read().splitlines():
    if line == "noop":
        v.append(x)
    else:
        v.append(x)
        v.append(x)
        x += int(line.split()[1])

print(sum(v[i - 1] * i for i in range(20, 220 + 1, 40)))
