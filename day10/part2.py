import sys

x = 1
v = []
for line in sys.stdin.read().splitlines():
    v += [x] if line == "noop" else [x, x]
    if line.startswith("add"):
        x += int(line.split()[1]) 
W = 40
crt = ["#" if abs(x - i % W) <= 1 else "." for i, x in enumerate(v)]
print("\n".join(map("".join, [crt[i:i + W] for i in range(0, len(crt), W)])))
