import sys
import math

data = {
    (e := line.strip().split(":"))[0]: e[1]
    for line in sys.stdin.read().strip().splitlines()
}


def compute(k):
    if k == "humn":
        return str(0 + 1j)
    if len((op := data[k].split())) == 3:
        for i in (0, 2):
            if op[i] in data.keys():
                op[i] = str(compute(op[i]))
    return f"({' '.join(op)})"

x1, _,  x2 = data["root"].split()
z = eval(compute(x1)) - eval(compute(x2))
print(math.floor(abs(z / z.imag)))
