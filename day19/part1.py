import sys
import functools

data = [
    {
        "ore": int(line.split()[6]),
        "clay": int(line.split()[12]),
        "obsidian": (int(line.split()[18]), int(line.split()[21])),
        "geode": (int(line.split()[27]), int(line.split()[30])),
    }
    for line in sys.stdin.read().strip().splitlines()
]


@functools.cache
def best(
        ore_ore,
        clay_ore,
        obsidian_ore,
        obsidian_clay,
        geode_ore,
        geode_obsidian,
        ore=0,
        clay=0,
        obsidian=0,
        geode=0,
        ore_rob=1,
        clay_rob=0,
        obsidian_rob=0,
        geode_rob=0,
        t=0):

    if t == 24:
        return geode
    arr = []

    if ore >= geode_ore and obsidian >= geode_obsidian:
        return best(
            ore_ore,
            clay_ore,
            obsidian_ore,
            obsidian_clay,
            geode_ore,
            geode_obsidian,
            ore + ore_rob - geode_ore,
            clay + clay_rob,
            obsidian + obsidian_rob - geode_obsidian,
            geode + geode_rob,
            ore_rob,
            clay_rob,
            obsidian_rob,
            geode_rob + 1,
            t + 1
        )

    if ore >= ore_ore:
        arr.append(
            best(
                ore_ore,
                clay_ore,
                obsidian_ore,
                obsidian_clay,
                geode_ore,
                geode_obsidian,
                ore + ore_rob - ore_ore,
                clay + clay_rob,
                obsidian + obsidian_rob,
                geode + geode_rob,
                ore_rob + 1,
                clay_rob,
                obsidian_rob,
                geode_rob,
                t + 1)
        )

    if ore >= clay_ore:
        arr.append(
            best(
                ore_ore,
                clay_ore,
                obsidian_ore,
                obsidian_clay,
                geode_ore,
                geode_obsidian,
                ore + ore_rob - clay_ore,
                clay + clay_rob,
                obsidian + obsidian_rob,
                geode + geode_rob,
                ore_rob,
                clay_rob + 1,
                obsidian_rob,
                geode_rob,
                t + 1)
        )

    if ore >= obsidian_ore and clay >= obsidian_clay:
        arr.append(
            best(
                ore_ore,
                clay_ore,
                obsidian_ore,
                obsidian_clay,
                geode_ore,
                geode_obsidian,
                ore + ore_rob - obsidian_ore,
                clay + clay_rob - obsidian_clay,
                obsidian + obsidian_rob,
                geode + geode_rob,
                ore_rob,
                clay_rob,
                obsidian_rob + 1,
                geode_rob,
                t + 1)
        )

    if ore < ore_ore:
        arr.append(
            best(
                ore_ore,
                clay_ore,
                obsidian_ore,
                obsidian_clay,
                geode_ore,
                geode_obsidian,
                ore + ore_rob,
                clay + clay_rob,
                obsidian + obsidian_rob,
                geode + geode_rob,
                ore_rob,
                clay_rob,
                obsidian_rob,
                geode_rob,
                t + 1
            )
        )
    return max(arr)


res = 0
for i, line in enumerate(data, 1):
    print(i)
    res += i * best(
        line["ore"],
        line["clay"],
        line["obsidian"][0],
        line["obsidian"][1],
        line["geode"][0],
        line["geode"][1],
    )
    best.cache_clear()
print(res)
