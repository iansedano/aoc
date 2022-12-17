from pprint import pp

import cave_input
from debug import p

EX_01 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

EX_02 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

EX_03 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def test_part1():
    nodes = cave_input.parse_caves(EX_01)
    routes = cave_input.get_routes(nodes["start"], nodes["end"])
    assert len(routes) == 10

    nodes = cave_input.parse_caves(EX_02)
    routes = cave_input.get_routes(nodes["start"], nodes["end"])
    assert len(routes) == 19

    nodes = cave_input.parse_caves(EX_03)
    routes = cave_input.get_routes(nodes["start"], nodes["end"])
    assert len(routes) == 226

    nodes = cave_input.parse_caves()
    routes = cave_input.get_routes(nodes["start"], nodes["end"])
    assert len(routes) == 4775


test_part1()


def test_part2():
    nodes = cave_input.parse_caves(EX_01)
    routes = cave_input.get_routes2(nodes["start"], nodes["end"])
    assert len(routes) == 36

    nodes = cave_input.parse_caves(EX_02)
    routes = cave_input.get_routes2(nodes["start"], nodes["end"])
    assert len(routes) == 103

    nodes = cave_input.parse_caves(EX_03)
    routes = cave_input.get_routes2(nodes["start"], nodes["end"])
    assert len(routes) == 3509

    nodes = cave_input.parse_caves()
    routes = cave_input.get_routes2(nodes["start"], nodes["end"])
    print(len(routes))


test_part2()
