from aocd import get_data

"""
"""

DAY = 2

def parse(puzzle_input):
    return puzzle_input

def part1(input):
    """
    """


def part2(input):
    """
    """


def main():
    puzzle_input = get_data(day=DAY, year=2015).strip()
    input = parse(puzzle_input)
    solution1 = part1(input)
    solution2 = part2(input)

    return solution1, solution2


if __name__ == "__main__":
    solution_1, solution_2 = main()
    print(f"{solution_1 = }\n{solution_2 = }")