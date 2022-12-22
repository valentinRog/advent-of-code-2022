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
p = next(complex(line.index("#"), i) for i, line in enumerate(m.splitlines()))

dir = (1, -1j, -1, 1j)
def rl(): return dir[(dir.index(d) + 1) % len(dir)]
def rr(): return dir[dir.index(d) - 1]


def move():
    if p + d in rock:
        return p
    if p + d in s:
        return p + d
    return np if (np := {
        1: min((e for e in s if e.imag == p.imag), key=lambda x: x.real),
        -1: max((e for e in s if e.imag == p.imag), key=lambda x: x.real),
        1j: min((e for e in s if e.real == p.real), key=lambda x: x.imag),
        -1j: max((e for e in s if e.real == p.real), key=lambda x: x.imag),
    }[d]) not in rock else p


acc = ""
for c in path:
    if not c.isdigit():
        for _ in range(int(acc)):
            p = move()
    if c == "R":
        acc = ""
        d = rr()
    elif c == "L":
        acc = ""
        d = rl()
    else:
        acc += c
for _ in range(int(acc)):
    p = move()

p += 1 + 1j
if d.imag:
    d = -d
print(1000 * int(p.imag) + 4 * int(p.real) + dir.index(d))
