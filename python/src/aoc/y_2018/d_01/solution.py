def parse(puzzle_input):
    nums = [int(line) for line in puzzle_input.splitlines()]
    return nums


def part_1(parsed_input):
    return sum(parsed_input)


def part_2(parsed_input):
    seen = {0}
    current = 0

    while True:
        for num in parsed_input:
            current += num
            if current in seen:
                return current
            else:
                seen.add(current)
