from aocd import get_data

# ( up one
# ) down one

def parse(puzzle_input):
    return puzzle_input

def part1(input):
    return input.count("(") - input.count(")")


# index at 1
# which char is the first to cause santa to enter the basement

def part2(input):
    level = 0
    for i, char in enumerate(input):
        if char == "(":
            level += 1
        else:
            level -= 1
        
        if level == -1:
            return i + 1


def main():
    puzzle_input = get_data(day=1, year=2015).strip()
    input = parse(puzzle_input)
    solution1 = part1(input)
    solution2 = part2(input)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")