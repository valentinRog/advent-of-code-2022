import sys
from operator import itemgetter

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


def connected_air_blocks(p):
    return {a for side in sides if (a := add(p, side)) not in data}


def expand(p): return {p} | {add(p, side) for side in sides}


def create_block(p, blocks, block=None):
    if block is None:
        block = [{p}, expand(p)]
    try:
        for b in (b for b in blocks if b in block[1]):
            block[0].add(b)
            block[1] |= expand(b)
        return create_block(p, blocks - block[0], block)
    except:
        return block[0]


def create_blocks(blocks):
    while blocks:
        blocks -= (block := create_block(next(iter(blocks)), blocks))
        yield block


air_blocks = set().union(*(connected_air_blocks(p) for p in data))
air_blocks |= {
    np
    for side in sides for p in air_blocks if (np := add(p, side)) not in data
}

y_max = max(air_blocks, key=itemgetter(1))
trapped_air_blocks = set().union(
    *(filter(lambda b: y_max not in b, create_blocks(air_blocks)))
)

print(
    sum(faces(p) for p in data)
    - sum(add(p, side) in data for p in trapped_air_blocks for side in sides)
)
