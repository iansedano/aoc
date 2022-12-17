import dirac

ex_player_1 = 4
ex_player_2 = 8


player_1 = 7
player_2 = 8


"""
player score, position
board gives new position (die, position)
die 100 gives 6, 6 + 9, n(n-2) + 9 ()


while player1
"""


def test_1():
    board = dirac.Board()
    die = dirac.Die()

    players: list[dirac.Player] = [dirac.Player(0, 4), dirac.Player(0, 8)]

    turn = 0
    while not any([player.score > 999 for player in players]):
        player = players[turn]
        dirac.game_tick(player, board, die)
        turn = 1 if turn == 0 else 0

    print(players)
    print(die.count)

    board = dirac.Board()
    die = dirac.Die()

    players: list[dirac.Player] = [dirac.Player(0, 7), dirac.Player(0, 8)]

    turn = 0
    while not any([player.score > 999 for player in players]):
        player = players[turn]
        dirac.game_tick(player, board, die)
        turn = 1 if turn == 0 else 0

    print(players)
    print(die.count)


test_1()
