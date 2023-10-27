from common import main
import json
import pprint

DAY = 12
YEAR = 2015
SAMPLE = ""


def parse(puzzle_input):
    return json.loads(puzzle_input)


def get_numbers_from_list(input):
    return tuple(item for item in input if isinstance(item, int))


def has_red(obj: dict):
    return any(value == "red" for value in obj.values())


def get_numbers(obj, exclude_red=False):
    if isinstance(obj, dict):
        if exclude_red and has_red(obj):
            return
        for item in obj.values():
            if isinstance(item, int):
                yield item
            elif isinstance(item, str):
                continue
            else:
                yield from get_numbers(item, exclude_red)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, int):
                yield item
            elif isinstance(item, str):
                continue
            else:
                yield from get_numbers(item, exclude_red)


def part1(input):
    return sum(get_numbers(input))


def part2(input):
    return sum(get_numbers(input, exclude_red=True))


main(DAY, YEAR, SAMPLE, parse, part1, part2)
