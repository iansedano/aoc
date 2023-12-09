import itertools
import math

from common import main

DAY = 8
YEAR = 2023
SAMPLE = """"""


def parse(puzzle_input):
    dirs, network = puzzle_input.split("\n\n")
    dirs = [0 if char == "L" else 1 for char in dirs]
    network = dict(parse_network_line(line) for line in network.splitlines())
    return dirs, network


def parse_network_line(line):
    src, dest = line.split(" = ")
    return src, tuple(dest.strip("()").split(", "))


def part1(parsed_input):
    dirs, network = parsed_input
    steps = 0
    location = "AAA"
    cycle = itertools.cycle(dirs)
    while location != "ZZZ":
        location = network[location][next(cycle)]
        steps += 1

    return steps


def part2(parsed_input):
    dirs, network = parsed_input
    locations = [k for k in network.keys() if k.endswith("A")]

    cycles = [find_cycle(location, dirs, network) for location in locations]
    return math.lcm(*cycles)


def find_cycle(location, dirs, network):
    """
    This won't work for many types of cycle. Just so happens to work on today's input.
    """
    dir_cycle = itertools.cycle(dirs)
    z_endings = []
    steps = 0
    while len(z_endings) < 3:
        location = network[location][next(dir_cycle)]
        steps += 1
        if location.endswith("Z"):
            z_endings.append(steps)
            steps = 0

    if any(ending != z_endings[0] for ending in z_endings):
        raise ValueError("no cycle found")

    return z_endings[0]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
