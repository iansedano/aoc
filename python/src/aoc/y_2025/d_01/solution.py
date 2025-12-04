import itertools

import peek

from aoc.tools.grid import create_grid_dict_from_string


def parse(puzzle_input):
    lines = puzzle_input.splitlines()
    new_lines = []
    for line in lines:
        if line.startswith("R"):
            new_lines.append(("R", int(line.strip("R"))))
        else:
            new_lines.append(("L", int(line.strip("L"))))

    from collections import Counter

    peek(Counter(amount for _, amount in new_lines))

    return new_lines


def part_1(parsed_input):
    dial = 50
    zeros = 0
    for dir, amount in parsed_input:
        dial = rotate_dial(dial, amount if dir == "R" else -amount)
        if dial == 0:
            zeros += 1

    return zeros


def rotate_dial(dial, amount, size=99):
    """
    >>> rotate_dial(99, 1)
    0
    >>> rotate_dial(0, -1)
    99
    >>> rotate_dial(0, -100)
    0
    >>> rotate_dial(0, -200)
    0
    >>> rotate_dial(0, -300)
    0
    >>> rotate_dial(99, 100)
    99
    >>> rotate_dial(99, 200)
    99
    >>> rotate_dial(99, 300)
    99
    >>> rotate_dial(0, 100)
    0
    >>> rotate_dial(0, 300)
    0
    >>> rotate_dial(99, 101)
    0
    >>> rotate_dial(99, -100)
    99
    """

    dial = dial + amount

    return dial % (size + 1)


def part_2(parsed_input):
    dial = 50
    zeros = 0
    for dir, amount in parsed_input:
        peek(dial, dir, amount)
        dial, new_zeros = rotate_dial_with_zeros(
            dial, amount if dir == "R" else -amount
        )
        peek(new_zeros)
        zeros += new_zeros
        peek(dial)
        print("---")

    return zeros


def rotate_dial_with_zeros(starting_dial, amount, size=99):
    """
    >>> rotate_dial_with_zeros(99, 1)
    (0, 1)
    >>> rotate_dial_with_zeros(0, -1)
    (99, 0)
    >>> rotate_dial_with_zeros(0, -100)
    (0, 1)
    >>> rotate_dial_with_zeros(0, -200)
    (0, 2)
    >>> rotate_dial_with_zeros(0, -300)
    (0, 3)
    >>> rotate_dial_with_zeros(99, 100)
    (99, 1)
    >>> rotate_dial_with_zeros(99, 200)
    (99, 2)
    >>> rotate_dial_with_zeros(99, 300)
    (99, 3)
    >>> rotate_dial_with_zeros(0, 100)
    (0, 1)
    >>> rotate_dial_with_zeros(0, 300)
    (0, 3)
    >>> rotate_dial_with_zeros(99, 101)
    (0, 2)
    >>> rotate_dial_with_zeros(99, -100)
    (99, 1)
    >>> rotate_dial_with_zeros(98, 3)
    (1, 1)
    >>> rotate_dial_with_zeros(1, -2)
    (99, 1)
    >>> rotate_dial_with_zeros(50, -68)
    (82, 1)
    >>> rotate_dial_with_zeros(82, -30)
    (52, 0)
    >>> rotate_dial_with_zeros(95, 60)
    (55, 1)
    >>> rotate_dial_with_zeros(95, 160)
    (55, 2)
    >>> rotate_dial_with_zeros(32, -60)
    (72, 1)
    >>> rotate_dial_with_zeros(32, -160)
    (72, 2)
    >>> rotate_dial_with_zeros(32, -32)
    (0, 1)
    >>> rotate_dial_with_zeros(0, 3)
    (3, 0)
    >>> rotate_dial_with_zeros(0, 100)
    (0, 1)
    >>> rotate_dial_with_zeros(54, 43)
    (97, 0)
    >>> rotate_dial_with_zeros(54, 943)
    (97, 9)
    >>> rotate_dial_with_zeros(0, 0)
    (0, 0)
    >>> rotate_dial_with_zeros(0, 1000)
    (0, 10)
    >>> rotate_dial_with_zeros(1, 198)
    (99, 1)
    >>> rotate_dial_with_zeros(0, 198)
    (98, 1)
    >>> rotate_dial_with_zeros(0, 199)
    (99, 1)
    >>> rotate_dial_with_zeros(0, 297)
    (97, 2)
    >>> rotate_dial_with_zeros(0, 200)
    (0, 2)
    """

    zeros = 0
    cycle_length = size + 1
    zeros = abs(amount) // cycle_length

    remainder = abs(amount) % cycle_length
    direction = -1 if amount < 0 else 1

    result = (starting_dial + (remainder * direction)) % cycle_length

    if remainder > 0:
        if direction == 1:
            if starting_dial + remainder >= cycle_length:
                zeros += 1
        else:
            if starting_dial > 0 and (starting_dial - remainder) <= 0:
                zeros += 1

    return result, zeros
