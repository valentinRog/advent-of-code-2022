import sys

data = [
    list(map(eval, line.split("\n")))
    for line in sys.stdin.read().strip().split("\n\n")
]

def cmp(a, b):
    if int == type(a) == type(b):
      return a - b
    a, b = map(lambda x: [x] if type(x) == int else x, (a, b))
    return next((c for e in zip(a, b) if (c := cmp(*e))), len(a) - len(b))

print(sum([i + 1 for i, e in enumerate(data) if cmp(*e) <= 0]))
