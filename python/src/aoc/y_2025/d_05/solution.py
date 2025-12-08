def parse(puzzle_input):
    id_ranges, available_ids = puzzle_input.split("\n\n")

    id_ranges = id_ranges.splitlines()
    available_ids = available_ids.splitlines()

    return (
        [
            tuple(int(part) for part in id_range.split("-"))
            for id_range in id_ranges
        ],
        [int(id) for id in available_ids],
    )


def part_1(parsed_input):

    id_ranges, available_ids = parsed_input

    id_ranges = [range(low, high + 1) for low, high in id_ranges]

    fresh = 0

    for available_id in available_ids:

        for id_range in id_ranges:
            if available_id in id_range:
                fresh += 1
                break

    return fresh


def part_2(parsed_input):
    id_ranges, _ = parsed_input

    id_ranges = merge_ranges(id_ranges)

    ranges = [range(a, b + 1) for a, b in id_ranges]
    return sum(len(r) for r in ranges)


def merge_ranges(ranges):
    """
    Inclusive ranges in, converted to default python ranges and then converted back on way out

    >>> merge_ranges([(3, 5), (10, 14), (16, 20), (12, 18)])
    [(3, 5), (10, 20)]
    >>> merge_ranges([(4, 5), (1, 14), (16, 20), (12, 18)])
    [(1, 20)]
    """
    ranges = sorted(ranges)
    ranges = [range(low, high + 1) for low, high in ranges]

    a_idx = 0
    b_idx = 1
    starting = list(ranges)
    while True:
        print(ranges)
        try:
            a, b = ranges[a_idx], ranges[b_idx]
        except IndexError:
            if all(s == r for s, r in zip(starting, ranges)):
                break
            ranges = sorted(ranges, key=lambda r: r.start)
            starting = list(ranges)
            a_idx = 0
            b_idx = 1
            continue

        a_low, a_high = a.start, a.stop - 1
        b_low, b_high = b.start, b.stop - 1

        if a_low in b and a_high in b:
            ranges.pop(a_idx)
            continue

        elif a_low not in b and a_high in b:
            ranges[a_idx] = range(a_low, b.stop)
            ranges.pop(b_idx)
            continue

        elif b_low in a and b_high in a:
            ranges.pop(b_idx)
            continue

        else:
            a_idx += 1
            b_idx += 1

    return [(r.start, r.stop - 1) for r in ranges]


if __name__ == "__main__":
    part_2(([(3, 5), (10, 14), (16, 20), (12, 18)], [1, 5, 8, 11, 17, 32]))
