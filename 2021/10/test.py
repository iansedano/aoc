import subsystem_input
from elements import Node, Token, Token_type, build_tree, print_tree
import elements

from debug import p
from pprint import pp

SAMPLE_01 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

MIN_SAMPLE = """
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>"""

"""
[
    (
        ()
        [<>]
    )
]
(
    {
        [
            <
                {
                    <
                        <[]>
                    >
                    (
                        
                        
{
    (
        [
            (
                <
                    {}
                    [
                        <>
                        []
                        }>{[]{[(<()> CORRUPTED
"""


BASIC = """{}
<>
()
[]
{}()[]<>
[[((<<>>))]]"""

MIN_CORRUPTED = """[)]"""
CORRUPTED_2 = """[)]
[}]
[)]
[)]"""


def test_sample_parse():
    token_lines = subsystem_input.parse_subsystem_data(MIN_SAMPLE)
    pp(token_lines)


def test_elements():
    token = Token(Token_type("{"))
    print(token)


def test_basic_sample_part_1():
    token_lines = subsystem_input.parse_subsystem_data(BASIC)
    for token_line in token_lines:
        print("\n===============")
        print("\nBUILDING LINE\n")
        tree = build_tree(token_line)
        print("\nPRINTING TREE")
        print_tree(tree)


def test_min_corrupted_part_1():
    token_lines = subsystem_input.parse_subsystem_data(MIN_CORRUPTED)
    corruption_score = 0
    for token_line in token_lines:
        try:
            tree = build_tree(token_line)
        except Exception as e:
            corruption_score += elements.ILLEGAL_CHAR_POINTS[str(e)]
    print(corruption_score)


def test_sample_part_1():
    token_lines = subsystem_input.parse_subsystem_data(SAMPLE_01)
    corruption_score = 0
    for token_line in token_lines:
        try:
            tree = build_tree(token_line)
        except Exception as e:
            corruption_score += elements.ILLEGAL_CHAR_POINTS[str(e)]
    assert corruption_score == 26397


test_sample_part_1()


def test_token_matching_parent():

    assert (
        elements.token_matches_parent(
            Token(Token_type.SQUARE_CLOSE), Node(Token(Token_type.NORMAL_OPEN))
        )
        == False
    )


# test_token_matching_parent()
def test_part_1():
    token_lines = subsystem_input.parse_subsystem_data()
    corruption_score = 0
    for token_line in token_lines:
        try:
            tree = build_tree(token_line)
        except Exception as e:
            pass
            corruption_score += elements.ILLEGAL_CHAR_POINTS[str(e)]
    assert corruption_score == 364389


test_part_1()


def test_sample_part_2():
    token_lines = subsystem_input.parse_subsystem_data(SAMPLE_01)
    ok_lines = []
    scores = []
    for token_line in token_lines:
        try:
            tree = build_tree(token_line)
            ok_lines.append(token_line)
            close_chars = elements.get_chars_to_close_open_tree(tree)

            score = elements.get_closing_char_score(close_chars)
            scores.append(score)

        except Exception as e:
            pass

    scores.sort()
    from statistics import median

    middle_score = median(scores)
    assert middle_score == 288957


test_sample_part_2()


def test_part_2():
    token_lines = subsystem_input.parse_subsystem_data()
    ok_lines = []
    scores = []
    for token_line in token_lines:
        try:
            tree = build_tree(token_line)
            ok_lines.append(token_line)
            close_chars = elements.get_chars_to_close_open_tree(tree)

            score = elements.get_closing_char_score(close_chars)
            scores.append(score)

        except Exception as e:
            pass

    scores.sort()
    from statistics import median

    middle_score = median(scores)
    assert middle_score == 2870201088


test_part_2()
