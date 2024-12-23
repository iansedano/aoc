from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Vector = namedtuple("Vector", ["x", "y"])
Target = namedtuple("Target", ["top_left", "bottom_right"])

Report = {
    "x_left": int,
    "x_right": int,
    "y_top": int,
    "y_bottom": int,
    "missed": bool,
    "hit": bool,
}
