from pathlib import Path
from pprint import pp

from debug import p

Point = tuple[int, int]


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_dots(raw_string=get_info_from_file()):

    lines = raw_string.strip().split("\n")

    dots, folds = [], []

    for line in lines:
        if "fold" in line:
            fold = line[11:].split("=")
            fold = (fold[0], int(fold[1]))
            folds.append(fold)
        elif line == "":
            continue
        else:
            dots.append(line)

    dots = [tuple(int(num) for num in line.split(",")) for line in dots]

    return dots, folds
