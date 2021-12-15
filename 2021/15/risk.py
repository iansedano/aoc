from debug import p
from pprint import pp


def find_path(risk_map):
    w = len(risk_map) - 1
    h = len(risk_map[0]) - 1
    current_pos = (0, 0)
    queue = []

    costs = {}
    visited_set = set()

    for i in range(w + 1):
        for j in range(h + 1):
            costs[(i, j)] = float("inf")

    cardinals = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def get_possible_weighted_positions(pos):
        paths = []

        for c in cardinals:
            new_pos = (c[0] + pos[0], c[1] + pos[1])
            if (
                new_pos[0] <= w
                and new_pos[0] >= 0
                and new_pos[1] <= h
                and new_pos[1] >= 0
            ):
                weighted_pos = (
                    new_pos[0],
                    new_pos[1],
                    risk_map[new_pos[0]][new_pos[1]],
                )
                paths.append(weighted_pos)

        return paths

    costs[current_pos] = 0
    queue.append(current_pos)

    while len(queue) > 0:
        current_pos = queue.pop(0)

        next_possible_weighted_positions = get_possible_weighted_positions(current_pos)

        for w_pos in next_possible_weighted_positions:
            weight = w_pos[2]
            n_pos = tuple(w_pos[:2])
            if costs[current_pos] + weight < costs[n_pos]:
                costs[n_pos] = costs[current_pos] + weight
                queue.append(n_pos)
            if n_pos not in queue and n_pos not in visited_set:
                queue.append(n_pos)

        visited_set.add(current_pos)

    return costs
    return costs[(w, h)]


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
