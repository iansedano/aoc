from string import ascii_letters

from common import main

DAY = 1
YEAR = 2023
SAMPLE = """"""

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0,
}


def parse(puzzle_input):
    return puzzle_input.splitlines()


def part1(parsed_input):
    stripped = [line.strip(ascii_letters) for line in parsed_input]
    numbers = [int(line[0] + line[-1]) for line in stripped]
    return sum(numbers)


def part2(parsed_input):
    return sum(find_numbers(line) for line in parsed_input)


def find_numbers(line: str):
    """
    >>> find_numbers("9five9six8threet")
    93
    >>> find_numbers("fgftp5")
    55
    """
    start, end = None, None
    for i in range(len(line)):
        for num in NUMBER_MAP.keys():
            if line[i:].startswith(num):
                start = num
                break
        if start is not None:
            break

    for i in range(0, -len(line), -1):
        for num in NUMBER_MAP.keys():
            if line[: i if i != 0 else None].endswith(num):
                end = num
                break
        if end is not None:
            break
    return int(f"{NUMBER_MAP[start]}{NUMBER_MAP[end]}")


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
