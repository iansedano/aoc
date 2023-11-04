from common import main
from parse import compile

DAY = 16
YEAR = 2015
SAMPLE = """Sue 329: perfumes: 3, goldfish: 10, akitas: 3
"""
TICKER_TAPE = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

SUE_PATTERN = compile("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}")
TICKER_PATTERN = compile("{}: {:d}")


def parse(puzzle_input):
    ticker = dict(TICKER_PATTERN.parse(line).fixed for line in TICKER_TAPE.splitlines())

    lines = (SUE_PATTERN.parse(line).fixed for line in puzzle_input.splitlines())

    sues = {
        line[0]: {key: val for key, val in zip(line[1::2], line[2::2])}
        for line in lines
    }

    return ticker, sues


def part1(input):
    ticker, sues = input

    for sue_number, possessions in sues.items():
        if all(
            possessions[item] == amount
            for item, amount in ticker.items()
            if item in possessions
        ):
            return sue_number


def check_possession(item, amount, target_amount):
    if item in ["cats", "trees"]:
        return amount > target_amount
    elif item in ["pomeranians", "goldfish"]:
        return amount < target_amount
    else:
        return amount == target_amount


def part2(input):
    ticker, sues = input

    for sue_number, possessions in sues.items():
        if all(
            check_possession(item, possessions[item], amount)
            for item, amount in ticker.items()
            if item in possessions
        ):
            return sue_number


main(DAY, YEAR, SAMPLE, parse, part1, part2)
