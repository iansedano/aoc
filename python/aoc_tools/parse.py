import re


def ints(line):
    """
    >>> ints("p=0,4 v=3,-3")
    (0, 4, 3, -3)
    >>> ints("Button A: X+94, Y+34")
    (94, 34)
    """
    return tuple(int(d) for d in re.findall(r"-*\d+", line))
