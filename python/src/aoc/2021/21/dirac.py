import itertools
from collections import namedtuple
from dataclasses import dataclass
from pprint import pp

from debug import p

# Player = namedtuple("Player", ["score", "position"])


@dataclass
class Player:
    score: int
    position: int


class Board:
    def __init__(self):
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_new_position(self, num_to_advance, current_position):

        current_index = current_position - 1
        num_to_advance = (num_to_advance) % 10

        for _ in range(num_to_advance):
            current_index += 1
            current_index = current_index % 10

        return self.positions[current_index]


class Die:
    def __init__(self):
        self.count = 0
        self.score = 0
        self.last_increment = 0

    def get_score(self):
        if self.count == 0:
            self.count = 3
            self.score = 6
            return self.score

        self.count += 3
        self.score += 9
        return self.score


def game_tick(player: Player, board: Board, die: Die):

    score = die.get_score()
    position = board.get_new_position(score, player.position)
    player.position = position
    player.score += position


class Universe:
    def __init__(self):
        pass


class Universe:
    def __init__(self, player_1, player_2):
        self.children = []
        self.player_1 = player_1
        self.player_2 = player_2
        
    def game_tick(self):
        
