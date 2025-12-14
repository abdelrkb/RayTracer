import math


class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # --- basic vector arithmetic ---

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, k):
        return Vec3(self.x * k, self.y * k, self.z * k)

    # --- dot product ---

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # --- vector length ---

    def length(self):
        return math.sqrt(self.dot(self))

    # --- normalized version of the vector ---

    def normalize(self):
        l = self.length()
        if l == 0:
            return Vec3(0, 0, 0)
        return Vec3(self.x / l, self.y / l, self.z / l)

    # --- helper to print vectors nicely ---

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"
