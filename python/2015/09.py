from collections import defaultdict
from itertools import permutations
from pprint import pp as print

from common import main

DAY = 9
YEAR = 2015
SAMPLE = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""


def parse(puzzle_input: str):
    return [
        (
            tuple(location.strip() for location in locations.strip().split("to")),
            int(distance.strip()),
        )
        for line in puzzle_input.strip().splitlines()
        for locations, distance in [line.split("=")]
    ]


def make_graph(input):
    graph = defaultdict(lambda: defaultdict(int))

    for (a, b), distance in input:
        graph[a][b] = distance
        graph[b][a] = distance

    return graph


def generate_permutations(cities):
    return [
        [city, *perm]
        for city in cities
        for perm in permutations(set(cities.keys()) - {city})
    ]


def get_total_distance(graph, route):
    return sum(graph[a][b] for a, b in zip(route[:-1], route[1:]))


def part1(input):
    graph = make_graph(input)
    permutations = generate_permutations(graph)
    return min(get_total_distance(graph, perm) for perm in permutations)


def part2(input):
    graph = make_graph(input)
    permutations = generate_permutations(graph)
    return max(get_total_distance(graph, perm) for perm in permutations)


main(DAY, YEAR, SAMPLE, parse, part1, part2)
