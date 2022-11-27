from debug import p
from pprint import pp
import heapq
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Position = namedtuple("Position", ["cost", "point"])


def find_path(risk_map):
    w = len(risk_map) - 1
    h = len(risk_map[0]) - 1
    current_pos = Position(0, Point(0, 0))
    queue = []
    heapq.heapify(queue)

    costs: dict[Point:int] = {}
    visited_set: set[Position] = set()

    for i in range(w + 1):
        for j in range(h + 1):
            costs[Point(i, j)] = float("inf")
    costs[Point(0, 0)] = 0
    cardinals = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]

    def get_possible_positions(pos):
        paths = []

        for c in cardinals:
            new_point = Point(c[0] + pos[0], c[1] + pos[1])
            if (
                new_point[0] <= w
                and new_point[0] >= 0
                and new_point[1] <= h
                and new_point[1] >= 0
            ):
                weighted_pos = Position(risk_map[new_point.x][new_point.y], new_point)
                paths.append(weighted_pos)

        return sorted(paths, key=lambda p: p.cost)

    heapq.heappush(queue, current_pos)

    while len(queue) > 0:
        current_pos = heapq.heappop(queue)

        next_possible_positions = get_possible_positions(current_pos.point)

        for possible_pos in next_possible_positions:
            if possible_pos.point not in visited_set:

                if current_pos.cost + possible_pos.cost < costs[possible_pos.point]:
                    costs[possible_pos.point] = (
                        costs[current_pos.point] + possible_pos.cost
                    )

                skip = False
                for candidate in queue:
                    if candidate.point == possible_pos.point:
                        if candidate.cost > possible_pos.cost:
                            candidate.cost = possible_pos.cost
                        skip = True

                if skip == False:
                    heapq.heappush(queue, possible_pos)

        visited_set.add(current_pos.point)
    print(costs[Point(w, h)])
    return costs[Point(w, h)]


def print_iter_of_pos(iter, risk_map):
    mark = "#"

    grid = [l.copy() for l in risk_map.copy()]

    for p in iter:
        grid[p[0]][p[1]] = mark
    print("\n")
    representation = [[str(d) for d in l] for l in grid]
    pp(["".join(l) for l in representation])


def build_cave(risk_map):
    w = len(risk_map)
    h = len(risk_map[0])

    final_cave = []

    for row in risk_map:
        final_row = []
        final_row.extend([val for val in row])
        for i in range(1, 5):
            incremented_row = []
            for val in row:
                if (val + i) > 9:
                    incremented_row.append(((val + i) % 10) + 1)
                else:
                    incremented_row.append(val + i)
            final_row.extend(incremented_row)
        final_cave.append(final_row)

    for i in range(4 * h):
        incremented_row = []
        for val in final_cave[i]:
            if (val + 1) > 9:
                incremented_row.append(((val + 1) % 10) + 1)
            else:
                incremented_row.append(val + 1)

        final_cave.append(incremented_row)

    return final_cave
