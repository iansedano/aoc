from common import main
from parse import compile
from itertools import permutations
from collections import defaultdict

DAY = 13
YEAR = 2015
SAMPLE = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

pattern = compile(
    "{a} would {gain_lose} {happiness} happiness units by sitting next to {b}."
)


def parse(puzzle_input):
    return [
        tuple(pattern.parse(line).named.values()) for line in puzzle_input.splitlines()
    ]


def build_graph(input):
    graph = defaultdict(lambda: defaultdict(int))
    for a, dir, amount, b in input:
        graph[a][b] = int(amount) if dir == "gain" else -int(amount)
    return graph


def get_possible_plans(people: set):
    fixed_person = people.pop()
    plans = permutations(person for person in people if person != fixed_person)
    return [tuple([fixed_person, *plan]) for plan in plans]


def evaluate_plan(plan: tuple, graph):
    first = graph[plan[0]][plan[-1]]
    last = graph[plan[-1]][plan[0]]

    return (
        first
        + last
        + sum(
            graph[person][plan[i + 1]] + graph[plan[i + 1]][person]
            for i, person in enumerate(plan[:-1])
        )
    )


def part1(input):
    graph = build_graph(input)
    people = set(graph.keys())
    plans = get_possible_plans(people)
    return max(evaluate_plan(plan, graph) for plan in plans)


def part2(input):
    graph = build_graph(input)
    for person in list(graph.keys()):
        graph["me"][person] = 0
        graph[person]["me"] = 0
    people = set(graph.keys())
    arrangements = get_possible_plans(people)
    return max(evaluate_plan(a, graph) for a in arrangements)


main(DAY, YEAR, SAMPLE, parse, part1, part2)
