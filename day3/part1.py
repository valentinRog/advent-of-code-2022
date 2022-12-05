import sys
from string import ascii_lowercase, ascii_uppercase 

table = {v: i + 1 for i, v in enumerate(ascii_lowercase + ascii_uppercase)}
data = [[set(line[len(line) // 2:]), set(line[:len(line) // 2]) ] for line in sys.stdin]
print(sum([table[tuple(s1.intersection(s2))[0]] for s1, s2 in data]))
