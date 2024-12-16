from aoc_tools.vector import Vec2


class Grid2D:

    @classmethod
    def from_string(cls, input, ignore=None):
        ignore = set() if ignore is None else ignore
        cls.grid = {}
        for y, line in enumerate(input.splitlines()):
            for x, char in enumerate(line):
                if char not in ignore:
                    cls.grid[Vec2(x, y)] = char
