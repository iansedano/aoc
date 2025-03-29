"""WIP"""

import heapq
from dataclasses import dataclass
from typing import NamedTuple

from common import main

DAY = 22
YEAR = 2015
SAMPLE = """"""


class Spell(NamedTuple):
    mana_cost: int
    damage: int
    heal: int
    armor: int
    mana_regain: int
    turns: int


@dataclass
class GameState:
    spells: list[Spell]
    player_hp: int
    player_mana: int
    boss_hp: int

    def __lt__(self, other):
        self.player_hp - self.boss_hp < other.player_hp - other.boss_hp


hp = 50
mana = 500

MAX_DURATION = 6

# Mana, damage, heal, armor, mana-regain, turns
magic_missile = Spell(53, 4, 0, 0, 0, 1)
drain = Spell(73, 2, 2, 0, 0, 1)
shield = Spell(113, 0, 0, 7, 0, 6)
poison = Spell(173, 3, 0, 0, 0, 6)
recharge = Spell(229, 0, 0, 0, 101, 5)

preferred_spell_order = [poison, shield, magic_missile, drain, recharge]
MAX_SPELL_DURATION = max(preferred_spell_order, key=lambda s: s.turns).turns


def parse(puzzle_input):
    # (hp, damage) 51, 9
    return tuple(int(line.split(": ")[1]) for line in puzzle_input.splitlines())


def part1(parsed_input):
    boss_hp, boss_damage = parsed_input
    play_game(boss_damage, GameState([], hp, mana, boss_hp))


def part2(parsed_input):
    return


def apply_spells_to_player(spells_cast, player_hp, player_mana, boss_hp):
    for i, spell in enumerate(spells_cast[-1:-7:-1]):
        if spell.turns >= i:
            player_hp = player_hp + spell.heal
            player_mana + spell.mana_regain
            player_armor = spell.armor
            boss_hp = boss_hp - spell.damage
            player_hp = min(0, boss_hp - player_armor)


def apply_spell_to_boss(spell, boss_hp):
    return boss_hp - spell.damage


def play_game(boss_damage, game_state: GameState):
    """
    Get possible spells
    for each spell:
        make new spell_cast routine
        simulate what would happen with spells_cast routine
        save new result of current spells cast
        decide if it can continue or should be discarded
    """

    priority_queue = []
    heapq.heappush(priority_queue, game_state)

    while True:
        current_game_state = heapq.heappop(priority_queue)
        spells = possible_spells(
            current_game_state.player_mana, current_game_state.spells
        )
        for spell in spells:
            new_game_state = get_new_game_state(
                boss_damage, current_game_state, spell
            )

            if new_game_state.boss_hp <= 0:
                return new_game_state
            if new_game_state.player_hp <= 0:
                continue

            heapq.heappush(priority_queue, new_game_state)


def get_new_game_state(
    boss_damage, current_game_state: GameState, new_spell: Spell
):
    """Simulate a player turn and a boss turn with the new spell and return new
    GameState"""

    """
    Effects based spells tick their timer down every turn, so 1 for player turn
    and 1 for boss turn.
    
    player casts poison, which lasts 6 turns, starts on next turn, bosses turn,
    then ticks down to 5. On player turn, deals effect again, and deals damage
    to boss, and ticks down to 4.
    
    They apply at the start of the turn, so when player casts them, they aren't
    active till the boss' turn
    """

    is_current_spell_effect = new_spell.turns > 1
    new_player_hp = current_game_state.player_hp
    new_player_mana = current_game_state.player_mana
    new_boss_hp = current_game_state.boss_hp

    # Player Turn
    # apply effects
    # cast spell
    active_effect_spells = [  # probably off by one
        spell
        for i, spell in enumerate(
            current_game_state.spells[-1 : -1 - MAX_SPELL_DURATION : -1]
        )
        if spell.turns >= i and spell.turns > 1
    ]
    player_current_armor = 0
    for spell in active_effect_spells:
        new_player_hp += spell.heal
        player_current_armor += spell.armor
        new_player_mana += spell.mana_regain

    new_boss_hp -= new_spell.damage if not is_current_spell_effect else 0
    new_player_mana -= new_spell.mana_cost

    # Boss Turn
    # apply effects
    # damage player
    for spell in active_effect_spells:
        new_boss_hp -= spell.damage

    new_player_hp -= max(boss_damage - player_current_armor, 0)

    return GameState(
        [*current_game_state, new_spell],
        new_player_hp,
        new_player_mana,
        new_boss_hp,
    )


def get_active_effect_spells(spells: list[Spell], player_turn: bool):
    """
    Should only be called at beginning of player turns.

    If player, don't include currently cast spell because it is not at beginning
    of turn.

    If boss, include player cast spell because then it's active at beginning of
    boss turn.

    >>> spells = [
    ...     Spell(2, 0, 0, 0, 0, 2),
    ...     Spell(1, 0, 0, 0, 0, 2),
    ... ]
    >>> get_active_effect_spells(spells, True)
    [Spell(mana_cost=1, damage=0, heal=0, armor=0, mana_regain=0, turns=2)]

    >>> spells = [
    ...     Spell(2, 0, 0, 0, 0, 2),
    ...     Spell(1, 0, 0, 0, 0, 2),
    ... ]
    >>> get_active_effect_spells(spells, False)
    [Spell(mana_cost=1, damage=0, heal=0, armor=0, mana_regain=0, turns=2)]

    >>> spells = [
    ...     Spell(4, 0, 0, 0, 0, 6),
    ...     Spell(3, 0, 0, 0, 0, 6),
    ...     Spell(2, 0, 0, 0, 0, 6),
    ...     Spell(1, 0, 0, 0, 0, 6),
    ... ]

    >>> get_active_effect_spells(spells, True) # doctest: +NORMALIZE_WHITESPACE
    [Spell(mana_cost=1, damage=0, heal=0, armor=0, mana_regain=0, turns=6),
     Spell(mana_cost=2, damage=0, heal=0, armor=0, mana_regain=0, turns=6),
     Spell(mana_cost=3, damage=0, heal=0, armor=0, mana_regain=0, turns=6)]

    """
    if not spells:
        return []
    if player_turn:
        spell_indices = [(-1, 2), (-2, 4), (-3, 6)]
    else:
        spell_indices = [(-1, 1), (-2, 3), (-3, 5)]

    active_spells = []
    for spell_index, turn_count in spell_indices:
        try:
            if spells[spell_index].turns >= turn_count:
                active_spells.append(spells[spell_index])
        except IndexError:
            continue

    return active_spells


def possible_spells(mana_budget, spells_cast=None):
    if spells_cast is None:
        spells_cast = []

    possible_spells = [
        spell
        for spell in preferred_spell_order
        if can_cast(spell, mana_budget, spells_cast)
        and (
            mana_budget - spell.mana_cost > 229
        )  # Not good for end of battle...
    ]
    return possible_spells


def can_cast(spell, budget, spells_cast):
    if spell.mana_cost > budget:
        return False

    if spell not in spells_cast:
        return True

    if len(spells_cast) < spell.turns:
        return False

    if spell in spells_cast[-1 * spell.turns :]:
        return False

    return True


if __name__ == "__main__":
    main(DAY, YEAR, SAMPLE, parse, part1, part2)
