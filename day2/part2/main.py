import sys

table = {
    "A": 1,
    "B": 2,
    "C": 3,
}

score = {
    "X": lambda x: table[x] - 1 + 3 * int(table[x] == 1),
    "Y": lambda x: 3 + table[x],
    "Z": lambda x: 6 + table[x] % 3 + 1,
}

print(sum([score[i[1]](i[0]) for i in [line.split() for line in sys.stdin]]))
 