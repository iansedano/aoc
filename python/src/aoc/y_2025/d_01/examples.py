from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """
        ),
        None,
        None,
    ),
    (
        dedent(
            """\
        ...
        """
        ),
        None,
        None,
    ),
]
