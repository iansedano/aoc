import collections
from pprint import pp

from aocd import get_data
from rich.console import Console
from rich.live import Live

CONSOLE = Console()

SAMPLE = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def viz(cave, sand=None):

    min_x = min(key[0] for key in cave.keys() if key != "floor")
    min_y = 0
    max_x = max(key[0] for key in cave.keys() if key != "floor") + 1
    max_y = cave["floor"] + 1

    out = []

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            item = cave.get((x, y))
            if sand and sand == (x, y):
                out.append("[#C2B280]O[/]")
            elif y == max_y - 1:
                out.append("[#5A4D41 on #74663B]#[/]")
            else:
                out.append(
                    "[#C2B280]O[/]"
                    if item == 1
                    else "[#5A4D41 on #74663B]#[/]"
                    if item == -1
                    else " "
                )
        out.append("\n")

    return "".join(out)


def parse(puzzle_input):
    """Parse input."""

    lines = [
        [
            tuple(int(num) for num in point.split(","))
            for point in line.split(" -> ")
        ]
        for line in puzzle_input.splitlines()
    ]

    cave = {}

    for line in lines:
        for start, end in zip(line[1:], line[:-1]):
            cave[start] = -1  # -1 for rock, 1 for sand, unassigned for air
            cave[end] = -1
            sx, sy = start
            ex, ey = end
            dx, dy = ex - sx, ey - sy
            if dx != 0:
                for x in range(sign(dx), dx + sign(dx), sign(dx)):
                    cave[(sx + x, sy)] = -1
            if dy != 0:
                for y in range(sign(dy), dy + sign(dy), sign(dy)):
                    cave[(sx, sy + y)] = -1

    max_y = max(key[1] for key in cave)

    cave["floor"] = 2 + max_y

    return cave


def sim(cave, part1=True, live=None):
    while True:  # SAND PRODUCTION

        if live:
            live.update(viz(cave))

        sand_x, sand_y = (500, 0)

        # SAND FALLING
        while True:

            S = (sand_x, sand_y + 1)  # South
            SW = (sand_x - 1, sand_y + 1)  # South West
            SE = (sand_x + 1, sand_y + 1)  # South East

            if S[1] == cave["floor"]:
                if part1:
                    return cave
                cave[sand_x, sand_y] = 1
                break
            if cave.get(S) is None:
                sand_x, sand_y = S
            elif cave.get(SW) is None:
                sand_x, sand_y = SW
            elif cave.get(SE) is None:
                sand_x, sand_y = SE
            elif sand_y == 0:
                cave[sand_x, sand_y] = 1
                return cave
            else:
                cave[sand_x, sand_y] = 1
                break


def part1(data):
    cave = data
    return collections.Counter(sim(cave).values())[1]


def part2(data):
    """Solve part 2."""
    cave = data
    return collections.Counter(sim(cave, part1=False).values())[1]


def visualization(data):
    with Live(console=CONSOLE, refresh_per_second=4) as live:
        sim(data, part1=False, live=live)


def main():
    puzzle_input = get_data(day=14, year=2022).strip()
    # puzzle_input = SAMPLE

    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
