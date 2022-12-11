import sys
from math import prod


def get_op(line):
    o, v = line.split(":")[1].split()[-2:]
    return {
        "+": lambda x: x + int(v),
        "*": lambda x: x * int(v),
    }[o] if v != "old" else lambda x: x ** 2

monkeys = [
    {
        "items": list(map(lambda x: int(x.strip()), monkey[1].split(":")[1].split(","))),
        "operation": get_op(monkey[2]),
        "test": int(monkey[3].split()[-1]),
        "true": int(monkey[4].split()[-1]),
        "false": int(monkey[5].split()[-1]),
        "inspections": 0,
    }
    for monkey in map(str.splitlines, sys.stdin.read().split("\n\n"))
]

for _ in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            worry = monkey["operation"](item) // 3
            if not worry % monkey["test"]:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
        monkey["inspections"] += len(monkey["items"])
        monkey["items"] = []

print(prod(sorted([monkey["inspections"] for monkey in monkeys])[-2:]))
