from pathlib import Path
import re

from debug import p


Point = tuple[int, int]
Line = tuple[Point, Point]


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_vent_data(raw_string=get_info_from_file()) -> list[Line]:
    """
    Output
    [ [vent(x1,y1),(x2,y2)] , [vent(x1,y1),(x2,y2)]
    """
    vent_lines = raw_string.strip().split("\n")

    vent_coords_raw = [line.split(" -> ") for line in vent_lines]

    output: list[Line] = [
        tuple(tuple(int(s) for s in str.split(",")) for str in raw_coord)
        for raw_coord in vent_coords_raw
    ]

    return output
