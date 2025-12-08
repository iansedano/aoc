from math import prod


def parse(puzzle_input):
    return puzzle_input


def part_1(parsed_input):
    parsed_input = [
        [int(x) if x not in "+*" else x for x in line.split()]
        for line in parsed_input.splitlines()
    ]

    length = len(parsed_input[0])

    problems = [
        [parsed_input[y][x] for y in range(len(parsed_input))]
        for x in range(length)
    ]
    problems = [(p[-1], p[:-1]) for p in problems]

    return solve_problems(problems)


def part_2(parsed_input):
    lines = parsed_input.splitlines()
    ops = lines[-1]

    indices = []
    for i, char in enumerate(ops):
        if char in "+*":
            indices.append(i)

    problems = []
    num_rows = lines[:-1]
    for starting_idx, next_idx in zip(indices, indices[1:] + [len(ops) + 1]):
        op = ops[starting_idx]
        cols = []
        for n_row in num_rows:
            number = []
            for i in range(starting_idx, next_idx - 1):
                number.append(n_row[i])
            cols.append(number)

        numbers = []
        for i in range(len(cols[0]) - 1, -1, -1):
            number = []
            for col in cols:
                number.append(col[i])
            numbers.append(int("".join(number)))

        problems.append((op, numbers))

    return solve_problems(problems)


def solve_problems(problems):
    total = 0

    for op, nums in problems:
        if op == "+":
            total += sum(nums)
        elif op == "*":
            total += prod(nums)
    return total
