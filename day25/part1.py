import sys

v = {
    "=": -2,
    "-": -1,
    "0": 0,
    "1": 1,
    "2": 2,
}

def from_snafu(s):
    return sum(v[c] * 5 ** i for i, c in enumerate(reversed(s)))

def to_snafu(n, s=""):
    n, m = divmod(n, 5)
    return to_snafu(n + (m > 2), "012=-"[m] + s) if n or m else s

print(to_snafu(sum(from_snafu(line) for line in sys.stdin.read().strip().splitlines())))
