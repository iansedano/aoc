def get_priority(item):
    """
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.

    >>> ord("a")
    97
    >>> ord("z")
    122
    >>> ord("A")
    65
    >>> ord("Z")
    90

    There are two ranges that need to be mapped onto other ranges:

                   65-90                      97-122
                     |                          |
                     v                          v
                   27-52                       1-26

    For the first range, you can just subtract 38 from the number to get the
    range 27-52. For the second range, you can subtract 96 to get range 1-26.
    With modulo, you can bring these two operations together without having to
    create an if statement.

    For _a_ modulo _b_, if _b_ is larger than _a_, then the result is always
    just _a_. It's as if you haven't operated on _a_.

    For _a_ modulo _b_, if _a_ is less than double _b_, then the result is the
    same as _a_ minus _b_.

    Combining these two properties of the modulo operator allows you to
    concisely map the ranges.

    You definitely need to subtract at least 38 from all the numbers, so you
    can start off with that:

                   65-90                      97-122
                     |                          |
                     v                          v
                   27-52                      59-84

    After subtracting 38, you still need to subtract 58 from the larger range.
    How could you subtract 58 from the higher range, without affecting the
    lower range? Modulo 58!

                   65-90                      97-122
                     |                          |
                     v                          v
                   27-52                       1-26
                (unaffected)
    """

    return (ord(item) - 38) % 58


def rock_paper_scissors_p1(f):
    """abc and xyz mean rock, paper, scissors

    A X       B Y        C Z
    rock  <  paper  <  scissors  <  rock...
     0         1          2

    paper vs rock (win)
      1   vs   0

    (1 - 0) % 3
    = 1

    paper vs scissors (lose)
      1   vs   2

    (1 - 2) % 3
    = 2

    paper vs paper (draw)
      1   vs   1

    (1 - 1) % 3
    = 0

    rock vs paper (lose)
      0   vs   1

    (0 - 1) % 3
    = 2
    """

    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)
        b = "XYZ".index(b)

        ans += b + 1

        match (b - a + 3) % 3:
            ...

    return ans


def rock_paper_scissors_p2(f):
    # xyz means lose draw win
    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)

        match b:
            case "X":
                ans += (a - 1) % 3 + 1
            case "Y":
                ans += 3
                ans += a + 1
            case "Z":
                ans += 6
                ans += (a + 1) % 3 + 1

    return ans
