import sys

h = t = [0, 0]
s = set()

actions = {
    "U": lambda : [h[0] + 1, h[1]],
    "D": lambda : [h[0] - 1, h[1]],
    "L": lambda : [h[0], h[1] - 1],
    "R": lambda : [h[0], h[1] + 1],
}

def follow():
    if abs(h[0] - t[0]) == 2:
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
        follow()
        s.add(tuple(t))
print(len(s))