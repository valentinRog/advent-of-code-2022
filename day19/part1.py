import sys
from collections import deque


def parse_bp(s: str):
    dq = deque(map(int, filter(str.isnumeric, s.replace(".", "").split())))
    return [
        (dq.popleft(), 0, 0, 0),
        (dq.popleft(), 0, 0, 0),
        (dq.popleft(), dq.popleft(), 0, 0),
        (dq.popleft(), 0, dq.popleft(), 0),
    ]


data = [
    parse_bp(line)
    for line in sys.stdin.read().strip().splitlines()
]


def best(bp):

    T_MAX = 24
    cache = {}
    current_best = 0

    def compute(mats, robs, t):
        nonlocal current_best

        dt = T_MAX - t
        if mats[-1] + robs[-1] * dt + (dt - 1) * dt // 2 <= current_best:
            return 0

        if (mats, robs) in cache:
            n, tt = cache[(mats, robs)]
            if t >= tt:
                return 0
            cache[(mats, robs)] = (n, t)

        if t == T_MAX:
            current_best = max(current_best, mats[-1])
            return mats[-1]

        res = 0
        for i, rob_cost in enumerate(bp):
            if any(map(lambda i: mats[i] < rob_cost[i], range(len(mats)))):
                continue
            new_mats = tuple(
                v + robs[ii] - rob_cost[ii]
                for ii, v in enumerate(mats)
            )
            new_robs = (*robs[:i], robs[i] + 1, *robs[i+1:])
            res = max(res, compute(new_mats, new_robs, t + 1))

        new_mats = tuple(
            v + robs[i]
            for i, v in enumerate(mats)
        )
        res = max(res, compute(new_mats, robs, t + 1))
        cache[(mats, robs)] = (res, t)
        return res

    return compute(tuple([0] * 4), (1, 0, 0, 0), 0)


print(sum((i + 1) * best(bp) for i, bp in enumerate(data)))
