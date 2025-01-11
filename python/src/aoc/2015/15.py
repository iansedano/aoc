import math
from itertools import product
from typing import NamedTuple

from common import main
from parse import compile

DAY = 15
YEAR = 2015
SAMPLE = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

pattern = compile(
    "{ingredient}: capacity {capacity:d}, durability {durability:d}, "
    "flavor {flavor:d}, texture {texture:d}, calories {calories:d}"
)


class IngredientProperties(NamedTuple):
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse(puzzle_input):
    return {
        (vals := list(pattern.parse(line).named.values()))[0]: IngredientProperties(
            *vals[1:]
        )
        for line in puzzle_input.splitlines()
    }


def part1(input):
    return max(
        math.prod(
            score if score > 0 else 0
            for score in score_recipe(recipe, input.values())[:-1]
        )
        for recipe in get_possible_recipes(len(input))
    )


def part2(input):
    scores = (
        tuple(
            score if score > 0 else 0 for score in score_recipe(recipe, input.values())
        )
        for recipe in get_possible_recipes(len(input))
    )
    scores = ((score[:-1], score[-1]) for score in scores)

    return max(math.prod(recipe[0]) for recipe in scores if recipe[1] == 500)


def score_recipe(recipe: tuple, ingredients: list[IngredientProperties]):
    totals = [0] * 5
    for amount, ingredient in zip(recipe, ingredients):
        totals[0] += ingredient.capacity * amount
        totals[1] += ingredient.durability * amount
        totals[2] += ingredient.flavor * amount
        totals[3] += ingredient.texture * amount
        totals[4] += ingredient.calories * amount

    return totals


def get_possible_recipes(ingredient_count):
    return list(
        (*result, 100 - sum(result))
        for result in product(range(101), repeat=ingredient_count - 1)
        if sum(result) <= 100
    )


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
