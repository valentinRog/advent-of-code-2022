import sys

data = [[int(x) for x in filter(None, i.split("\n"))] for i in sys.stdin.read().split("\n\n")]
print(sum(sorted(map(lambda x: sum(x), data))[-3:]))