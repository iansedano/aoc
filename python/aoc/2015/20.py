from collections import defaultdict
from functools import cache

from common import main

DAY = 20
YEAR = 2015
SAMPLE = """"""


def parse(puzzle_input):
    return int(puzzle_input)


def part1(parsed_input):
    houses = defaultdict(int)

    house_max = parsed_input // 10

    for elf in range(1, house_max):
        for visit in range(elf, house_max, elf):
            houses[visit] += elf * 10
            if houses[elf] > parsed_input:
                return elf


def part2(parsed_input):
    houses = defaultdict(int)

    house_max = parsed_input // 10

    for elf in range(1, house_max):
        for visit in range(elf, elf * 51, elf):
            houses[visit] += elf * 11
            if houses[elf] > parsed_input:
                return elf


def get_divisors(num):
    divisors = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
