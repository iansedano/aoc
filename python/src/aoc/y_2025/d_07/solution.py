from collections import defaultdict
from pprint import pprint


def parse(puzzle_input):

    lines = puzzle_input.splitlines()
    start = (lines[0].index("S"), 0)
    splitters = set()

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "^":
                splitters.add((x, y))

    return start, splitters, len(lines)


def part_1(parsed_input):
    start, splitters, length = parsed_input
    beam = {(start[0], start[1] + 1)}
    splits = 0

    for _ in range(length):
        new_beam = set()

        for b in beam:
            p = (b[0], b[1] + 1)
            if p in splitters:
                splits += 1
                new_beam.add((p[0] - 1, p[1]))
                new_beam.add((p[0] + 1, p[1]))
            else:
                new_beam.add(p)

        beam = new_beam

    return splits


def part_2(parsed_input):
    start, splitters, length = parsed_input

    # Build Graph

    graph = defaultdict(set)
    graph[start]
    beam = {start}

    for _ in range(length):
        new_beam = set()
        for b in beam:
            p = (b[0], b[1] + 1)

            if p in splitters:
                left, right = (p[0] - 1, p[1]), (p[0] + 1, p[1])
                new_beam.add(left)
                new_beam.add(right)
                graph[b].add(left)
                graph[b].add(right)

            else:
                new_beam.add(p)
                graph[b].add(p)

        beam = new_beam

    end = (0, float("inf"))
    graph[end]
    for b in beam:
        graph[b].add(end)

    # DP

    reverse_topological = reversed(sorted(graph.keys(), key=lambda x: x[1]))

    table = {}

    for node in reverse_topological:
        if node == end:
            table[node] = 1
            continue

        table[node] = sum(table[path] for path in graph[node])

    return table[start]


if __name__ == "__main__":
    part_2(
        (
            (7, 0),
            {
                (6, 12),
                (3, 10),
                (5, 10),
                (9, 14),
                (13, 14),
                (6, 8),
                (12, 12),
                (5, 6),
                (4, 8),
                (9, 10),
                (11, 10),
                (10, 8),
                (1, 14),
                (6, 4),
                (7, 6),
                (3, 14),
                (8, 4),
                (5, 14),
                (9, 6),
                (2, 12),
                (7, 2),
                (7, 14),
            },
            16,
        )
    )
    # from aocd import get_data

    # parsed = parse(get_data(day=7, year=2025))
    # print(part_2(parsed))
