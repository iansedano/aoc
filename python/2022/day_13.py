import itertools
import json
from copy import deepcopy
from functools import cmp_to_key

from aocd import get_data

SAMPLE = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


class Empty:
    def __repr__(self):
        return "Empty"


def parse(puzzle_input):
    """Parse input."""
    return [
        [json.loads(packet) for packet in pair.split("\n")]
        for pair in puzzle_input.split("\n\n")
    ]


def get_item(item, left=True):
    try:
        return item.pop(0)
    except IndexError:
        return Empty()


def compare(left, right):
    """
    >>> compare([1,1,3,1,1], [1,1,5,1,1])
    True
    >>> compare([[1],[2,3,4]], [[1],4])
    True
    >>> compare([9], [[8,7,6]])
    False
    >>> compare([[4,4],4,4], [[4,4],4,4,4])
    True
    >>> compare([7,7,7,7], [7,7,7])
    False
    >>> compare([], [3])
    True
    >>> compare([[[]]], [[]])
    False
    >>> compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
    False
    """
    left = deepcopy(left)
    right = deepcopy(right)

    while True:
        left_item = get_item(left)
        right_item = get_item(right)

        match type(left_item).__name__, type(right_item).__name__:
            case ("int", "int"):
                if left_item == right_item:
                    continue
                else:
                    return left_item < right_item
            case ("list", "int"):
                comparison = compare(left_item, [right_item])
                if comparison is None:
                    continue
                else:
                    return comparison
            case ("int", "list"):
                comparison = compare([left_item], right_item)
                if comparison is None:
                    continue
                else:
                    return comparison
            case ("list", "list"):
                comparison = compare(left_item, right_item)
                if comparison is None:
                    continue
                else:
                    return comparison
            case ("Empty", "Empty"):
                return None
            case ("Empty", _):
                return True
            case (_, "Empty"):
                return False


def wrap_compare(left, right):
    """
    >>> wrap_compare([1,1,3,1,1], [1,1,5,1,1])
    1
    >>> wrap_compare([[1],[2,3,4]], [[1],4])
    1
    >>> wrap_compare([9], [[8,7,6]])
    -1
    >>> wrap_compare([[4,4],4,4], [[4,4],4,4,4])
    1
    >>> wrap_compare([7,7,7,7], [7,7,7])
    -1
    >>> wrap_compare([], [3])
    1
    >>> wrap_compare([[[]]], [[]])
    -1
    >>> wrap_compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
    -1
    """

    match compare(left, right):
        case True:
            return 1
        case False:
            return -1
        case None:
            return 0


def gah_compare(left, right):
    """by @gahjelle"""
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else -1 if left > right else 0
    elif isinstance(left, int):
        return gah_compare([left], right)
    elif isinstance(right, int):
        return gah_compare(left, [right])
    else:
        for lf, rg in zip(left, right):
            if (cmp := gah_compare(lf, rg)) != 0:
                return cmp
        return gah_compare(len(left), len(right))


def salabim_compare(left, right):
    """by @salabim"""
    for left, right in itertools.zip_longest(left, right):
        if left is None:
            return -1
        if right is None:
            return 1

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            if left > right:
                return 1
        else:
            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right
            if salabim_compare(left, right):
                return salabim_compare(left, right)


def part1(data):
    return sum(i + 1 for i in range(len(data)) if compare(*data[i]))


def part2(data):
    marker1 = [[2]]
    marker2 = [[6]]

    flattened_data = [packet for pair in data for packet in pair]
    flattened_data.extend([marker1, marker2])
    sorted_data = sorted(
        flattened_data, key=cmp_to_key(wrap_compare), reverse=True
    )

    idxs = []
    for i, item in enumerate(sorted_data):
        if item == marker1:
            idxs.append(i + 1)
        if item == marker2:
            idxs.append(i + 1)
        if len(idxs) == 2:
            break
    return idxs[0] * idxs[1]


def main():
    puzzle_input = get_data(day=13, year=2022).strip()
    data = parse(puzzle_input)
    # data = parse(SAMPLE)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
