from collections import deque

from common import main

DAY = 23
YEAR = 2023
SAMPLE = """\
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def parse(puzzle_input):
    trails = {
        (x, y): char
        for y, line in enumerate(puzzle_input.splitlines())
        for x, char in enumerate(line)
        if char != "#"
    }

    start, stop = (None, float("inf")), (None, float("-inf"))
    for k in trails.keys():
        if k[1] < start[1]:
            start = k
        if k[1] > stop[1]:
            stop = k

    return trails, start, stop


SLOPES = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}


def build_graph(trails, start, stop, ignore_slopes=False):
    graph = {start: {}, stop: {}}
    paths_to_process = deque()
    paths_to_process.append((start, (0, 1)))
    paths_done = set()

    def next_steps_from(pos, direction):
        return [
            (direction, new_p)
            for direction in {(1, 0), (0, 1), (-1, 0), (0, -1)}
            - {inv_v(direction)}
            if (new_p := add_v(direction, pos)) in trails
        ]

    while paths_to_process:
        start_node, direction = paths_to_process.popleft()
        paths_done.add((start_node, direction))
        next_step = add_v(start_node, direction)
        one_way = False
        cost = 1
        cardinals = next_steps_from(next_step, direction)
        while len(cardinals) == 1 and next_step not in graph:
            if not ignore_slopes and (char := trails[next_step]) in SLOPES:
                if SLOPES[char] == direction:
                    one_way = True
                elif SLOPES[char] == inv_v(direction):
                    break
                else:
                    raise ValueError("Encountered dir that doesn't make sense")

            direction, next_step = cardinals[0]
            cost += 1
            cardinals = next_steps_from(next_step, direction)

        if not one_way and not ignore_slopes:
            continue

        if next_step not in graph:
            graph[next_step] = {}
        graph[start_node][next_step] = cost

        for direction, _ in cardinals:
            path_start = (next_step, direction)
            if (
                path_start not in paths_done
                and path_start not in paths_to_process
            ):
                paths_to_process.append((next_step, direction))

    return graph


def part1(parsed_input):
    trails, start, stop = parsed_input
    graph = build_graph(trails, start, stop)

    stack = deque()
    stack.append((0, start))
    highest_cost_to_stop = 0
    while stack:
        cost, node = stack.pop()
        if node == stop:
            highest_cost_to_stop = max(highest_cost_to_stop, cost)
            continue
        for next_pos, next_cost in graph[node].items():
            stack.append((next_cost + cost, next_pos))

    return highest_cost_to_stop


def part2(parsed_input):
    trails, start, stop = parsed_input
    graph = build_graph(trails, start, stop, ignore_slopes=True)

    stack = deque()
    stack.append((0, start, {start}))
    max_cost_for_stop = 0
    while stack:
        cost, current, path = stack.pop()

        if current == stop:
            max_cost_for_stop = max(max_cost_for_stop, cost)
            continue

        for next_pos, next_cost in graph[current].items():
            if next_pos not in path:
                stack.append((next_cost + cost, next_pos, path | {next_pos}))

    return max_cost_for_stop


def add_v(a, b):
    return (a[0] + b[0], a[1] + b[1])


def inv_v(a):
    return (-a[0], -a[1])


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
