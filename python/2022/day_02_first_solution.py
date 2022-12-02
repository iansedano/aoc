from aocd import get_data

WIN = 6
DRAW = 3
LOSS = 0

HAND_SCORE = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}
HAND_KEY = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}
INSTRUCTION_KEY = {
    "X": "LOSE",
    "Y": "DRAW",
    "Z": "WIN",
}

"""
PART 1
"""


def determine_outcome(opponent, you):
    valid_hands = ["ROCK", "PAPER", "SCISSORS"]
    assert opponent in valid_hands and you in valid_hands
    if (
        (opponent == "ROCK" and you == "PAPER")
        or (opponent == "PAPER" and you == "SCISSORS")
        or (opponent == "SCISSORS" and you == "ROCK")
    ):
        return WIN
    elif opponent == you:
        return DRAW
    else:
        return LOSS


def calculate_score(line):
    """
    >>> calculate_score("A Y")
    8
    >>> calculate_score("B X")
    1
    >>> calculate_score("C Z")
    6
    """
    opponent, you = line.strip().split(" ")
    score = determine_outcome(HAND_KEY[opponent], HAND_KEY[you])
    return score + HAND_SCORE[you]


"""
PART 2
"""


def determine_score(opponent, instruction):
    match instruction, opponent:
        case ["WIN", "SCISSORS"]:
            return WIN + HAND_SCORE["ROCK"]
        case ["WIN", "ROCK"]:
            return WIN + HAND_SCORE["PAPER"]
        case ["WIN", "PAPER"]:
            return WIN + HAND_SCORE["SCISSORS"]
        case ["DRAW", _]:
            return DRAW + HAND_SCORE[opponent]
        case ["LOSE", "SCISSORS"]:
            return LOSS + HAND_SCORE["PAPER"]
        case ["LOSE", "ROCK"]:
            return LOSS + HAND_SCORE["SCISSORS"]
        case ["LOSE", "PAPER"]:
            return LOSS + HAND_SCORE["ROCK"]


def parse_scores(line):
    """
    >>> parse_scores("A Y")
    4
    >>> parse_scores("B X")
    1
    >>> parse_scores("C Z")
    7
    """
    opponent, instruction = line.strip().split(" ")
    return determine_score(HAND_KEY[opponent], INSTRUCTION_KEY[instruction])


"""
======================================================================
"""


def parse(puzzle_input):
    return puzzle_input.strip().split("\n")


def part1(data):
    return sum(calculate_score(line) for line in data)


def part2(data):
    return sum(parse_scores(line) for line in data)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


"""
======================================================================
"""

if __name__ == "__main__":
    puzzle_input = get_data(day=2, year=2022).strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))
