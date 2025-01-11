from aoc.tools.vector import Vec2

NORTH = Vec2(0, -1)
EAST = Vec2(1, 0)
SOUTH = Vec2(0, 1)
WEST = Vec2(-1, 0)
NORTH_EAST = Vec2(1, -1)
SOUTH_EAST = Vec2(1, 1)
SOUTH_WEST = Vec2(-1, 1)
NORTH_WEST = Vec2(-1, -1)

CARDINALS = {
    NORTH,
    EAST,
    SOUTH,
    WEST,
}

ORDINALS = {
    NORTH,
    NORTH_EAST,
    EAST,
    SOUTH_EAST,
    SOUTH,
    SOUTH_WEST,
    WEST,
    NORTH_WEST,
}
