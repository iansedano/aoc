from hashlib import md5

from common import main

DAY = 4
YEAR = 2015
SAMPLE = "abcdef"


def parse(puzzle_input):
    return puzzle_input


def part1(input):
    for i in range(1, 1000000):
        hash = md5(f"{input}{i}".encode("utf-8"))

        if hash.hexdigest()[:5] == "00000":
            return i


def part2(input):
    for i in range(1, 10000000):
        hash = md5(f"{input}{i}".encode("utf-8"))

        if hash.hexdigest()[:6] == "000000":
            return i


main(DAY, YEAR, SAMPLE, parse, part1, part2)
