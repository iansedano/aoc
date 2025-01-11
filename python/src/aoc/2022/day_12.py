from dataclasses import dataclass, field
from queue import PriorityQueue
from string import ascii_lowercase

from aocd import get_data
from rich.console import Console

CONSOLE = Console()


@dataclass(frozen=True)
class Vec:
    x: int
    y: int

    @classmethod
    def from_vec(cls, vec):
        return cls(vec.x, vec.y)

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) == tuple:
            if len(other) != 2:
                raise TypeError
            return self.x == other[0] and self.y == other[1]
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"


@dataclass(order=True)
class Loc:
    f: int
    position: Vec = field(compare=False)
    height: int = field(compare=False)
    parent_position: Vec = field(default=None, compare=False)
    g_distance: int = field(default=0, compare=False)
    heuristic: int = field(default=float("inf"), compare=False)

    def copy(self):
        return Loc(
            self.f,
            self.position,
            self.height,
            self.parent_position,
            self.g_distance,
            self.heuristic,
        )


def parse(puzzle_input):
    """Parse input."""

    grid = {}
    start = end = ()
    for y, row in enumerate(puzzle_input.split("\n")):
        for x, char in enumerate(row):
            if char == "S":
                grid[Vec(x, y)] = start = Loc(
                    0, Vec(x, y), ascii_lowercase.index("a")
                )
                continue
            if char == "E":
                grid[Vec(x, y)] = end = Loc(
                    0, Vec(x, y), ascii_lowercase.index("z")
                )
                continue

            grid[Vec(x, y)] = Loc(0, Vec(x, y), ascii_lowercase.index(char))

    for loc in grid.values():
        if loc is end:
            loc.heuristic = 1
            continue
        # diff = end.position - loc.position
        loc.heuristic = 1  # (diff.x**2 + diff.y**2) ** 1 / 2

    return grid, start, end


def print_grid(grid):
    max_x = max(p.x for p in grid.keys())
    max_y = max(p.y for p in grid.keys())

    print(max_x, max_y)

    for y in range(max_y):
        for x in range(max_x):
            print(f"{grid[Vec(x, y)].height:^3}", end="")
        print()


def viz(grid, current_node: Loc, open_, closed_):
    max_x = max(p.x for p in grid.keys()) + 1
    max_y = max(p.y for p in grid.keys()) + 1
    path = [current_node.position]
    node = current_node
    while node := grid.get(node.parent_position):
        path.append(node.position)

    out = ["   "]
    out.extend(f"{i:^3}" for i in range(max_x))
    out.append("\n")
    for y in range(max_y):
        out.append(f"{y:^3}")

        for x in range(max_x):
            current_height = grid.get(Vec(x, y)).height
            if Vec(x, y) == current_node.position:
                out.append(f"[yellow]{current_height:^3}[/yellow]")
            elif Vec(x, y) in path:
                out.append(f"[red]{current_height:^3}[/red]")
            elif Vec(x, y) in [l.position for l in open_.queue]:
                out.append(f"[#36454F on green]{current_height:^3}[/]")
            elif Vec(x, y) in closed_:
                out.append(f"[black on blue]{current_height:^3}[/]")
            else:
                out.append(f"[#36454F]{current_height:^3}[/#36454F]")
        out.append("\n")
    return "".join(out)


def get_neighbors(location: Loc, grid: dict):
    neighbors = []
    for x, y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        diff = Vec(x, y)
        potential_neighbor = grid.get(location.position + diff)

        if (
            potential_neighbor
            and (potential_neighbor.height - location.height) <= 1
        ):
            neighbor = potential_neighbor.copy()
            neighbors.append(neighbor)
    return sorted(neighbors, key=lambda n: n.heuristic)


def a_star(grid, start: Loc, end: Loc):

    open_: PriorityQueue[Loc] = PriorityQueue()
    closed_: set[Vec] = set()

    open_.put(start)

    while not open_.empty():

        current_node = open_.get()

        closed_.add(current_node.position)
        grid[current_node.position] = current_node

        if current_node.position == end.position:

            path = [current_node]

            while current_node := grid.get(current_node.parent_position):
                path.append(current_node.position)

            return path

        children = get_neighbors(current_node, grid)

        for child in children:
            if child.position in closed_:
                continue

            child.parent_position = current_node.position

            g_distance = grid.get(child.parent_position, 0).g_distance + 1
            f = g_distance + child.heuristic

            already_open = next(
                (
                    (i, loc)
                    for i, loc in enumerate(open_.queue)
                    if child.position == loc.position
                ),
                None,
            )

            if already_open and already_open[1].f < f:
                continue
            elif already_open:
                open_.queue.pop(already_open[0])

            child.g_distance = g_distance
            child.f = f
            open_.put(child)

        children.clear()


def part1(data):
    grid, start, end = data

    print(len(a_star(grid, start, end)) - 1)


def part2(data):
    grid, _, end = data

    start_points = [loc for loc in grid.values() if loc.height == 0]

    results = filter(
        lambda x: x is not None,
        [a_star(grid, start, end) for start in start_points],
    )

    print(sorted([len(result) - 1 for result in results])[0])


def main():
    puzzle_input = get_data(day=12, year=2022).strip()
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    solution1, solution2 = main()
    print(f"{solution1 = }\n{solution2 = }")
