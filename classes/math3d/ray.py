class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()

    def point_at(self, t):
        return self.origin.add(self.direction.mul(t))