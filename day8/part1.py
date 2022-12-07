import sys

data = sys.stdin.read().splitlines()

def dirsize(i):
    level = 0
    n = 0
    while level >= 0 and i < len(data):
        if data[i].startswith("$ cd"):
            level += -1 if data[i].strip().endswith("..") else 1
        elif not data[i].startswith("$") and not data[i].startswith("dir"):
            n += int(data[i].split()[0])
        i += 1
    return n

dir = [dirsize(i + 1) for i, line in enumerate(data) if line.startswith("$ cd") and not line.endswith("..")]
print(sum(filter(lambda x: x <= 100000, dir)))
