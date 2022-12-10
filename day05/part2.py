import sys

data = sys.stdin.read().split("\n\n")
game = [[] for _ in range(int(data[0].strip()[-1]))]
for line in data[0].splitlines()[:-1]:
    for i, c in enumerate(line):
        if not ((i - 1) % 4) and c != " ":
            game[i // 4] = [c] + game[i // 4]
for line in data[1].splitlines():
    _, x, _, y, _, z = line.split()
    x, y, z = map(int, [x, y, z])
    game[z - 1] += game[y - 1][-x:]
    game[y - 1] = game[y - 1][:-x]
print("".join(e[-1] for e in game))
