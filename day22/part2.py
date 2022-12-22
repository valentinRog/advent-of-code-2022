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
    1: (complex(2 * TILE, 0), complex(3 * TILE - 1, TILE - 1)),
    2: (complex(0, TILE - 1), complex(TILE - 1, 2 * TILE - 1)),
    3: (complex(TILE, TILE), complex(2 * TILE - 1, 2 * TILE - 1)),
    4: (complex(2 * TILE, TILE), complex(3 * TILE - 1, 2 * TILE - 1)),
    5: (complex(2 * TILE, 2 * TILE), complex(3 * TILE - 1, 3 * TILE - 1)),
    6: (complex(3 * TILE, 2 * TILE), complex(4 * TILE - 1, 3 * TILE - 1)),
}


def face(p):
    return next(
        k for k, v in fcs.items()
        if v[0].real <= p.real <= v[1].real and v[0].imag <= p.imag <= v[1].imag
    )


for y in range(1 + max(map(lambda z: int(z.imag), s))):
    for x in range(1 + max(map(lambda z: int(z.real), s))):
        if complex(x, y) in s:
            print(face(complex(x, y)), end="")
        else:
            print(" ", end="")
    print()

exit()

conversions = {
    (1, 2): lambda p: (complex(TILE - 1 - int(p.real) % TILE, TILE - 1), 1j),
}


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
