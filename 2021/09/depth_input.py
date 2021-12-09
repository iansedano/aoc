from pathlib import Path

from debug import p


def get_info_from_file(path=Path(Path(__file__).parent, "input.txt")):
    with open(path, mode="r") as f:
        return f.read()


def parse_depth_data(
    raw_string=get_info_from_file(),
):
    """
    Return a two dimensional list of depths
    """
    lines = raw_string.strip().split("\n")
    depths = [[int(d) for d in line] for line in lines]

    return depths
