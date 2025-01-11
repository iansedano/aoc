import main

sample_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_sample_cases():
    lines = sample_input.split("\n")
    assert main.part1(lines) == 198
    assert main.part2(lines) == 230
