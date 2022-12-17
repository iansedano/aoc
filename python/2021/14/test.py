from collections import Counter
from pprint import pp

import input
import polymer
from debug import p

EX_01 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_input():
    chain, rules = input.parse_template(EX_01)


test_input()


def test_part_1():
    chain, rules = input.parse_template(EX_01)

    chain = polymer.step(chain, rules)
    assert "".join(chain) == "NCNBCHB"
    chain = polymer.step(chain, rules)
    assert "".join(chain) == "NBCCNBBBCBHCB"
    chain = polymer.step(chain, rules)
    assert "".join(chain) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
    chain = polymer.step(chain, rules)
    assert "".join(chain) == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"

    chain = polymer.step(chain, rules)
    chain = polymer.step(chain, rules)
    chain = polymer.step(chain, rules)
    chain = polymer.step(chain, rules)
    chain = polymer.step(chain, rules)
    chain = polymer.step(chain, rules)

    assert polymer.score(chain) == 1588

    chain, rules = input.parse_template()
    for _ in range(10):
        chain = polymer.step(chain, rules)
    assert polymer.score(chain) == 2194


def part_2():
    chain, rules = input.parse_template(EX_01)
    first_base = chain[0]
    last_base = chain[-1]
    chain_representation = polymer.sim(chain, rules, 40)
    p(chain_representation)
    counts = {base: 0 for base in polymer.return_unique_bases(rules)}
    for pair, value in chain_representation.items():
        for base in pair:
            counts[base] += value
    counts[first_base] += 1
    counts[last_base] += 1
    p(counts)
    counts = [value / 2 for value in counts.values()]
    assert max(counts) - min(counts) == 2188189693529

    chain, rules = input.parse_template()
    first_base = chain[0]
    last_base = chain[-1]
    chain_representation = polymer.sim(chain, rules, 40)
    p(chain_representation)
    counts = {base: 0 for base in polymer.return_unique_bases(rules)}
    for pair, value in chain_representation.items():
        for base in pair:
            counts[base] += value
    counts[first_base] += 1
    counts[last_base] += 1
    p(counts)
    counts = [value / 2 for value in counts.values()]
    print(max(counts) - min(counts))


part_2()
