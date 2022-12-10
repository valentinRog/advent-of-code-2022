import sys

h = [0, 0]
t = [[0, 0] for _ in range(9)]
s = set()

actions = {
    "U": lambda : [h[0] + 1, h[1]],
    "D": lambda : [h[0] - 1, h[1]],
    "L": lambda : [h[0], h[1] - 1],
    "R": lambda : [h[0], h[1] + 1],
}

def follow(h, t):
    if abs(h[0] - t[0]) == 2 and abs(h[1] - t[1]) == 2:
        t[0] += (h[0] - t[0]) >> 1
        t[1] += (h[1] - t[1]) >> 1
    elif abs(h[0] - t[0]) == 2:
        t[0] += (h[0] - t[0]) >> 1
        if h[1] - t[1]:
            t[1] += h[1] - t[1]
    elif abs(h[1] - t[1]) == 2:
        t[1] += (h[1] - t[1]) >> 1
        if h[0] - t[0]:
            t[0] += h[0] - t[0]

for line in sys.stdin:
    for _ in range(int(line.split()[1])):
        h = actions[line.split()[0]]()
        for i, e in enumerate(t):
            follow(t[i - 1], e) if i else follow(h, e)
        s.add(tuple(t[-1]))
print(len(s))