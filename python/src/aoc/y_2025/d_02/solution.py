import peek

from aoc.tools.grid import create_grid_dict_from_string


def parse(puzzle_input):
    return [
        tuple(int(p) for p in rng.split("-")) for rng in puzzle_input.split(",")
    ]
    return [line for line in puzzle_input.splitlines()]
    return [line.split(",") for line in puzzle_input.splitlines()]


def part_1(parsed_input):

    invalids = []

    for start, end_inclusive in parsed_input:
        for x in range(start, end_inclusive + 1):
            if not is_valid(x):
                invalids.append(x)

    return sum(invalids)


def is_valid(id):
    """
    >>> is_valid(123123)
    False
    >>> is_valid(11)
    False
    >>> is_valid(110110)
    False
    >>> is_valid(239009)
    True
    """

    id_str = str(id)

    length = len(id_str)

    if length % 2 != 0:
        return True

    sequence_length = length // 2

    if id_str[:sequence_length] == id_str[sequence_length:]:
        return False

    return True


def part_2(parsed_input):
    invalids = []

    for start, end_inclusive in parsed_input:
        for x in range(start, end_inclusive + 1):
            if not is_valid_plus(x):
                invalids.append(x)

    return sum(invalids)


def is_valid_plus(id):
    """
    >>> is_valid_plus(123123)
    False
    >>> is_valid_plus(11)
    False
    >>> is_valid_plus(110110)
    False
    >>> is_valid_plus(239009)
    True
    >>> is_valid_plus(999)
    False
    >>> is_valid_plus(565656)
    False
    >>> is_valid_plus(824824824)
    False
    >>> is_valid_plus(2121212121)
    False
    >>> is_valid_plus(111)
    False
    """

    id_str = str(id)

    length = len(id_str)

    max_length = length // 2

    for seq_len in range(1, max_length + 1):
        if similar_segments(id_str, seq_len):
            return False

    return True


def similar_segments(id_str, seq_len):
    """
    >>> similar_segments("2121212121", 2)
    True
    """
    length = len(id_str)

    if length % seq_len != 0:
        return False

    number_of_segments = length // seq_len

    segments = set()

    for x in range(number_of_segments):
        start = x * seq_len
        end = start + seq_len

        segments.add(id_str[start:end])
        # try:
        #     segments.add(id_str[start:end])
        # except IndexError:
        #     return False

    if len(segments) == 1:
        return True


if __name__ == "__main__":
    similar_segments("2121212121", 2)
