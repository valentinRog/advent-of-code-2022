import sys
from functools import cmp_to_key

data = list(map(eval, sys.stdin.read().strip().replace("\n\n", "\n").splitlines()))

def cmp(a, b):
    if int == type(a) == type(b):
      return a - b
    a, b = map(lambda x: [x] if type(x) == int else x, (a, b))
    return next((c for e in zip(a, b) if (c := cmp(*e))), len(a) - len(b))

data = sorted(data + [[[2]], [[6]]], key=cmp_to_key(cmp))
print((data.index([[2]]) + 1) * (data.index([[6]]) + 1))
