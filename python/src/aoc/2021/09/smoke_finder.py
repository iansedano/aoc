from debug import p

DIRS = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}


def find_low_points(heightmap: list[list[int]]):
    low_points = []

    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):

            adjacent_heights = []
            if i != 0:
                n = heightmap[i + DIRS["N"][0]][j + DIRS["N"][1]]
                adjacent_heights.append(n)

            if j != 0:
                w = heightmap[i + DIRS["W"][0]][j + DIRS["W"][1]]
                adjacent_heights.append(w)

            if j != len(row) - 1:
                e = heightmap[i + DIRS["E"][0]][j + DIRS["E"][1]]
                adjacent_heights.append(e)

            if i != len(heightmap) - 1:
                s = heightmap[i + DIRS["S"][0]][j + DIRS["S"][1]]
                adjacent_heights.append(s)

            if height < min(adjacent_heights):
                low_points.append((i, j, height))

    return low_points


def get_basin(heightmap: list[list[int]], low_point: tuple[int, int, int]):

    """
    until 9 or height lower than current
    """

    basin: list[tuple[int, int]] = [low_point]

    def basin_helper(heightmap, current_point, basin):
        row, col, height = current_point

        if row != 0:
            n_pos = (row + DIRS["N"][0], col + DIRS["N"][1])
            n_depth = heightmap[n_pos[0]][n_pos[1]]
            if n_depth > height and n_depth != 9:
                n_point = (n_pos[0], n_pos[1], n_depth)
                basin.append(n_point)
                basin = basin_helper(heightmap, n_point, basin)

        if col != 0:
            w_pos = (row + DIRS["W"][0], col + DIRS["W"][1])
            w_depth = heightmap[w_pos[0]][w_pos[1]]
            if w_depth > height and w_depth != 9:
                w_point = (w_pos[0], w_pos[1], w_depth)
                basin.append(w_point)
                basin = basin_helper(heightmap, w_point, basin)

        if col != len(heightmap[0]) - 1:
            e_pos = (row + DIRS["E"][0], col + DIRS["E"][1])
            e_depth = heightmap[e_pos[0]][e_pos[1]]
            if e_depth > height and e_depth != 9:
                e_point = (e_pos[0], e_pos[1], e_depth)
                basin.append(e_point)
                basin = basin_helper(heightmap, e_point, basin)

        if row != len(heightmap) - 1:
            s_pos = (row + DIRS["S"][0], col + DIRS["S"][1])
            s_depth = heightmap[s_pos[0]][s_pos[1]]
            if s_depth > height and s_depth != 9:
                s_point = (s_pos[0], s_pos[1], s_depth)
                basin.append(s_point)
                basin = basin_helper(heightmap, s_point, basin)

        return basin

    return list(set(basin_helper(heightmap, low_point, basin)))
