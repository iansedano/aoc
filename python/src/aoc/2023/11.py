import itertools

from common import main

DAY = 11
YEAR = 2023
SAMPLE = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def parse(puzzle_input):
    universe = [list(line) for line in puzzle_input.splitlines()]

    blank_y = [
        i
        for i, line in enumerate(universe)
        if all(char == "." for char in line)
    ]
    blank_x = [
        i
        for i, line in enumerate(transpose(universe))
        if all(char == "." for char in line)
    ]
    return universe, blank_x, blank_y


def transpose(array):
    return [list(x) for x in zip(*array)]


def part1(parsed_input):
    universe, blank_x, blank_y = parsed_input
    galaxies = get_galaxies(universe, blank_x, blank_y, expansion_factor=2)
    return sum(manhattan(*pair) for pair in itertools.combinations(galaxies, 2))


def part2(parsed_input):
    universe, blank_x, blank_y = parsed_input
    galaxies = get_galaxies(
        universe, blank_x, blank_y, expansion_factor=1_000_000
    )
    return sum(manhattan(*pair) for pair in itertools.combinations(galaxies, 2))


def get_galaxies(universe, blank_x, blank_y, expansion_factor):
    expansion_factor -= 1
    galaxies = set()
    y_offset = 0
    for y, line in enumerate(universe):
        if y in blank_y:
            y_offset += expansion_factor
        x_offset = 0
        for x, pos in enumerate(line):
            if x in blank_x:
                x_offset += expansion_factor
            if pos == "#":
                galaxies.add((x + x_offset, y + y_offset))

    return galaxies


def manhattan(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
