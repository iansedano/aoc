from itertools import product

from common import main

DAY = 21
YEAR = 2015
SAMPLE = """"""

# cost attack defense
WEAPONS = [
    ("weapon", "dagger", 8, 4, 0),
    ("weapon", "shortsword", 10, 5, 0),
    ("weapon", "warhammer", 25, 6, 0),
    ("weapon", "longsword", 40, 7, 0),
    ("weapon", "greataxe", 74, 8, 0),
]
ARMORS = [
    ("", "", 0, 0, 0),
    ("armor", "leather", 13, 0, 1),
    ("armor", "chainmail", 31, 0, 2),
    ("armor", "splintmail", 53, 0, 3),
    ("armor", "bandedmail", 75, 0, 4),
    ("armor", "platemail", 102, 0, 5),
]
RINGS = [
    ("", "", 0, 0, 0),
    ("ring", "damage +1", 25, 1, 0),
    ("ring", "damage +2", 50, 2, 0),
    ("ring", "damage +3", 100, 3, 0),
    ("ring", "defense +1", 20, 0, 1),
    ("ring", "defense +2", 40, 0, 2),
    ("ring", "defense +3", 80, 0, 3),
]


def parse(puzzle_input):
    player = {"damage": 0, "defense": 0, "hp": 100}

    boss_lines = [line.split(": ") for line in puzzle_input.splitlines()]
    boss = {
        "damage": int(boss_lines[1][1]),
        "defense": int(boss_lines[2][1]),
        "hp": int(boss_lines[0][1]),
    }

    return player, boss


def part1(parsed_input):
    player, boss = parsed_input
    sorted_kit_combos = sorted(get_kit_combos(), key=lambda k: k["cost"])

    for combo in sorted_kit_combos:
        player = player | combo
        _, boss_result = simulate_battle(player, boss)
        if boss_result["hp"] == 0:
            return combo["cost"]


def part2(parsed_input):
    player, boss = parsed_input
    sorted_kit_combos = sorted(get_kit_combos(), key=lambda k: k["cost"], reverse=True)

    for combo in sorted_kit_combos:
        player = player | combo
        player_result, _ = simulate_battle(player, boss)
        if player_result["hp"] == 0:
            return combo["cost"]


def get_kit_combos(weapons=WEAPONS, armors=ARMORS, rings=RINGS):
    kits = product(weapons, armors, rings, rings)

    return [get_kit_stats(kit) for kit in kits]


def get_kit_stats(items):
    stats = {"cost": 0, "damage": 0, "defense": 0}
    for item in items:
        stats = {
            "cost": stats["cost"] + item[2],
            "damage": stats["damage"] + item[3],
            "defense": stats["defense"] + item[4],
        }
    return stats


def simulate_battle(player_a, player_b):
    while True:
        player_b = hit(player_a, player_b)
        if player_b["hp"] == 0:
            return player_a, player_b
        player_a = hit(player_b, player_a)
        if player_a["hp"] == 0:
            return player_a, player_b


def hit(attacker, receiver):
    damage = max(attacker["damage"] - receiver["defense"], 1)
    return receiver | {"hp": max(receiver["hp"] - damage, 0)}


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
