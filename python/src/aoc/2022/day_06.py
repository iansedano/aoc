from aocd import get_data


def part1(data):
    for a, b, c, d, i in zip(
        data[:-3],
        data[1:-2],
        data[2:-1],
        data[3:],
        range(4, len(data[3:])),
    ):
        if len({a, b, c, d}) == 4:
            return i


def part2(data):
    for i in range(len(data) - 14):
        window = data[i : i + 14]
        if len(set(window)) == 14:
            return i + 14


def main():
    puzzle_input = get_data(day=6, year=2022).strip()
    return part1(puzzle_input), part2(puzzle_input)


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
