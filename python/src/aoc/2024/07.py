import itertools
from textwrap import dedent

from aocd import get_data

DAY = 7
YEAR = 2024
SAMPLE = dedent(
    """\
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """
)


def parse(puzzle_input):

    lines = [line.split(": ") for line in puzzle_input.splitlines()]

    return [
        (int(result), [int(num) for num in numbers.split(" ")])
        for result, numbers in lines
    ]


def part_1(parsed_input):

    solution = 0

    for result, numbers in parsed_input:

        for perm in itertools.product(["+", "*"], repeat=len(numbers) - 1):
            total = numbers[0]
            index = 1
            for op in perm:
                if op == "+":
                    total = total + numbers[index]
                elif op == "*":
                    total = total * numbers[index]
                index += 1
            if total == result:

                solution += result
                break

    return solution


def part_2(parsed_input):
    solution = 0

    for result, numbers in parsed_input:

        for perm in itertools.product(
            ["+", "*", "||"], repeat=len(numbers) - 1
        ):
            total = numbers[0]
            index = 1
            for op in perm:
                if op == "+":
                    total = total + numbers[index]
                elif op == "*":
                    total = total * numbers[index]
                elif op == "||":
                    total = int(str(total) + str(numbers[index]))
                index += 1
            if total == result:

                solution += result
                break

    return solution


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(data)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
