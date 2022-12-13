import sys

data = [
    list(map(eval, line.split("\n")))
    for line in sys.stdin.read().strip().split("\n\n")
]

def cmp(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        return a - b
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for e1, e2 in zip(a, b):
        if cmp(e1, e2):
            return cmp(e1, e2)
    return len(a) - len(b)

print(sum([i + 1 for i, e in enumerate(data) if cmp(*e) <= 0]))
