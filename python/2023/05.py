from common import main

DAY = 5
YEAR = 2023
SAMPLE = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

"""
destination source range
"""


def parse(puzzle_input):
    """
    sample line: `50 98 2`
    destination source range
    """
    seeds, *almanac = puzzle_input.split("\n\n")
    seeds = [int(s) for s in seeds.split()[1:]]

    almanac = [
        [
            tuple(int(i) for i in m.split())  # (destination, source, range)
            for m in m.splitlines()[1:]  # strip heading
        ]
        for m in almanac
    ]

    almanac = [
        [(src, src + rng, dst - src) for dst, src, rng in m] for m in almanac
    ]

    return seeds, almanac


def part1(parsed_input):
    seeds, almanac = parsed_input
    seeds = [(seed, seed + 1) for seed in seeds]
    seeds = find_seed_locations(seeds, almanac)
    return min(r[0] for r in seeds)


def part2(parsed_input):
    seeds, almanac = parsed_input
    seeds = [(pair[0], sum(pair)) for pair in zip(seeds[::2], seeds[1::2])]
    seeds = find_seed_locations(seeds, almanac)
    return min(r[0] for r in seeds)


def find_seed_locations(seed_ranges, almanac):
    for transform_ranges in almanac:
        seed_ranges = [
            new_range
            for seed_range in seed_ranges
            for new_range in apply_transform(*seed_range, transform_ranges)
        ]
    return seed_ranges


def apply_transform(seed_start, seed_stop, transform_ranges):
    """With help from @gahjelle"""
    if seed_stop <= seed_start:
        return []

    for t_start, t_stop, offset in transform_ranges:
        if t_start >= seed_stop or t_stop <= seed_start:
            continue

        left = seed_start, max(t_start, seed_start)  # Can be nothing
        middle = max(t_start, seed_start), min(t_stop, seed_stop)
        right = min(t_stop, seed_stop), seed_stop  # Can be nothing

        return (
            apply_transform(*left, transform_ranges)
            + [(middle[0] + offset, middle[1] + offset)]
            + apply_transform(*right, transform_ranges)
        )

    return [(seed_start, seed_stop)]


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
