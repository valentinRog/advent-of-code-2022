import sys

data = {
    (e := line.strip().split(":"))[0]: e[1]
    for line in sys.stdin.read().strip().splitlines()
}

def compute(k):
    if len((op := data[k].split())) == 3:
        for i in (0, 2):
            if op[i] in data.keys():
                op[i] = str(compute(op[i]))
    return int(eval(" ".join(op)))

print(compute("root"))
        