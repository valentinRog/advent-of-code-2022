import sys

table = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def score(x1, x2):
    n = table[x2]
    if table[x1] % 3 + 1 == table[x2]:
        n += 6
    elif table[x1] == table[x2]:
        n += 3
    return n

print(sum([score(*line.split()) for line in sys.stdin]))
