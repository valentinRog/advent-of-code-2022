import sys
from functools import reduce

monkeys = []

def get_op(line):
    operation = line.split(":")[1].split()
    if operation[-1] == "old":
        return lambda x: x**2
    elif operation[-2] == "+":
        return lambda x: x + int(operation[-1])
    return lambda x: x * int(operation[-1])

for monkey in sys.stdin.read().split("\n\n"):
    arr = monkey.splitlines()
    monkey = {
        "items": list(map(lambda x: int(x.strip()), arr[1].split(":")[1].split(","))),
        "operation": get_op(arr[2]),
        "test": int(arr[3].split()[-1]),
        "true": int(arr[4].split()[-1]),
        "false": int(arr[5].split()[-1]),
        "inspections": 0,
    }
    monkeys.append(monkey)

for _ in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            worry = monkey["operation"](item) // 3
            if not worry % monkey["test"]:
                monkeys[monkey["true"]]["items"].append(worry)
            else:
                monkeys[monkey["false"]]["items"].append(worry)
            monkey["inspections"] += 1
        monkey["items"] = []

print(reduce(lambda x, y: x * y, sorted([monkey["inspections"] for monkey in monkeys])[-2:]))