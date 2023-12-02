import math
from contextlib import suppress

from common import main

DAY = 2
YEAR = 2023
SAMPLE = """"""


def parse(puzzle_input):
    """
    >>> parse('''Game 1: 4 blue; 1 red, 2 green, 11 blue; 12 blue, 1 green, 1 red
    ... Game 2: 10 blue, 5 green; 4 green, 3 red, 6 blue; 2 green, 4 red, 1 blue''')
    ... # doctest: +NORMALIZE_WHITESPACE
    [({'blue': 4},
      {'red': 1, 'green': 2, 'blue': 11},
      {'blue': 12, 'green': 1, 'red': 1}),
     ({'blue': 10, 'green': 5},
      {'green': 4, 'red': 3, 'blue': 6},
      {'green': 2, 'red': 4, 'blue': 1})]
    """
    return [parse_line(line) for line in puzzle_input.splitlines()]


def parse_line(line):
    """
    >>> parse_line("Game 1: 4 blue; 1 red, 2 green, 11 blue; 12 blue, 1 green, 1 red")
    ... # doctest: +NORMALIZE_WHITESPACE
    ({'blue': 4},
     {'red': 1, 'green': 2, 'blue': 11},
     {'blue': 12, 'green': 1, 'red': 1})
    """
    _, selections = line.split(": ")
    return tuple(parse_cube_selection(part) for part in selections.split("; "))


def parse_cube_selection(selection):
    """
    >>> parse_cube_selection("1 red, 2 green, 11 blue")
    {'red': 1, 'green': 2, 'blue': 11}
    """
    split = (cube.split(" ") for cube in selection.split(", "))
    return {cube[1]: int(cube[0]) for cube in split}


def part1(parsed_input):
    return sum(
        i if valid_game(game) else 0 for i, game in enumerate(parsed_input, 1)
    )


def part2(parsed_input):
    return sum(math.prod(min_cubes(game).values()) for game in parsed_input)


def valid_game(game):
    """
    >>> valid_game([
    ...     {'red': 1, 'green': 1, 'blue': 1},
    ...     {'red': 1, 'green': 1, 'blue': 1}
    ... ])
    True
    >>> valid_game([
    ...     {'red': 99, 'green': 1, 'blue': 1},
    ...     {'red': 1, 'green': 1, 'blue': 1}
    ... ])
    False
    """
    for pick in game:
        for color, max_number in [("red", 12), ("green", 13), ("blue", 14)]:
            with suppress(KeyError):
                if pick[color] > max_number:
                    return False
    return True


def min_cubes(game):
    """
    >>> min_cubes([
    ...    {'red': 1, 'green': 1, 'blue': 2},
    ...    {'red': 1, 'green': 1, 'blue': 1}
    ... ])
    {'red': 1, 'green': 1, 'blue': 2}
    >>> min_cubes([
    ...     {'red': 99, 'green': 1, 'blue': 1},
    ...     {'red': 1, 'green': 99, 'blue': 1}
    ... ])
    {'red': 99, 'green': 99, 'blue': 1}
    """
    result = {"red": 0, "green": 0, "blue": 0}
    for pick in game:
        for color in result.keys():
            with suppress(KeyError):
                result[color] = max(result[color], pick[color])
    return result


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
