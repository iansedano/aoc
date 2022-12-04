from aocd import get_data


def parse(puzzle_input):
    return [
        [
            [int(section) for section in job.split("-")]
            for job in line.split(",")
        ]
        for line in puzzle_input.split("\n")
    ]


def part1(data):
    return sum(
        (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])
        or (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1])
        for pair in data
    )


def part2(data):
    return sum(
        pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1] for pair in data
    )


def main():
    puzzle_input = get_data(day=4, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()

    print(f"{solution1 = }\n{solution2 = }")
