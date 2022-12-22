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


#         1111
#         1111
#         1111
#         1111
# 222233334444
# 222233334444
# 222233334444
# 222233334444
#         55556666
#         55556666
#         55556666
#         55556666

# hardcoding for the win, don't do this at home

TILE = 4

fcs = {
    1: complex(2 * TILE, 0),
    2: complex(0, TILE - 1),
    3: complex(TILE, TILE),
    4: complex(2 * TILE, TILE),
    5: complex(2 * TILE, 2 * TILE),
    6: complex(3 * TILE, 2 * TILE),
}


def face(p):
    return next(
        k for k, v in fcs.items()
        if v.real <= p.real < v.real + TILE and v.imag <= p.imag < v.imag + TILE
    )


def transform(p, fi, ff):
    x, y = int(p.real) % TILE, int(p.imag) % TILE
    return {
        (1, 2): (complex(TILE - 1 - x, 0) + fcs[2], 1j),
        (1, 3): (complex(TILE - 1 - y, 0) + fcs[3], 1j),
        (1, 6): (complex(TILE - 1, TILE - 1 - y) + fcs[6], -1),
        (2, 1): (complex(TILE - 1 - x, 0) + fcs[1], 1j),
        (2, 5): (complex(TILE - 1 - x, TILE - 1) + fcs[5], -1j),
        (2, 6): (complex(TILE - 1 - y, TILE - 1), -1j),
        (3, 1): (complex(0, x) + fcs[1], 1),
        (3, 5): (complex(0, TILE - 1 - x) + fcs[5], 1),
        (4, 6): (complex(TILE - 1 - y, 0) + fcs[6], 1j),
        (5, 2): (complex(TILE - 1 - x, TILE - 1) + fcs[2], -1j),
        (5, 3): (complex(TILE - 1 - y, TILE - 1) + fcs[3], -1j),
        (6, 1): (complex(TILE - 1, TILE - 1 - y) + fcs[1], -1),
        (6, 2): (complex(0, TILE - 1 - x) + fcs[2], 1),
        (6, 4): (complex(TILE - 1, TILE - 1 - x) + fcs[4], -1),
    }[(fi, ff)]


def printm():
    for y in range(1 + max(map(lambda z: int(z.imag), s))):
        for x in range(1 + max(map(lambda z: int(z.real), s))):
            if complex(x, y) in s:
                if complex(x, y) == p:
                    print("p", end="")
                else:
                    print(face(complex(x, y)), end="")
            else:
                print(" ", end="")
        print()
    print()


printm()
p += d
p += d
p += d
p, d = transform(p, 1, 6)

printm()

# for _ in range(7):
#     p += d

# p = transform(p, 5, 3, d, -1j)
# d = -1j
# for _ in range(3):
#     p += d

# p = transform(p, 3, 1, d, 1)
# d = 1

exit()
#######################################

def move(p, d):
    if p + d in rock:
        return p, d
    if p + d in s:
        return p + d, d

    x, y = int(p.real), int(p.imag)

    if face(p) == 1:
        if d == 1:
            p2 = p + complex(TILE, )
            d2 = -1
            pass
        if d == -1j:
            p2 = p + complex(-2 * TILE, TILE)
            d2 = 1j
            return (p2, d2) if p2 not in rock else (p, d)
        if d == -1:
            pass
    if face(p) == 2:
        pass
    if face(p) == 3:
        pass
    if face(p) == 4:
        pass
    if face(p) == 5:
        pass
    if face(p) == 6:
        pass
    return p, d


print(p)
print()
acc = ""
for c in path:
    if not c.isdigit():
        for _ in range(int(acc)):
            p, d = move(p, d)
            print(p)
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
print(1000 * int(p.imag) + 4 * int(p.real) + dir.index(d))
