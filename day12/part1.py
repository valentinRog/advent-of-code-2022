import sys
from string import ascii_lowercase

m = sys.stdin.read().strip()
W = m.index("\n")
H = len(m.splitlines())
m = "".join(m.splitlines()) 
S = m.index("S")
E = m.index("E")
m = m.replace("E", "z")
m = m.replace("S", "a")

arr = []
def backtracking(p=S, s=None, n=0):
    if s is None:
        s = set()
    s.add(p)
    n += 1
    if len(arr) and n > max(arr):
        return False
    if p == E:
        arr.append(n)
        return False
    if p // W > 0 and ascii_lowercase.index(m[p]) + 1 >= ascii_lowercase.index(m[p - W]) and p - W not in s and backtracking(p - W, set(s), n):
        return True
    if p // W < H - 1 and ascii_lowercase.index(m[p]) + 1 >= ascii_lowercase.index(m[p + W]) and p + W not in s and backtracking(p + W, set(s), n):
        return True
    if p % W and ascii_lowercase.index(m[p]) + 1 >= ascii_lowercase.index(m[p - 1]) and p - 1 not in s and backtracking(p - 1, set(s), n):
        return True
        if len(arr) and n > max(arr):
            return False
    if p % W != W - 1 and ascii_lowercase.index(m[p]) + 1 >= ascii_lowercase.index(m[p + 1]) and p + 1 not in s and backtracking(p + 1, set(s), n):
        return True
    return False 


backtracking()
print(min(arr) - 1 if len(arr) else "non")