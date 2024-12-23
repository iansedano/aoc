import itertools
from pprint import pp

from aocd import get_data
from rich.console import Console
from rich.live import Live

console = Console()

SENSOR, BEACON, NO_BEACON = 0, 1, 2

SAMPLE = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def parse(puzzle_input: str):
    """Parse input."""

    return [
        [
            tuple(int(loc[2:]) for loc in pair.split(", "))
            for pair in line.strip("Sensor at ").split(
                ": closest beacon is at "
            )
        ]
        for line in puzzle_input.splitlines()
    ]


def manhattan(p1, p2):
    x = abs(p2[0] - p1[0])
    y = abs(p2[1] - p1[1])

    return x + y


def points_in_distance(origin, distance):
    """
    >>> points_in_distance((0,0), 1)
    [(0, -1), (1, 0), (0, 1), (-1, 0)]
    >>> points_in_distance((0,0), 3)
    [(0, -1), (1, 0), (0, 1), (-1, 0)]
    """

    o_x, o_y = origin

    points = []

    for y in range(-distance, distance + 1):
        sides = abs(abs(y) - distance)

        for x in range(-sides, sides + 1):
            if (x, y) == (0, 0):
                continue
            points.append((x + o_x, y + o_y))

    return points


def build_complete_grid(data):

    grid = {}
    sensors = []
    for pair in data:
        print(pair)
        sensor, beacon = pair

        distance = manhattan(sensor, beacon)
        print(distance)

        points_covered = [
            point
            for point in points_in_distance(sensor, distance)
            if point not in [beacon, sensor]
        ]

        sensors.append(
            {
                "origin": sensor,
                "beacon": beacon,
                "points_covered": points_covered,
            }
        )

        grid[sensor] = SENSOR
        grid[beacon] = BEACON

        for point in points_covered:
            grid[point] = NO_BEACON

    return grid


def part1(data):
    """Solve part 1."""
    sensors = [sensor for sensor, _ in data]
    beacons = {beacon for _, beacon in data}
    distances = [manhattan(sensor, beacon) for sensor, beacon in data]
    max_distance = max(distances)

    min_x = min(sensor[0] - max_distance for sensor in sensors)
    max_x = max(sensor[0] + max_distance for sensor in sensors)

    Y_ROW = 2_000_000
    # Y_ROW = 10

    squares_where_beacon_cant_be = 0
    for x in range(min_x, max_x):

        if any(
            manhattan((x, Y_ROW), sensor) <= distance
            and (x, Y_ROW) not in beacons
            for sensor, distance in zip(sensors, distances)
        ):
            squares_where_beacon_cant_be += 1

    return squares_where_beacon_cant_be


def get_sensor_coverage(sensor, distance, row_y):
    s_x, s_y = sensor
    if abs(s_y - row_y) > distance:
        return None
    side = abs(abs(s_y - row_y) - distance)
    return (s_x - side, s_x + side + 1)


def merge_ranges(ranges):
    ranges = sorted(ranges)

    non_overlapping = []

    for r in ranges:
        if non_overlapping and r[0] <= non_overlapping[-1][1]:
            non_overlapping[-1] = (
                min(r[0], non_overlapping[-1][0]),
                max(r[1], non_overlapping[-1][1]),
            )
        else:
            non_overlapping.append(r)

    return non_overlapping


def part2(data):
    """Solve part 2."""

    sensors = [sensor for sensor, _ in data]
    distances = [manhattan(sensor, beacon) for sensor, beacon in data]

    min_c = 0
    max_c = 4_000_000

    # min_c = 0
    # max_c = 20

    for row in range(min_c, max_c):
        if row % 100000 == 0:
            print(row)
        ranges = [
            get_sensor_coverage(sensor, distance, row)
            for sensor, distance in zip(sensors, distances)
        ]
        ranges = list(filter(lambda r: r is not None, ranges))
        rng_union = merge_ranges(ranges)

        if len(rng_union) > 1:
            return rng_union[0][1] * 4_000_000 + row


def viz(grid):

    min_x = min(key[0] for key in grid.keys() if key != "floor")
    min_y = min(key[1] for key in grid.keys() if key != "floor")
    max_x = max(key[0] for key in grid.keys() if key != "floor") + 1
    max_y = max(key[1] for key in grid.keys() if key != "floor") + 1

    # print(min_x, min_y, max_x, max_y)

    out = []

    for y in range(min_y, max_y):
        out.append(f"{y:3}")
        for x in range(min_x, max_x):
            item = grid.get((x, y))
            if item == SENSOR:
                out.append("[#C2B280]S[/]")
            elif item == BEACON:
                out.append("[#5A4D41 on #74663B]B[/]")
            elif item == NO_BEACON:
                out.append("#")
            else:
                out.append(".")
        out.append("\n")

    return "".join(out)


def main():
    puzzle_input = get_data(day=15, year=2022).strip()
    # puzzle_input = SAMPLE
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
