from pprint import pp

from aocd import get_data


def parse(puzzle_input: str):
    """Parse input."""
    pp(puzzle_input)


def part1(data):
    """Solve part 1."""


def part2(data):
    """Solve part 2."""


def main():
    puzzle_input = get_data(day=XX, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
