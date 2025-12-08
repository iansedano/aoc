import collections
import itertools
import math
from pprint import pprint

import peek


def parse(puzzle_input):
    return [
        tuple(int(x) for x in line.split(","))
        for line in puzzle_input.splitlines()
    ]


def part_1(parsed_input):
    map = collections.defaultdict(dict)

    for a, b in itertools.product(parsed_input, repeat=2):
        if a == b:
            continue
        if a in map[b]:
            continue
        map[a][b] = distance(a, b)

    pairs = []

    for a in map.keys():
        for b, dist in map[a].items():
            pairs.append((a, b, dist))

    closest = sorted(pairs, key=lambda x: x[2])[0:1000]

    circuits = DisjointSet(parsed_input)

    for a, b, _ in closest:
        circuits.connect(a, b)

    top_three = circuits.get_top_three_circuits()

    return math.prod(t[1] for t in top_three)


def part_2(parsed_input):
    return


def distance(a, b):

    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2
    z = (a[2] - b[2]) ** 2

    return math.sqrt(x + y + z)


class DisjointSet:
    def __init__(self, iterable):
        self._parent = {i: (i, 1) for i in iterable}

    def _find(self, item):
        current = item

        chain = [current]
        while True:
            parent = self._parent[current][0]
            if parent == current:
                self._compress(chain, parent)
                return current

            chain.append(parent)
            current = parent

    def _compress(self, chain, parent):
        for c in chain:
            size = self._parent[c][1]
            self._parent[c] = (parent, size)

    def get_top_three_circuits(self):
        return list(
            reversed(sorted(self._parent.values(), key=lambda x: x[1]))
        )[0:3]

    def connect(self, a, b):
        parent_a = self._find(a)
        parent_b = self._find(b)

        if parent_a != parent_b:
            self._join(parent_a, parent_b)

    def _join(self, parent_a, parent_b):
        size_a, size_b = self._parent[parent_a][1], self._parent[parent_b][1]

        if size_a > size_b:
            self._parent[parent_b] = (parent_a, size_b)
            self._parent[parent_a] = (parent_a, size_a + size_b)
        else:
            self._parent[parent_a] = (parent_b, size_a)
            self._parent[parent_b] = (parent_b, size_a + size_b)


if __name__ == "__main__":

    # ds = DisjointSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    # ds.connect(1, 3)
    # ds.connect(6, 7)
    # ds.connect(1, 6)

    # print(ds._parent)

    part_1(
        [
            (162, 817, 812),
            (57, 618, 57),
            (906, 360, 560),
            (592, 479, 940),
            (352, 342, 300),
            (466, 668, 158),
            (542, 29, 236),
            (431, 825, 988),
            (739, 650, 466),
            (52, 470, 668),
            (216, 146, 977),
            (819, 987, 18),
            (117, 168, 530),
            (805, 96, 715),
            (346, 949, 466),
            (970, 615, 88),
            (941, 993, 340),
            (862, 61, 35),
            (984, 92, 344),
            (425, 690, 689),
        ]
    )
