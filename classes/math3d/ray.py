from classes.math3d.vector import Vector

class Ray:
    """
    Represents a ray in 3D space.
    """
    def __init__(self, origin : Vector, direction : Vector):
        """
        Create a ray

        Args:
            origin (Vector): starting point of the ray
            direction(Vector): direction of the ray normalized
        """
        self.origin = origin
        self.direction = direction.normalize()

    def point_at(self, t : float) -> Vector:
        """
        Compute a point along the ray.

        Uses the parametric ray equatrion P(t) = origin + t * direction

        Args: 
            t (float): distance parameter along the ray

        Returns: 
            Vector: point located at distance t along the ray
        """
        return self.origin.add(self.direction.mul(t))