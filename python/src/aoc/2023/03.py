import itertools
import math
from collections import defaultdict

from common import main

DAY = 3
YEAR = 2023
SAMPLE = """"""


def parse(puzzle_input):
    symbols, numbers = {}, []
    parsed_num = False

    for y, line in enumerate(puzzle_input.splitlines()):
        for x, char in enumerate(line):
            if char == ".":
                parsed_num = False
                continue
            if not char.isdigit():
                parsed_num = False
                symbols[(x, y)] = char
            if char.isdigit() and not parsed_num:
                parsed_num = True
                new_num = []
                for d_x, n_char in enumerate(line[x:]):
                    if n_char.isdigit():
                        new_num.append((n_char, (x + d_x, y)))
                    else:
                        break
                new_int = int("".join(char for char, _ in new_num))
                coords = [coord for _, coord in new_num]
                numbers.append((new_int, coords))

    return numbers, symbols


def part1(parsed_input: tuple[list, list]):
    numbers, symbols = parsed_input

    number_adj_map = []
    for num, coords in numbers:
        adjacent = set(
            a_c for c in coords for a_c in get_adjacent_positions(c)
        ) - set(coords)
        number_adj_map.append((num, adjacent))

    return sum(
        number
        for number, coords in number_adj_map
        if any(c in symbols for c in coords)
    )


def part2(parsed_input):
    numbers, symbols = parsed_input

    potential_gears = set(pos for pos, char in symbols.items() if char == "*")

    number_adj_map = []
    for num, coords in numbers:
        adjacent = set(
            a_c for c in coords for a_c in get_adjacent_positions(c)
        ) - set(coords)
        number_adj_map.append((num, adjacent))

    gears = defaultdict(list)
    for num, num_coords in number_adj_map:
        if any((coord := c) in potential_gears for c in num_coords):
            gears[coord].append(num)

    return sum(
        math.prod(positions)
        for positions in gears.values()
        if len(positions) == 2
    )


def get_adjacent_positions(position):
    """
    >>> get_adjacent_positions((5,5)) # doctest: +NORMALIZE_WHITESPACE
    [(4, 4),
     (4, 5),
     (4, 6),
     (5, 4),
     (5, 6),
     (6, 4),
     (6, 5),
     (6, 6)]
    """
    return [
        (position[0] + pos[0], position[1] + pos[1])
        for pos in itertools.product([-1, 0, 1], repeat=2)
        if pos != (0, 0)
    ]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
