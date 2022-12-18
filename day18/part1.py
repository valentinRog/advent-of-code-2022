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

def touching_faces(p):
    faces = 6
    for side in sides:
        for x in data:
            if p == addt(x, side):
                faces -= 1
                break
    return faces

print(sum(touching_faces(p) for p in data))
