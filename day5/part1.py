import sys

data = sys.stdin.read().split("\n\n")

game = [[] for _ in range(9)]
for line in data[0].splitlines()[:-1]:
    for i, c in enumerate(line):
        if not ((i - 1) % 4) and c != " ":
            game[i // 4] = [c] + game[i // 4]

for line in data[1].splitlines():
    _, x, _, y, _, z = line.split();
    for _ in range(int(x)):
        game[int(z) - 1].append(game[int(y) - 1].pop())

for x in game:
    if x:
        print(x[-1], end="")
print()