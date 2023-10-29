import re

from common import main

DAY = 8
YEAR = 2015
SAMPLE = r"""""
"abc"
"aaa\"aaa"
"\x27"
"""

"""
"erse\x9etmzhlmhy\x67yftoti"
"fdsa\\x123"
"""


def parse(puzzle_input):
    return puzzle_input.strip().splitlines()


def count_code_chars(line):
    return len(line)


def count_memory_chars(line: str):
    line = line[1:-1]
    count = 0
    char_gen = iter(line)
    while char := next(char_gen, False):
        if char == "\\":
            if char := next(char_gen, False):
                if char == "x":
                    next(char_gen)
                    next(char_gen)
                count += 1
        else:
            count += 1

    return count


def encoded_length(line: str):
    new_chars = []
    char_gen = iter(line)
    while char := next(char_gen, False):
        if char in ["\\", '"']:
            new_chars.append("\\")
        new_chars.append(char)

    return len(new_chars) + 2


def part1(input):
    # 1129 too low
    # 1344 too high
    return sum(
        count_code_chars(line.strip()) - count_memory_chars(line.strip())
        for line in input
    )


def part2(input):
    return sum(
        encoded_length(line.strip()) - count_code_chars(line.strip()) for line in input
    )


main(DAY, YEAR, SAMPLE, parse, part1, part2)
