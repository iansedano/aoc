from pprint import pp
from debug import p

from functools import reduce


def lmap(f, arr):
    return list(map(f, arr))


def simulate(octo_array, generations):

    size = len(octo_array) * len(octo_array[0])

    # pp(octo_array)
    flashes = 0
    first_sync_flash = None

    for i in range(generations):
        # print("AGE TICK")
        octo_array = age_tick(octo_array)
        # print("LIGHT TICK")
        octo_array = light_tick(octo_array)

        flash_count = count_flash(octo_array)
        if flash_count == size and first_sync_flash is None:
            first_sync_flash = i + 1

        flashes += flash_count
        # print("RESET TICK")
        octo_array = reset_flashed_octopi(octo_array)
        # pp(octo_array)

    print("FLASHES", flashes)
    p(first_sync_flash)
    return octo_array


def age_tick(octo_array):
    output = lmap(lambda row: lmap(lambda octo: octo + 1, row), octo_array)

    return output


CARDINALS = {
    "N": (-1, 0),
    "NE": (-1, 1),
    "E": (0, 1),
    "SE": (1, 1),
    "S": (1, 0),
    "SW": (1, -1),
    "W": (0, -1),
    "NW": (-1, -1),
}


def light_tick(octo_array):

    _octo_array = list(octo_array)

    for i, row in enumerate(_octo_array):
        for j, octo in enumerate(row):
            if octo == 10:
                highlight_flash(_octo_array, i, j)

    return _octo_array


def highlight_flash(octo_array, row, col):
    _octo_array = list(octo_array)

    assert _octo_array[row][col] == 10

    _octo_array[row][col] = 11

    for v, h in CARDINALS.values():
        if row + v in range(len(_octo_array)) and col + h in range(len(_octo_array[0])):

            if _octo_array[row + v][col + h] < 10:
                _octo_array[row + v][col + h] += 1

            if _octo_array[row + v][col + h] == 10:
                highlight_flash(_octo_array, row + v, col + h)

    return _octo_array


def count_flash(octo_array):
    return sum(map(lambda row: row.count(11), octo_array))


def reset_flashed_octopi(octo_array):
    return lmap(
        lambda row: lmap(lambda octo: 0 if octo == 11 else octo, row), octo_array
    )
