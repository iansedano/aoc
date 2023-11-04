from itertools import chain, combinations, islice

from common import main

DAY = 17
YEAR = 2015
SAMPLE = """"""


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.splitlines()]


def part1(input):
    return len([bottles for bottles in powerset(input) if sum(bottles) == 150])


def part2(input):
    combs = sorted(
        [bottles for bottles in powerset(input) if sum(bottles) == 150],
        key=lambda b: len(b),
    )
    min_len = len(combs[0])
    return len([comb for comb in combs if len(comb) == min_len])


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


main(DAY, YEAR, SAMPLE, parse, part1, part2)
