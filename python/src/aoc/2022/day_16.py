import collections
import itertools
from pprint import pp
from typing import Any

import networkx as nx
from aocd import get_data
from pyvis.network import Network

# from dataclasses import Dataclass, field

SAMPLE = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


Valve = collections.namedtuple("Valve", ["rate", "leads_to"])


def main():
    puzzle_input = get_data(day=16, year=2022).strip()
    # puzzle_input = SAMPLE
    data = parse(puzzle_input)
    print(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def part1(data):
    """Solve part 1."""
    return get_instructions_to_save_elephants(data, "AA", 30)


def part2(data):
    """Solve part 2."""
    return get_instructions_to_save_elephants_with_helper(data, "AA", 26)
    # 2561 too low


def parse(puzzle_input: str):
    """Parse input."""

    lines = [line.split() for line in puzzle_input.splitlines()]
    # ['Valve', 'CG', 'has', 'flow', 'rate=10;', 'tunnels', 'lead', 'to', 'valves', 'TI,', 'SU,', 'RV,', 'FF,', 'QX'],
    valves = [line[1] for line in lines]
    rate = [int(line[4].strip(";").split("=")[-1]) for line in lines]
    leads_to = [tuple(name.strip(",") for name in line[9:]) for line in lines]

    # build_networkx_graph(
    #     {
    #         valve: Valve(rate, leads_to)
    #         for valve, rate, leads_to in zip(valves, rate, leads_to)
    #     }
    # )

    return build_graph(
        {
            valve: Valve(rate, leads_to)
            for valve, rate, leads_to in zip(valves, rate, leads_to)
        }
    )


def build_networkx_graph(valve_dict):

    G = nx.Graph()

    for name, valve in valve_dict.items():
        G.add_node(name, size=(valve.rate + 1) * 1.5, label=name)
        for n in valve.leads_to:
            G.add_edge(name, n)

    net = Network("2000px", "2000px")
    net.from_nx(G)
    net.save_graph("nx.html")


def build_graph(valve_dict):

    return {
        name: {"rate": valve.rate, "distances": get_distances(name, valve_dict)}
        for name, valve in valve_dict.items()
    }


def get_distances(start_name, valve_dict):
    distances = {start_name: 0}
    distance = 1
    nodes_to_explore = [
        (name, distance) for name in valve_dict[start_name].leads_to
    ]

    while nodes_to_explore:
        name, distance = nodes_to_explore.pop(0)

        if distances.get(name, float("-inf")) < distance:
            distances[name] = distance

        valve = valve_dict.get(name)

        nodes_to_explore.extend(
            (name, distance + 1)
            for name in valve.leads_to
            if name not in distances.keys()
        )

    del distances[start_name]

    return {
        name: distance
        for name, distance in distances.items()
        if valve_dict.get(name).rate != 0
    }


highest_score = 0


def get_instructions_to_save_elephants(graph, start_key, time_left):
    def helper(path, time_left, score, valves_opened):

        if time_left < 2:
            return (score, path)

        potential_moves = sorted(
            find_potential_moves(graph, path[-1], time_left, valves_opened),
            key=lambda m: m[1],
            reverse=True,
        )

        if not potential_moves:
            return (score, path)

        paths = []
        for target, points, cost in potential_moves:

            paths.append(
                helper(
                    path + (target,),
                    time_left - cost,
                    score + points,
                    valves_opened + (target,),
                )
            )
        global highest_score
        best = sorted(paths, reverse=True)[0]

        if best[0] > highest_score:
            highest_score = best[0]
            print(best)
        return sorted(paths, reverse=True)[0]

    valves_opened = tuple(
        name for name, valve in graph.items() if valve["rate"] == 0
    )

    best_path = helper(
        path=(start_key,),
        time_left=time_left,
        score=0,
        valves_opened=valves_opened,
    )

    return best_path


NO_MOVE = (None, 0, 0)


def get_move_combinations(pm1, pm2):

    pm1 = pm1 or (NO_MOVE,)
    pm2 = pm2 or (NO_MOVE,)

    if pm1 == (NO_MOVE,) and pm2 == (NO_MOVE,):
        return []

    move_combos = [
        (m1, m2) for m1, m2 in itertools.product(pm1, pm2) if m1[0] != m2[0]
    ]

    return sorted(
        move_combos,
        key=lambda mvs: mvs[0][1] + mvs[1][1],
        reverse=True,
    )


def get_instructions_to_save_elephants_with_helper(graph, start_key, time_left):
    def helper(path, time_left, score, valves_opened):

        # potential moves
        pm1 = sorted(
            find_potential_moves(
                graph, path[-1][0], time_left[0], valves_opened
            ),
            key=lambda m: m[1],
            reverse=True,
        )
        pm2 = sorted(
            find_potential_moves(
                graph, path[-1][1], time_left[1], valves_opened
            ),
            key=lambda m: m[1],
            reverse=True,
        )

        move_combinations = get_move_combinations(pm1, pm2)

        if not move_combinations:
            return (score, path)

        paths = []
        for m1, m2 in move_combinations:
            t1, p1, c1 = m1
            t2, p2, c2 = m2

            paths.append(
                helper(
                    path + ((t1, t2),),
                    (time_left[0] - c1, time_left[1] - c2),
                    score + p1 + p2,
                    valves_opened + (t1, t2),
                )
            )
        global highest_score
        best = sorted(paths, reverse=True)[0]

        if best[0] > highest_score:
            highest_score = best[0]
            print(best)
        return sorted(paths, reverse=True)[0]

    valves_opened = tuple(
        name for name, valve in graph.items() if valve["rate"] == 0
    )

    best_path = helper(
        path=((start_key, start_key),),
        time_left=(time_left, time_left),
        score=0,
        valves_opened=valves_opened,
    )

    return best_path


def find_potential_moves(graph, start_key, time_left, valves_opened):
    if not start_key:
        return [NO_MOVE]
    potential_moves = []

    for potential_target, distance_to_target in graph[start_key][
        "distances"
    ].items():

        rate = graph[potential_target]["rate"]
        time_cost = distance_to_target + 1
        potential_pressure_release = rate * (time_left - time_cost)
        if potential_pressure_release > 0:
            potential_moves.append(
                (potential_target, potential_pressure_release, time_cost)
            )

    return [move for move in potential_moves if move[0] not in valves_opened]


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
