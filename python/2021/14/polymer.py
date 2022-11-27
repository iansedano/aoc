from collections import Counter

from debug import p
from pprint import pp


def step(chain, rules):

    new_chain = []
    base_gen = (b for b in chain)
    current_pair = (next(base_gen, None), next(base_gen, None))
    while current_pair[1] is not None:
        insertion = rules[current_pair]
        new_chain = new_chain + [current_pair[0], insertion]
        current_pair = (current_pair[1], next(base_gen, None))
    new_chain.append(current_pair[0])

    return new_chain


def score(chain):
    c = Counter(chain)
    common = c.most_common()
    return common[0][1] - common[-1][1]


def return_unique_bases(rules):
    bases = set()
    for rule, replacement in rules.items():
        bases.add(rule[0])
        bases.add(rule[1])
        bases.add(replacement)

    return list(bases)


def break_chain_into_pairs(chain, rep_dict):

    chain_representation = {key: 0 for key in rep_dict.keys()}

    base_gen = (b for b in chain)
    current_pair = (next(base_gen, None), next(base_gen, None))
    while current_pair[1] is not None:
        chain_representation[current_pair] += 1
        current_pair = (current_pair[1], next(base_gen, None))

    return chain_representation


def make_replacement_pair_dict(rules):
    dict = {pair: "" for pair, _ in rules.items()}

    for rule in rules:
        val = list(rule)
        val = step(val, rules)
        dict[rule] = [tuple([val[0], val[1]]), tuple([val[1], val[2]])]
    return dict


def sim(chain, rules, generations):
    rep_dict = make_replacement_pair_dict(rules)
    chain_representation = break_chain_into_pairs(chain, rep_dict)

    for _ in range(generations):

        pair_values = list(chain_representation.items())

        for pair_value in pair_values:
            pair = pair_value[0]
            value = pair_value[1]
            replacement_pairs = rep_dict[pair]
            for tup in replacement_pairs:
                chain_representation[tup] += value
            chain_representation[pair] -= value

    return chain_representation
