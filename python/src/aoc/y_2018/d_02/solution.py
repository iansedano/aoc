import itertools
from collections import defaultdict

from aoc.tools.grid import create_grid_dict_from_string


def parse(puzzle_input):
    return puzzle_input.splitlines()
    return [line for line in puzzle_input.splitlines()]
    return [line.split(",") for line in puzzle_input.splitlines()]


def part_1(parsed_input):

    counter = defaultdict(int)
    for word in parsed_input:
        counts = letter_counts(word)
        if 2 in counts:
            counter[2] += 1
        if 3 in counts:
            counter[3] += 1

    return counter[2] * counter[3]


def part_2(parsed_input):

    for a, b in itertools.product(parsed_input, repeat=2):
        found_difference = False
        discard = False
        for i, letter in enumerate(a):
            if letter != b[i]:
                if found_difference:
                    discard = True
                    break
                found_difference = True

        if discard or not found_difference:
            continue

        a_letter = None
        for letter in a:
            if letter not in b:
                a_letter = letter
                break
        return "".join([letter for letter in a if letter != a_letter])

    return


def letter_counts(word):
    counts = defaultdict(int)
    for letter in word:
        counts[letter] += 1

    return set(counts.values())
