from common import main

DAY = 18
YEAR = 2023
SAMPLE = """\
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

DIRECTIONS = {
    "3": (0, -1),
    "U": (0, -1),
    "0": (1, 0),
    "R": (1, 0),
    "1": (0, 1),
    "D": (0, 1),
    "2": (-1, 0),
    "L": (-1, 0),
}


def parse(puzzle_input):
    lines = [tuple(line.split()) for line in puzzle_input.splitlines()]
    return [
        (DIRECTIONS[direction], int(num), color.strip("()#"))
        for direction, num, color in lines
    ]


def part1(parsed_input):
    position = (0, 0)
    outline = []
    for direction, num, _ in parsed_input:
        for _ in range(num):
            position = add_v(direction, position)
            outline.append(position)

    return shoelace(outline, len(outline))


def part2(parsed_input):
    instructions = [
        (DIRECTIONS[inst[-1]], int(inst[:-1], 16))
        for _, _, inst in parsed_input
    ]

    position = (0, 0)
    outline = []
    circumference = 0
    for direction, num in instructions:
        circumference += num
        position = add_v(mul_v(direction, num), position)
        outline.append(position)

    return shoelace(outline, circumference)


def shoelace(outline, circumference):
    sum_a = 0
    sum_b = 0

    for (x_a, y_a), (x_b, y_b) in zip(outline, outline[1:] + outline[:1]):
        sum_a += x_a * y_b
        sum_b += y_a * x_b

    return (abs(sum_a - sum_b) / 2) + (circumference / 2) + 1


def add_v(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul_v(a, b):
    return (a[0] * b, a[1] * b)


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
