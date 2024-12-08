import itertools
from collections import defaultdict
from textwrap import dedent

from aocd import get_data

DAY = 1
YEAR = 2024
SAMPLE = dedent(
    """\
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """
)


def parse(puzzle_input):
    antennas = defaultdict(set)
    lines = puzzle_input.splitlines()
    height, width = len(lines), len(lines[0])

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                antennas[char].add((x, y))

    return antennas, (width, height)


def part_1(parsed_input):
    antennas, (width, height) = parsed_input

    antinodes = set()

    for _, nodes in antennas.items():
        for n1, n2 in itertools.combinations(nodes, 2):
            for n in [get_antinode(n1, n2), get_antinode(n2, n1)]:
                if 0 <= n[0] < width and 0 <= n[1] < height:
                    antinodes.add(n)

    return len(antinodes)


def part_2(parsed_input):
    antennas, (width, height) = parsed_input

    antinodes = set()

    for _, nodes in antennas.items():
        for n1, n2 in itertools.combinations(nodes, 2):
            antinodes = (
                antinodes
                | get_resonant_antinodes(n1, n2, (width, height))
                | get_resonant_antinodes(n2, n1, (width, height))
            )

    return len(antinodes)


def get_antinode(a, b):
    return (a[0] - (b[0] - a[0]), a[1] - (b[1] - a[1]))


def get_resonant_antinodes(a, b, limit):
    antinodes = set([a, b])

    dx, dy = b[0] - a[0], b[1] - a[1]
    current = a

    while True:
        next_antinode = current[0] - dx, current[1] - dy
        if not (
            0 <= next_antinode[0] < limit[0]
            and 0 <= next_antinode[1] < limit[1]
        ):
            break
        antinodes.add(next_antinode)
        current = next_antinode

    return antinodes


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
