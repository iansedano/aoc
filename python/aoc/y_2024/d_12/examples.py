from textwrap import dedent

examples = [
    (
        dedent(
            """\
            RRRRIICCFF
            RRRRIICCCF
            VVRRRCCFFF
            VVRCCCJFFF
            VVVVCJJCFE
            VVIVCCJJEE
            VVIIICJJEE
            MIIIIIJJEE
            MIIISIJEEE
            MMMISSJEEE
            """
        ),
        1930,
        1206,
    ),
    (
        dedent(
            """\
            OOOOO
            OXOXO
            OOOOO
            OXOXO
            OOOOO
            """
        ),
        772,
        436,
    ),
    (
        dedent(
            """\
            AAAA
            BBCD
            BBCC
            EEEC
            """
        ),
        140,
        80,
    ),
    (
        dedent(
            """\
            EEEEE
            EXXXX
            EEEEE
            EXXXX
            EEEEE
            """
        ),
        692,
        236,
    ),
    (
        dedent(
            """\
            AAAAAA
            AAABBA
            AAABBA
            ABBAAA
            ABBAAA
            AAAAAA
            """
        ),
        1184,
        368,
    ),
]
