import itertools
import random
import sys
from collections import defaultdict, deque
from pprint import pp

from common import main

DAY = 25
YEAR = 2023
SAMPLE = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""


def parse(puzzle_input):
    lines = puzzle_input.splitlines()

    apparatus = defaultdict(set)
    connections = set()

    for line in lines:
        src, *dst = line.replace(":", "").split()

        for d in dst:
            apparatus[src].add(d)
            apparatus[d].add(src)
            connections.add((src, d))

    return apparatus, connections


"""
hfx/pzl
bvb/cmg
nvd/jqt

 ('xrd', 28),
 ('qhf', 34),
 
 ('mtl', 51),
 ('pgl', 54),
 ('scf', 76),
 ('lkf', 76)
 
 zxb
 zkv
"""


def part1(parsed_input):
    apparatus, connections = parsed_input

    nodes = list(apparatus.keys())
    # popular_nodes = defaultdict(int)
    # for _ in range(1000):
    #     print(_)
    #     choice = set(random.choices(nodes, k=2))
    #     if len(choice) != 2:
    #         continue
    #     path = get_path(*choice, apparatus)
    #     for node in path:
    #         popular_nodes[node] += 1

    # six_nodes = sorted(popular_nodes.items(), key=lambda x: x[1], reverse=True)[
    #     :6
    # ]

    six_nodes = ["zxb", "zkv", "mtl", "pgl", "scf", "lkf"]
    print(six_nodes)

    for node in six_nodes:
        apparatus[node] = apparatus[node] - set(six_nodes)

    random_start = random.choice(nodes)
    nodes_in_one = {random_start}

    sys.setrecursionlimit(5000)

    def get_paths(node):
        for item in apparatus[node]:
            if item not in nodes_in_one:
                yield item
                yield from get_paths(item)

    for item in get_paths(random_start):
        nodes_in_one.add(item)

    return len(nodes_in_one) * (len(nodes) - len(nodes_in_one))


def part2(parsed_input):
    return


def get_size_of_group(graph):
    q = deque()


def get_path(start, end, graph):
    q = deque()
    for item in graph[start]:
        q.append((start, item))

    while q:
        path = q.popleft()
        if path[-1] == end:
            return path
        for item in graph[path[-1]]:
            if item not in path:
                q.append(path + (item,))


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
