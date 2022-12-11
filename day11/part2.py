import sys
from math import prod


def op(line):
    return lambda x: eval(" ".join(line.split()[-3:]).replace("old", str(x)))

monkeys = [
    {
        "items": list(map(lambda x: int(x.strip()), monkey[1].split(":")[1].split(","))),
        "operation": op(monkey[2]),
        "test": int(monkey[3].split()[-1]),
        "true": int(monkey[4].split()[-1]),
        "false": int(monkey[5].split()[-1]),
        "inspections": 0,
    }
    for monkey in map(str.splitlines, sys.stdin.read().split("\n\n"))
]

cm = prod([monkey["test"] for monkey in monkeys])
for _ in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            worry = monkey["operation"](item) % cm
            if not worry % monkey["test"]:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
        monkey["inspections"] += len(monkey["items"])
        monkey["items"] = []

print(prod(sorted([monkey["inspections"] for monkey in monkeys])[-2:]))
