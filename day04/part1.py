import sys

data = [map(lambda x: list(map(int, x.split("-"))), line.split(",")) for line in sys.stdin]

def issubarray(x, y):
    return (x[0] >= y [0] and x[1] <= y[1]) or (y[0] >= x [0] and y[1] <= x[1])

print(sum(int(issubarray(x, y)) for x, y in data))
