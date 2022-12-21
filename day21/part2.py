import sys
import math

data = {
    (e := line.strip().split(":"))[0]: e[1]
    for line in sys.stdin.read().strip().splitlines()
}


def compute(k):
    if k == "humn":
        return 1j
    if len((op := data[k].split())) == 3:
        for i in (0, 2):
            if op[i] in data.keys():
                op[i] = str(compute(op[i]))
    return eval(" ".join(op))

x1, _,  x2 = data["root"].split()
z = compute(x1) - compute(x2)
print(math.floor(abs(z.real / z.imag)))
