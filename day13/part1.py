import sys

data = [list(map(eval, line.split("\n"))) for line in sys.stdin.read().strip().split("\n\n")]

def cmp(a, b):
    if not isinstance(a, list) and not isinstance(b, list):
        return a - b
    if isinstance(a, list) and not isinstance(b, list):
        b = [b]
    elif isinstance(b, list) and not isinstance(a, list):
        a = [a]
    for e1, e2 in zip(a, b):
        if cmp(e1, e2):
            return cmp(e1, e2)
    return len(a) - len(b)

res = []
for i, group in enumerate(data):
    if cmp(*group) <= 0:
        res.append(i + 1)
print(sum(res))