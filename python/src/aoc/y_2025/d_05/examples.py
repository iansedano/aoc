from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        3-5
        10-14
        16-20
        12-18

        1
        5
        8
        11
        17
        32
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
