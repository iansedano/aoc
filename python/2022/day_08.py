from aocd import get_data


def parse(puzzle_input):
    """Parse puzzle input into a dictionary representing a grid"""
    rows = [
        [int(tree) for tree in list(line)] for line in puzzle_input.splitlines()
    ]
    width = len(rows[0])
    height = len(rows)

    grid = {}
    for y, col in enumerate(rows):
        for x, cell in enumerate(col):
            grid[(x, y)] = cell

    return grid, height, width


def is_visible(x, y, grid, max_width, max_height):
    """Determine if tree is visible from outside"""

    height = grid[(x, y)]

    if x in (0, max_width - 1) or y in (0, max_height - 1):
        return True

    directions_hidden = 0

    for i in range(x - 1, -1, -1):
        if grid[i, y] >= height:
            directions_hidden += 1
            break
    for i in range(x + 1, max_width):
        if grid[i, y] >= height:
            directions_hidden += 1
            break
    for i in range(y - 1, -1, -1):
        if grid[x, i] >= height:
            directions_hidden += 1
            break
    for i in range(y + 1, max_height):
        if grid[x, i] >= height:
            directions_hidden += 1
            break

    return directions_hidden != 4


def viewing_score(x, y, grid, max_width, max_height):
    """Determine viewing score for potential treehouse position"""

    height = grid[(x, y)]

    up, down, left, right = 0, 0, 0, 0

    for i in range(x - 1, -1, -1):
        left += 1
        if grid[i, y] >= height:
            break
    for i in range(x + 1, max_width):
        right += 1
        if grid[i, y] >= height:
            break
    for i in range(y - 1, -1, -1):
        up += 1
        if grid[x, i] >= height:
            break
    for i in range(y + 1, max_height):
        down += 1
        if grid[x, i] >= height:
            break

    return up * down * left * right


def part1(grid, width, height):
    """How many trees are visible from outside?"""
    return sum(is_visible(*pos, grid, width, height) for pos in grid.keys())


def part2(grid, width, height):
    """What's the the tree with the highest viewing score?"""
    return max(viewing_score(*pos, grid, width, height) for pos in grid.keys())


def main():
    puzzle_input = get_data(day=8, year=2022).strip()
    grid, width, height = parse(puzzle_input)
    solution1 = part1(grid, width, height)
    solution2 = part2(grid, width, height)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1}\n{solution2}")
