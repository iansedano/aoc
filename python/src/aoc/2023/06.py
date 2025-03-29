import math

from common import main

DAY = 6
YEAR = 2023
SAMPLE = """\
Time:      7  15   30
Distance:  9  40  200"""


def parse(puzzle_input):
    time, distance = (line.split() for line in puzzle_input.splitlines())
    return [tuple(int(i) for i in pair) for pair in zip(time[1:], distance[1:])]


def part1(parsed_input):
    return math.prod(
        get_winning_times(time_limit, distance)
        for time_limit, distance in parsed_input
    )


def part2(parsed_input):
    time_limit = int("".join(str(t) for t, _ in parsed_input))
    record_distance = int("".join(str(d) for _, d in parsed_input))
    return get_winning_times(time_limit, record_distance)


def get_winning_times_brute_force(time_limit, record_distance):
    winning_times = 0
    time_pressing_button = 1

    while time_pressing_button < time_limit - 1:
        time_left = time_limit - time_pressing_button
        distance = time_pressing_button * time_left
        if distance > record_distance:
            winning_times += 1
        time_pressing_button += 1

    return winning_times


def get_winning_times(time_limit, record_distance):
    """
    >>> get_winning_times(7, 9)
    4
    >>> get_winning_times(15, 40)
    8
    >>> get_winning_times(30, 200)
    9
    >>> get_winning_times(71530, 940200)
    71503
    """
    time_pressing_button = 1

    start_win_time, end_win_time = 0, 0

    while time_pressing_button < time_limit - 1:
        time_left = time_limit - time_pressing_button
        distance = time_pressing_button * time_left
        if distance > record_distance:
            start_win_time = time_pressing_button
            break
        time_pressing_button += 1

    time_pressing_button = time_limit - 1

    while time_pressing_button > start_win_time:
        time_left = time_limit - time_pressing_button
        distance = time_pressing_button * time_left
        if distance > record_distance:
            end_win_time = time_pressing_button
            break
        time_pressing_button -= 1

    return end_win_time - start_win_time + 1


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
