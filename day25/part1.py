import sys

v = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

def compute(s):
    res = 0
    for i, c in enumerate(reversed(s)):
        res += v[c] * 5 ** i
    return res

def compute_reverse(n):
    res = ""
    while n:
        if n % 5 <= 2:
            res = str(n % 5) + res
            n //= 5
        else:
            res = "-="[5 - n % 5 - 1] + res
            n //= 5
            n += 1
    return res

res = 0
for line in sys.stdin.read().strip().splitlines():
  res += compute(line)
print(compute_reverse(res))

