from common import main

DAY = 21
YEAR = 2023
SAMPLE = """\
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def parse(puzzle_input):
    lines = puzzle_input.splitlines()

    shape = (len(lines[0]), len(lines))

    rocks = set()
    garden_plots = set()
    start = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                rocks.add((x, y))
            elif char == ".":
                garden_plots.add((x, y))
            elif char == "S":
                garden_plots.add((x, y))
                start = (x, y)

    return garden_plots, start, shape


def part1(parsed_input):
    garden_plots, start, _ = parsed_input
    return len(simulate_steps(garden_plots, start, 64))


def part2(parsed_input):
    # So many off by one errors!
    NUMBER_OF_STEPS = 26_501_365
    garden_plots, start, shape = parsed_input
    assert shape[0] == shape[1], "square"
    size = shape[0]
    steps_to_edge = size // 2
    remaining_steps = NUMBER_OF_STEPS - steps_to_edge
    grids_from_center = remaining_steps / size
    assert grids_from_center % 2 == 0, "even number of grids from center"
    assert NUMBER_OF_STEPS % 2 != 0, "odd number of steps"

    # Start locations
    st_n = (size // 2, 0)
    st_ne = (size, 0)
    st_e = (size, size // 2)
    st_se = (size - 1, size - 1)
    st_s = (size // 2, size)
    st_sw = (0, size)
    st_w = (0, size // 2)
    st_nw = (0, 0)

    # Worked out quadratic of this by hand by drawing out grids
    total_full_odd_squares = grids_from_center**2 - grids_from_center * 2 + 1
    total_full_even_squares = grids_from_center**2
    small_wedges = grids_from_center * 4
    large_wedges = (grids_from_center - 1) * 4

    full_even_square = len(simulate_steps(garden_plots, start, size + 1))
    full_odd_square = len(simulate_steps(garden_plots, start, size))

    n_corner = len(simulate_steps(garden_plots, st_s, size))
    s_corner = len(simulate_steps(garden_plots, st_n, size - 1))
    w_corner = len(simulate_steps(garden_plots, st_e, size))
    e_corner = len(simulate_steps(garden_plots, st_w, size - 1))

    nw_sm_wedge = len(simulate_steps(garden_plots, st_se, size // 2 - 1))
    ne_sm_wedge = len(simulate_steps(garden_plots, st_sw, size // 2))
    sw_sm_wedge = len(simulate_steps(garden_plots, st_ne, size // 2))
    se_sm_wedge = len(simulate_steps(garden_plots, st_nw, size // 2 - 1))

    nw_lg_wedge = len(simulate_steps(garden_plots, st_se, (size // 2) * 3))
    ne_lg_wedge = len(simulate_steps(garden_plots, st_sw, (size // 2) * 3 + 1))
    sw_lg_wedge = len(simulate_steps(garden_plots, st_ne, (size // 2) * 3 + 1))
    se_lg_wedge = len(simulate_steps(garden_plots, st_nw, (size // 2) * 3))

    return (
        total_full_even_squares * full_even_square
        + total_full_odd_squares * full_odd_square
        + n_corner
        + s_corner
        + w_corner
        + e_corner
        + (small_wedges / 4) * nw_sm_wedge
        + (small_wedges / 4) * ne_sm_wedge
        + (small_wedges / 4) * sw_sm_wedge
        + (small_wedges / 4) * se_sm_wedge
        + (large_wedges / 4) * nw_lg_wedge
        + (large_wedges / 4) * ne_lg_wedge
        + (large_wedges / 4) * sw_lg_wedge
        + (large_wedges / 4) * se_lg_wedge
    )


def simulate_steps(garden, start, steps):
    positions = {start}

    for _ in range(steps):
        positions = set(
            c_p
            for pos in positions
            for c_p in get_cardinals(*pos)
            if c_p in garden
        )
    return positions


def get_cardinals(x, y):
    return [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]


def visualize_garden(garden, positions, shape):
    output = []
    for y in range(shape[1]):
        output.append("\n")
        for x in range(shape[0]):
            if x == shape[0] // 2 or y == shape[0] // 2:
                output.append("X")  # invaluable to correct off by one errors
            elif (x, y) in positions:
                output.append("O")
            elif (x, y) in garden:
                output.append(".")
            else:
                output.append("#")

    print("".join(output[1:]))


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
