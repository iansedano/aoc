from aocd import get_data

HAND_KEY = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}
HAND_TO_WIN_AGAINST = {
    "ROCK": "PAPER",
    "PAPER": "SCISSORS",
    "SCISSORS": "ROCK",
}
HAND_TO_LOSE_AGAINST = {v: k for k, v in HAND_TO_WIN_AGAINST.items()}
HAND_SCORE = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}
OUTCOME_SCORE = {"WIN": 6, "DRAW": 3, "LOSS": 0}
INSTRUCTION_KEY = {
    "X": "LOSS",
    "Y": "DRAW",
    "Z": "WIN",
}


def calculate_score(self, other):
    if HAND_TO_WIN_AGAINST[other] == self:
        return OUTCOME_SCORE["WIN"] + HAND_SCORE[self]
    elif other == self:
        return OUTCOME_SCORE["DRAW"] + HAND_SCORE[self]
    else:
        return OUTCOME_SCORE["LOSS"] + HAND_SCORE[self]


def calculate_score_with_instruction(instruction, other):
    if instruction == "WIN":
        return calculate_score(HAND_TO_WIN_AGAINST[other], other)
    elif instruction == "DRAW":
        return calculate_score(other, other)
    elif instruction == "LOSS":
        return calculate_score(HAND_TO_LOSE_AGAINST[other], other)


def part1(data):
    return sum(
        calculate_score(HAND_KEY[line[2]], HAND_KEY[line[0]]) for line in data
    )


def part2(data):
    return sum(
        calculate_score_with_instruction(
            INSTRUCTION_KEY[line[2]], HAND_KEY[line[0]]
        )
        for line in data
    )


def parse(puzzle_input):
    return puzzle_input.strip().split("\n")


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    puzzle_input = get_data(day=2, year=2022).strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
