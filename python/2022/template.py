import sys

from pprint import pp

from aocd import get_data

DAY = None
SAMPLE = """"""


def parse(puzzle_input: str):
    """Parse input."""
    pp(puzzle_input)


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 2."""


def main(main=True):
    if main:
        print("MAIN")
        data = parse(get_data(day=DAY, year=2022).strip())
    else:
        print("SAMPLE")
        data = SAMPLE.strip()

    solution1 = part1(data)
    solution2 = part2(data)

    print(f"\t{solution1 = }\n\t{solution2 = }")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(False)
        main(True)
    elif sys.argv[1] == "sample":
        main(False)
    elif sys.argv[1] == "main":
        main(True)
