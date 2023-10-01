from common import main
from collections import defaultdict

DAY = 6
YEAR = 2015
SAMPLE = ""

instructions = {
    "turn off": lambda _: 0,
    "turn on": lambda _: 1,
    "toggle": lambda x: 1 if x == 0 else 0,
}

instructions = {
    "turn off": "OFF",
    "turn on": "ON",
    "toggle": "TOGGLE",
}


def parse(puzzle_input):
    return [parse_line(line) for line in puzzle_input.split("\n")]


def parse_line(line):
    inst_from, to_coord = line.split("through")
    inst_from = inst_from.split()
    from_coord = inst_from[-1]
    instruction = " ".join(inst_from[:2]) if len(inst_from) == 3 else inst_from[0]
    instruction = instructions[instruction]

    to_coord = tuple(int(x) for x in to_coord.split(","))
    from_coord = tuple(int(x) for x in from_coord.split(","))
    return (instruction, from_coord, to_coord)


def part1(input):
    grid = set()

    for instruction, from_coord, to_coord in input:
        from_x, from_y = from_coord
        to_x, to_y = to_coord

        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                if instruction == "ON":
                    grid.add((x, y))
                elif instruction == "OFF":
                    if (x, y) in grid:
                        grid.remove((x, y))
                elif instruction == "TOGGLE":
                    if (x, y) in grid:
                        grid.remove((x, y))
                    else:
                        grid.add((x, y))
    return len(grid)


def part2(input):
    grid = defaultdict(int)

    for instruction, from_coord, to_coord in input:
        from_x, from_y = from_coord
        to_x, to_y = to_coord

        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                if instruction == "ON":
                    grid[(x, y)] += 1
                elif instruction == "OFF":
                    grid[(x, y)] = 0 if grid[(x, y)] <= 1 else grid[(x, y)] - 1
                elif instruction == "TOGGLE":
                    grid[(x, y)] += 2

    return sum(grid.values())


main(DAY, YEAR, SAMPLE, parse, part1, part2)
