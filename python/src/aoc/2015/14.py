from collections import defaultdict
from dataclasses import dataclass
from typing import NamedTuple

from common import main
from parse import compile

DAY = 14
YEAR = 2015
SAMPLE = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

pattern = compile(
    "{reindeer} can fly {speed:d} km/s for {fly_time:d} seconds, but then must rest for {rest_time:d} seconds."
)


class DeerStats(NamedTuple):
    speed: int
    fly_time: int
    rest_time: int


@dataclass
class DeerStatus:
    is_resting: bool = False
    time_flown: int = 0
    time_rested: int = 0
    distance: int = 0


def parse(puzzle_input):
    return build_speed_map(
        [
            tuple(pattern.parse(line).named.values())
            for line in puzzle_input.splitlines()
        ]
    )


def build_speed_map(input):
    return {deer: DeerStats(*stats) for deer, *stats in input}


def increment_deer(deer, deer_stats):
    if not deer.is_resting:
        if deer.time_flown == deer_stats.fly_time:
            deer.is_resting = True
            deer.time_rested = 1
        else:
            deer.distance += deer_stats.speed
            deer.time_flown += 1
        return deer

    if deer.time_rested == deer_stats.rest_time:
        deer.is_resting = False
        deer.time_flown = 1
        deer.distance += deer_stats.speed

    else:
        deer.time_rested += 1

    return deer


def part1(stats):
    status = defaultdict(DeerStatus)

    for _ in range(2503):
        for deer in stats.keys():
            status[deer] = increment_deer(status[deer], stats[deer])

    return max(deer.distance for deer in status.values())


def part2(stats):
    status = defaultdict(DeerStatus)

    deer_points = defaultdict(int)

    for _ in range(2503):
        for deer in stats.keys():
            status[deer] = increment_deer(status[deer], stats[deer])

        top_deer = sorted(status.items(), key=lambda d: d[1].distance, reverse=True)[0][
            0
        ]
        deer_points[top_deer] += 1

    return max(deer_points.values())


main(DAY, YEAR, SAMPLE, parse, part1, part2)
