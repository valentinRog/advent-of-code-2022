import sys

data = {
    tuple(map(int, line.split(",")))
    for line in sys.stdin.read().strip().splitlines()
}

sides = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)


def add(*t): return tuple(sum(e) for e in zip(*t))
def faces(p): return sum(add(p, side) not in data for side in sides)


print(sum(faces(p) for p in data))
