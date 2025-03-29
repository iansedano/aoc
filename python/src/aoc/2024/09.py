from textwrap import dedent

from aocd import get_data

DAY = 9
YEAR = 2024
SAMPLE = dedent(
    """\
    2333133121414131402"""
)


def parse(puzzle_input):
    return [int(char) for char in puzzle_input]


def part_1(parsed_input):

    disk = write_disk(parsed_input)

    start = 0
    end = len(disk) - 1

    while start < end:
        if disk[start] is not None:
            start += 1
            continue

        if disk[end] is None:
            end -= 1
            continue

        disk[start] = disk[end]
        disk[end] = None
        start += 1
        end -= 1

    return checksum(disk)


def part_2(parsed_input):
    disk = write_summarized_disk(parsed_input)

    start = 0
    end = len(disk) - 1

    while True:

        start_disk = disk

        while start < end:
            start_id, start_len = disk[start]
            end_id, end_len = disk[end]

            if start_id is not None:
                start += 1
                continue

            if end_id is None:
                end -= 1
                continue

            if start_len >= end_len:
                remaining = start_len - end_len
                disk[start] = (end_id, end_len)
                disk[end] = (None, end_len)
                end -= 1

                if remaining:
                    disk.insert(start + 1, (None, remaining))

                disk = normalize_summarized(disk)

                start = 0
                continue

            if start_len < end_len:
                start += 1
                continue

        if disk == start_disk and end == 1:
            break
        else:
            start = 0
            end -= 1

    return checksum(expand_summarized_disk(disk))


def normalize_summarized(disk):

    output = list(disk)

    for _ in range(2):
        normalized = []
        i = 0

        while i < len(output) - 1:
            if output[i][0] == output[i + 1][0]:
                normalized.append(
                    (output[i][0], output[i][1] + output[i + 1][1])
                )
                i += 2
            else:
                normalized.append(output[i])
                i += 1

        if i == len(output) - 1:
            normalized.append(output[i])

        output = list(normalized)

    return output


def checksum(seq):
    """
    >>> checksum([int(c) for c in '0099811188827773336446555566'])
    1928
    """
    return sum(i * val for i, val in enumerate(seq) if val is not None)


def write_disk(disk_map):
    disk = []
    file_id = 0
    blank = False
    for n in disk_map:
        for _ in range(n):
            if not blank:
                disk.append(file_id)
            else:
                disk.append(None)

        if not blank:
            file_id += 1
        blank = not blank

    return disk


def write_summarized_disk(disk_map):
    summarized_disk = []
    file_id = 0
    blank = False

    for n in disk_map:
        if not blank:
            summarized_disk.append((file_id, n))
        else:
            summarized_disk.append((None, n))

        if not blank:
            file_id += 1
        blank = not blank
    return summarized_disk


def expand_summarized_disk(summarized_disk):
    disk = []
    for id, length in summarized_disk:
        for _ in range(length):
            disk.append(id)

    return disk


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).strip()
    parsed = parse(SAMPLE)
    print(f"Part 1: {part_1(parsed)}")
    print(f"Part 2: {part_2(parsed)}")
