from collections import namedtuple
from textwrap import dedent

Example = namedtuple("Example", ["input", "part_1", "part_2"])

examples = [
    (
        dedent(
            """\
        abcdef
        bababc
        abbcde
        abcccd
        aabcdd
        abcdee
        ababab
        """
        ),
        12,
        None,
    ),
    (
        dedent(
            """\
        abcde
        fghij
        klmno
        pqrst
        fguij
        axcye
        wvxyz
        """
        ),
        None,
        "fgij",
    ),
]
