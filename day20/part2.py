import sys
from collections import deque

data = list(map(lambda x: int(x) * 811589153 , sys.stdin.read().split()))

arr = deque(e for e in enumerate(data))

def r():
    global arr
    e = arr[0]
    arr.popleft()
    arr.append(e)

def align(e):
    while arr[0] != e:
        r()

for _ in range(10):
    for e in enumerate(data):
        i1 = arr.index(e)
        a = e[1]
        align(e)
        arr.popleft()
        if a < 0:
            a += (-a // len(arr)) * len(arr)
        a %= len(arr)
        for _ in range(a):
            r()
        arr.appendleft(e)

res = 0
for n in (1000, 2000, 3000):
    while arr[0][1]:
        r()
    for _ in range(n):
        r()
    res += arr[0][1]
print(res)
