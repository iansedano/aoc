from pathlib import Path

from typ import Point, Img

from debug import p
from pprint import pp


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_input(raw_string=get_info_from_file()):
    lines = raw_string.strip().split("\n")

    algo = [0 if char == "." else 1 for char in lines[0]]
    grid = lines[2:]

    img = Img()

    offset = 0

    for i, row in enumerate(grid):
        y = (offset * len(grid)) + len(grid) - 1 - i
        for j, pixel in enumerate(row):
            x = offset * len(row) + j

            img[Point(x, y)] = pixel

    return algo, img
