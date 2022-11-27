import octopus_input
import octopi_sim

from pprint import pp
from debug import p

SAMPLE_01 = """11111
19991
19191
19991
11111"""

"""34543
40004
50005
40004
34543

45654
51115
61116
51115
45654"""


SAMPLE_02 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

SAMPLE_02_100 = """0397666866
0749766918
0053976933
0004297822
0004229892
0053222877
0532222966
9322228966
7922286866
6789998766"""


def test_input():
    octopi = octopus_input.parse_octopi(SAMPLE_01)
    assert octopi == [
        [1, 1, 1, 1, 1],
        [1, 9, 9, 9, 1],
        [1, 9, 1, 9, 1],
        [1, 9, 9, 9, 1],
        [1, 1, 1, 1, 1],
    ]


test_input()


def test_sample_1_p1():
    octopi = octopus_input.parse_octopi(SAMPLE_01)

    assert octopi_sim.simulate(octopi, 2) == [
        [4, 5, 6, 5, 4],
        [5, 1, 1, 1, 5],
        [6, 1, 1, 1, 6],
        [5, 1, 1, 1, 5],
        [4, 5, 6, 5, 4],
    ]


test_sample_1_p1()


def test_sample_02_p1():
    octopi = octopus_input.parse_octopi(SAMPLE_02)
    end_state = octopus_input.parse_octopi(SAMPLE_02_100)

    assert octopi_sim.simulate(octopi, 100) == end_state


test_sample_02_p1()


def test_p1():
    octopi = octopus_input.parse_octopi()

    octopi_sim.simulate(octopi, 100)


test_p1()


def test_sample_02_p2():
    octopi = octopus_input.parse_octopi(SAMPLE_02)

    octopi_sim.simulate(octopi, 200)


test_sample_02_p2()


def test_02_p2():
    octopi = octopus_input.parse_octopi()

    octopi_sim.simulate(octopi, 500)


test_02_p2()
