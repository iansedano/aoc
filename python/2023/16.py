import sys

from common import main

DAY = 16
YEAR = 2023
SAMPLE = R""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


def parse(puzzle_input):
    grid = {}
    max_x, max_y = 0, 0

    for y, row in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(row):
            max_x, max_y = max(x, max_x), max(y, max_y)
            if char == ".":
                continue
            grid[(x, y)] = char

    return grid, (max_x, max_y)


def part1(parsed_input):
    grid, shape = parsed_input
    beam_pos = (0, 0)
    beam_dir = (1, 0)

    sys.setrecursionlimit(3400)
    return len(shine(beam_pos, beam_dir, grid, shape))


def part2(parsed_input):
    grid, shape = parsed_input

    sys.setrecursionlimit(4000)
    max_energy = 0
    for i in range(shape[0]):
        max_energy = max(
            max_energy,
            len(shine((i, 0), (0, 1), grid, shape)),
            len(shine((i, shape[1]), (0, -1), grid, shape)),
        )

    for i in range(shape[1]):
        max_energy = max(
            max_energy,
            len(shine((0, i), (1, 0), grid, shape)),
            len(shine((shape[0], i), (-1, 0), grid, shape)),
        )

    return max_energy


def shine(beam_pos, beam_dir, grid, shape):
    energized = set()

    def _shine(beam_pos, beam_dir):
        if any(
            [
                beam_pos[0] > shape[0],
                beam_pos[1] > shape[1],
                beam_pos[0] < 0,
                beam_pos[1] < 0,
                (beam_pos, beam_dir) in energized,
            ]
        ):
            return

        energized.add((beam_pos, beam_dir))

        if beam_pos not in grid:
            _shine(add_v(beam_pos, beam_dir), beam_dir)
            return

        item = grid[beam_pos]

        if item in "\\/":
            beam_dir = get_new_beam_dir(item, beam_dir)
            _shine(add_v(beam_pos, beam_dir), beam_dir)
            return

        if (item == "-" and beam_dir in [(1, 0), (-1, 0)]) or (
            item == "|" and beam_dir in [(0, 1), (0, -1)]
        ):
            _shine(add_v(beam_pos, beam_dir), beam_dir)
            return

        if item == "-":
            dir_a, dir_b = (1, 0), (-1, 0)
        elif item == "|":
            dir_a, dir_b = (0, -1), (0, 1)

        _shine(add_v(beam_pos, dir_b), dir_b)
        _shine(add_v(beam_pos, dir_a), dir_a)
        return

    _shine(beam_pos, beam_dir)

    return set(e[0] for e in energized)


def add_v(a, b):
    return (a[0] + b[0], a[1] + b[1])


def get_new_beam_dir(mirror, beam_dir):
    match (mirror, beam_dir):
        case ("\\", (1, 0)):
            return (0, 1)
        case ("\\", (0, 1)):
            return (1, 0)
        case ("\\", (-1, 0)):
            return (0, -1)
        case ("\\", (0, -1)):
            return (-1, 0)
        case ("/", (1, 0)):
            return (0, -1)
        case ("/", (0, 1)):
            return (-1, 0)
        case ("/", (-1, 0)):
            return (0, 1)
        case ("/", (0, -1)):
            return (1, 0)


def debug(pos_set, shape):
    out = []
    for y in range(shape[1]):
        out.append("\n")
        for x in range(shape[0]):
            if (x, y) in pos_set:
                out.append("#")
            else:
                out.append(".")
    return "".join(out)


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
