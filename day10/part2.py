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

for i, x in enumerate(v):
    if abs(x - (i % 40)) < 2:
        print("#", end="")
    else:
        print(".", end="")
    if not (i + 1) % 40:
        print()
