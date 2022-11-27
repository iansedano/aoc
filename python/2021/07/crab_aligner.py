from collections import Counter

# from functools import cache
from debug import p

"""
Counter returns (position, frequency)
"""

Crabs = tuple[int, int]  # position, frequency


def align_crabs(h_positions: list[int]):
    print("----------")
    counts = Counter(h_positions)

    highest_freq = counts.most_common(1)[0][1]
    p(highest_freq)
    most_common = []

    for c in counts.most_common():
        if c[1] >= highest_freq - 50:
            most_common.append(c)
        else:
            break

    most_common_range = range(
        min([crab[0] for crab in most_common]),
        max([crab[0] for crab in most_common]) + 1,
    )

    grid = [[0 for _ in most_common_range] for crabs in counts.items()]

    crabs: Crabs
    for i, crabs in enumerate(counts.items()):
        for j, loc in enumerate(most_common_range):
            grid[i][j] = abs(crabs[0] - loc) * crabs[1]

    sums = [0 for _ in most_common_range]

    for row in grid:
        for i, value in enumerate(row):
            sums[i] += value

    return min(sums)


# @cache
def calc_fuel_cost(distance):
    # if distance == 0:
    #     return 0
    # elif distance == 1:
    #     return 1

    # return distance + calc_fuel_cost(distance - 1)

    return (distance * (distance + 1)) / 2


# def warm_up_calc():
#     calc_fuel_cost(10)
#     calc_fuel_cost(20)
#     calc_fuel_cost(500)
#     calc_fuel_cost(800)
#     calc_fuel_cost(1000)


def align_crabs_new_cost(h_positions: list[int]):
    print("----------")
    counts = Counter(h_positions)

    highest_freq = counts.most_common(1)[0][1]
    p(highest_freq)
    most_common = []

    for c in counts.most_common():
        if c[1] >= highest_freq - 50:
            most_common.append(c)
        else:
            break

    most_common_range = range(
        min([crab[0] for crab in most_common]),
        max([crab[0] for crab in most_common]) + 1,
    )

    grid = [[0 for _ in most_common_range] for crabs in counts.items()]

    # warm_up_calc()
    crabs: Crabs
    for i, crabs in enumerate(counts.items()):
        for j, loc in enumerate(most_common_range):
            distance = abs(crabs[0] - loc)
            grid[i][j] = calc_fuel_cost(distance) * crabs[1]

    sums = [0 for _ in most_common_range]

    for row in grid:
        for i, value in enumerate(row):
            sums[i] += value

    return min(sums)
