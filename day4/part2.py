import sys

data = [map(lambda x: list(map(lambda y: int(y), x.split("-"))), line.split(",")) for line in sys.stdin]
print(sum(int(x[0] <= y[1] and x[1] >= y[0]) for x, y in data))
