from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        123 328  51 64 
         45 64  387 23 
          6 98  215 314
        *   +   *   +  
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
