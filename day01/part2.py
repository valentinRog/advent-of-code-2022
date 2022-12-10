import sys

data = [[int(x) for x in i.split("\n")] for i in sys.stdin.read().strip().split("\n\n")]
print(sum(sorted(map(sum, data))[-3:]))