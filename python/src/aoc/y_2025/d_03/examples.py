from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        987654321111111
        811111111111119
        234234234234278
        818181911112111
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
