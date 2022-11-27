from debug import p
from pprint import pp


def fold(dots, fold):

    orientation = 0 if fold[0] == "x" else 1

    output = set()

    for dot in dots:

        if dot[orientation] > fold[1]:
            new_pos = fold[1] - (dot[orientation] - fold[1])
            new_dot = (dot[0], new_pos) if orientation == 1 else (new_pos, dot[1])
            output.add(new_dot)

        else:
            output.add(dot)

    return list(output)


def get_grid_size(dots):
    y = max([dot[1] for dot in dots])
    x = max([dot[0] for dot in dots])

    return x, y


def print_dots(dots):

    x, y = get_grid_size(dots)

    grid = [["_" for __ in range(y + 1)] for _ in range(x + 1)]

    for d in dots:
        grid[d[0]][d[1]] = "#"

    pp(grid)
