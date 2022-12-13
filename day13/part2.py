import sys
from functools import cmp_to_key

data = list(map(eval, sys.stdin.read().strip().replace("\n\n", "\n").splitlines()))

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

data += [[[2]], [[6]]]
data = sorted(data, key=cmp_to_key(cmp))
print((data.index([[2]]) + 1) * (data.index([[6]]) + 1))
