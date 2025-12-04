from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        ..@@.@@@@.
        @@@.@.@.@@
        @@@@@.@.@@
        @.@@@@..@.
        @@.@@@@.@@
        .@@@@@@@.@
        .@.@.@.@@@
        @.@@@.@@@@
        .@@@@@@@@.
        @.@.@@@.@.
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
