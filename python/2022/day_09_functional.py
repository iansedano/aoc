import math
import itertools
from aocd import get_data
from dataclasses import dataclass

SAMPLE = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

SAMPLE_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


@dataclass
class Vec:
    x: int
    y: int

    @classmethod
    def from_vec(cls, vec):
        return cls(vec.x, vec.y)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) == tuple:
            if len(other) != 2:
                raise TypeError
            return self.x == other[0] and self.y == other[1]
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"


DIRECTIONS = {"U": Vec(0, -1), "R": Vec(1, 0), "D": Vec(0, 1), "L": Vec(-1, 0)}


def sign(n):
    return math.copysign(1, n) if abs(n) > 0 else 0


def parse(puzzle_input):

    return [
        (line.split()[0], int(line.split()[1]))
        for line in puzzle_input.splitlines()
    ]


def new_tail_position(head, tail):
    distance = head - tail

    if abs(distance.x) <= 1 and abs(distance.y) <= 1:
        return Vec(tail.x, tail.y)
    else:
        return Vec(
            tail.x + sign(distance.x),
            tail.y + sign(distance.y),
        )


def move(rope, direction):
    rope = list(rope)
    rope[0] = rope[0] + DIRECTIONS[direction]
    for i in range(1, len(rope)):
        rope[i] = new_tail_position(rope[i - 1], rope[i])
    return rope


def visualize(rope, positions):
    y_range = -280, 10
    x_range = -50, 250
    for y in range(*y_range):
        for x in range(*x_range):
            if Vec(x, y) == rope[0]:
                print("H", end="")
            elif Vec(x, y) in rope:
                print(rope.index(Vec(x, y)) + 1, end="")
            elif Vec(x, y) in positions:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print("\n")


def part1(data):
    """Solve part 1."""
    rope = [Vec(0, 0) for _ in range(2)]
    positions = {rope[-1]}
    for instruction in data:
        direction, amount = instruction
        for _ in range(amount):
            rope = move(rope, direction)
            positions.add(rope[-1])

    return len(positions)


def part2(data):
    """Solve part 2."""
    rope = [Vec(0, 0) for _ in range(10)]
    positions = {rope[-1]}
    for instruction in data:
        direction, amount = instruction
        for _ in range(amount):
            rope = move(rope, direction)
            positions.add(rope[-1])

    return len(positions)


def main():
    puzzle_input = get_data(day=9, year=2022).strip()
    # puzzle_input = SAMPLE
    # puzzle_input = SAMPLE_2
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
