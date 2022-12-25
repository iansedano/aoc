from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2D:
    x: int
    y: int

    @classmethod
    def from_vec(cls, vec):
        return cls(vec.x, vec.y)

    def __add__(self, other):
        if type(other) == tuple:
            if len(other) != 2:
                raise TypeError
            return Vec2D(self.x + other[0], self.y + other[1])
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) == tuple:
            if len(other) != 2:
                raise TypeError
            return Vec2D(self.x - other[0], self.y - other[1])
        return Vec2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) == tuple:
            if len(other) != 2:
                raise TypeError
            return self.x == other[0] and self.y == other[1]
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        yield from (self.x, self.y)


@dataclass(frozen=True)
class Vec3D:
    x: int
    y: int
    z: int

    @classmethod
    def from_vec(cls, vec):
        return cls(vec.x, vec.y, vec.z)

    def __add__(self, other):
        if type(other) == tuple:
            if len(other) != 3:
                raise TypeError
            return Vec3D(
                self.x + other[0], self.y + other[1], self.z + other[2]
            )
        return Vec3D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if type(other) == tuple:
            if len(other) != 3:
                raise TypeError
            return Vec3D(
                self.x - other[0], self.y - other[1], self.z - other[2]
            )
        return Vec3D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if type(other) == tuple:
            if len(other) != 3:
                raise TypeError
            return (
                self.x == other[0] and self.y == other[1] and self.z == other[2]
            )
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        yield from (self.x, self.y, self.z)
