import sys

data = sys.stdin.read().split("\n\n")
m = data[0]
path = data[1]


s = set()
rock = set()
for y, line in enumerate(m.splitlines()):
    for x, e in enumerate(line):
        if e != " ":
            s.add(complex(x, y))
        if e == "#":
            rock.add(complex(x, y))

d = 1
p = next(complex(line.index("."), i) for i, line in enumerate(m.splitlines()))

dir = (1, -1j, -1, 1j)
def rl(): return dir[(dir.index(d) + 1) % len(dir)]
def rr(): return dir[dir.index(d) - 1]


# hardcoding for the win, don't do this at home

# TILE = 4
TILE = 50

# fcs = {
#     1: complex(2 * TILE, 0),
#     2: complex(0, TILE),
#     3: complex(TILE, TILE),
#     4: complex(2 * TILE, TILE),
#     5: complex(2 * TILE, 2 * TILE),
#     6: complex(3 * TILE, 2 * TILE),
# }
fcs = {
    1: complex(TILE, 0),
    2: complex(2 * TILE, 0),
    3: complex(TILE, TILE),
    4: complex(0, 2 * TILE),
    5: complex(TILE, 2 * TILE),
    6: complex(0, 3 * TILE),
}


def face(p):
    return next(
        k for k, v in fcs.items()
        if v.real <= p.real < v.real + TILE and v.imag <= p.imag < v.imag + TILE
    )

# def getff(fi, d):
#     return {
#         (1, -1): 3,
#         (1, -1j): 2,
#         (1, 1): 6,
#         (2, -1): 6,
#         (2, -1j): 1,
#         (2, 1j): 5,
#         (3, -1j): 1,
#         (3, 1j): 5,
#         (4, 1): 6,
#         (5, -1): 3,
#         (5, 1j): 2,
#         (6, 1j): 2,
#         (6, -1j): 4,
#         (6, 1): 1,
#     }[(fi, d)]


def getff(fi, d):
    return {
        (1, -1): 4,
        (1, -1j): 6,
        (2, -1j): 6,
        (2, 1): 5,
        (2, 1j): 3,
        (3, -1): 4,
        (3, 1): 2,
        (4, -1): 1,
        (4, -1j): 3,
        (5, 1): 2,
        (5, 1j): 6,
        (6, -1): 1,
        (6, 1j): 2,
        (6, 1): 5,
    }[(fi, d)]


# def transform(p, fi, ff):
#     x, y = int(p.real) % TILE, int(p.imag) % TILE
#     return {
#         (1, 2): (complex(TILE - 1 - x, 0) + fcs[2], 1j),
#         (1, 3): (complex(TILE - 1 - y, 0) + fcs[3], 1j),
#         (1, 6): (complex(TILE - 1, TILE - 1 - y) + fcs[6], -1),
#         (2, 1): (complex(TILE - 1 - x, 0) + fcs[1], 1j),
#         (2, 5): (complex(TILE - 1 - x, TILE - 1) + fcs[5], -1j),
#         (2, 6): (complex(TILE - 1 - y, TILE - 1), -1j),
#         (3, 1): (complex(0, x) + fcs[1], 1),
#         (3, 5): (complex(0, TILE - 1 - x) + fcs[5], 1),
#         (4, 6): (complex(TILE - 1 - y, 0) + fcs[6], 1j),
#         (5, 2): (complex(TILE - 1 - x, TILE - 1) + fcs[2], -1j),
#         (5, 3): (complex(TILE - 1 - y, TILE - 1) + fcs[3], -1j),
#         (6, 1): (complex(TILE - 1, TILE - 1 - y) + fcs[1], -1),
#         (6, 2): (complex(0, TILE - 1 - x) + fcs[2], 1),
#         (6, 4): (complex(TILE - 1, TILE - 1 - x) + fcs[4], -1),
#     }[(fi, ff)]

def transform(p, fi, ff):
    x, y = int(p.real) % TILE, int(p.imag) % TILE
    return {
        (1, 4): (complex(0, TILE - 1 - y) + fcs[4], 1),
        (1, 6): (complex(0, x) + fcs[6], 1),
        (2, 3): (complex(TILE - 1, x) + fcs[3], -1),
        (2, 5): (complex(TILE - 1, TILE - 1 - y) + fcs[5], -1),
        (2, 6): (complex(x, TILE - 1) + fcs[6], -1j),
        (3, 2): (complex(y, TILE - 1) + fcs[2], -1j),
        (3, 4): (complex(y, 0) + fcs[4], 1j),
        (4, 1): (complex(0, TILE - 1 - y) + fcs[1], 1),
        (4, 3): (complex(0, x) + fcs[3], 1),
        (5, 2): (complex(TILE - 1, TILE - 1 - y) + fcs[2], -1),
        (5, 6): (complex(TILE - 1, x) + fcs[6], -1),
        (6, 1): (complex(y, 0) + fcs[1], 1j),
        (6, 2): (complex(x, 0) + fcs[2], 1j),
        (6, 5): (complex(y, TILE - 1) + fcs[5], -1j),

    }[(fi, ff)]


def move(p, d):
    if p + d in rock:
        return p, d
    if p + d in s:
        return p + d, d

    p2, d2 = transform(p, face(p), getff(face(p), d))
    if p2 not in rock:
        return p2, d2
    return p, d


acc = ""
for c in path:
    if not c.isdigit():
        for _ in range(int(acc)):
            p, d = move(p, d)
    if c == "R":
        acc = ""
        d = rr()
    elif c == "L":
        acc = ""
        d = rl()
    else:
        acc += c

for _ in range(int(acc)):
    p, d = move(p, d)

p += 1 + 1j
if d.imag:
    d = -d
print(1000 * int(p.imag) + 4 * int(p.real) + dir.index(d))
