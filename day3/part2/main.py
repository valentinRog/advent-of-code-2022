import sys
from string import ascii_lowercase, ascii_uppercase
from functools import reduce

table = {v: i + 1 for i, v in enumerate(ascii_lowercase + ascii_uppercase)}
data = sys.stdin.read().splitlines()
data = [list(map(lambda x: set(x), data[i:i + 3])) for i in range(0, len(data), 3)]
print(sum([table[tuple(reduce(lambda x, y: x.intersection(y), i))[0]] for i in data]))
