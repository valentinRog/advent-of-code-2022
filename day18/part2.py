import sys

data = [
    tuple(map(int, line.split(",")))
    for line in sys.stdin.read().strip().splitlines()
]

sides = {
    (-1, 0 ,0),
    (1, 0 ,0),
    (0, -1 ,0),
    (0, 1 ,0),
    (0, 0 , -1),
    (0, 0 ,1),
}

def addt(t1, t2):
    return tuple(sum(e) for e in zip(t1, t2))

def connected(p1, p2):
    for side in sides:
        for p in p1:
            if addt(p, side) in p2:
                return True
    return False

air_blocks = set()
def touching_faces(p):
    faces = 6
    for side in sides:
        for x in data:
            if addt(p, side) == x:
                faces -= 1
                break
        else:
            air_blocks.add(addt(p, side))
    return faces

r1 = sum(touching_faces(p) for p in data)

def create_block(p, blocks):
    s = {p}
    prev = -1
    while prev != len(blocks):
        prev = len(blocks)
        for b in blocks:
            if connected(s, {b}):
                s.add(b)
                blocks.remove(b)
    return s

def expand_air(ab):
    res = set()
    for b in ab:
        res.add(b)
        for side in sides:
            if addt(b, side) not in data:
                res.add(addt(b, side))
    return res

air_blocks = expand_air(air_blocks)

arr = []
done = set()
for i, p in enumerate(air_blocks):
    if p not in done:
        arr.append(create_block(p, list(air_blocks)))
    done |= arr[-1]

ext_len = max(len(x) for x in arr)
yo = set()
for s in arr:
    if len(s) < ext_len:
        yo |= s

res = 0
for p in yo:
    for side in sides:
        if addt(p, side) in data:
            res += 1
print(r1 - res)
