from itertools import chain, combinations
from typing import Iterable


def power_set_iterative(input: Iterable):
    if len(input) == 0:
        return [[]]

    subsets = []
    first_element, *remaining_set = input
    for subset in power_set_iterative(remaining_set):
        subsets.append(subset)
        next_subset = subset + [first_element]
        subsets.append(next_subset)

    return subsets


# almost 10x faster than others
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# On avg about 10% slower than iterative
def power_set(input: Iterable):
    return (
        [
            subset
            for curr_subset in power_set(input[1:])
            for subset in (curr_subset, curr_subset + input[:1])
        ]
        if len(input) != 0
        else [[]]
    )


p = powerset(list(range(20)))
