from __future__ import annotations
import math


class Vector:
    """
    Represents a 3D Vector in space.
    """
    def __init__(self, x : float, y : float, z: float):
        """
        Create a 3D Vector.

        Args:
            x (float): x point
            y (float): y point
            z (float): z point
        """
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        """
        Return a readable string representation of the vector. Mainly used for debug.

        Returns:
            str: representation
        """
        return f"Vector({self.x}, {self.y}, {self.z})"

    def add(self, other : Vector) -> Vector:
        """
        Vector addition.

        Args:
            other (Vector): Vector to add

        Returns:
            Vector: self+other
        """
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other: Vector) -> Vector:
        """
        Vector substraction.

        Args:
            other (Vector): Vector to substract

        Returns:
            Vector: self-other
        """
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, k: float) -> Vector:
        """
        Vector multiplication by a scalar.

        Args:
            k (float): scalar 

        Returns:
            Vector: self-other
        """
        return Vector(self.x * k, self.y * k, self.z * k)

    def dot(self, other) -> float:
        """
        Product between two vectors.

        Args:
            other (Vector): another vector

        Returns:
            float: dot product self · other
        """
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        """
        Vector Length

        Returns:
            float: vector length
        """
        return math.sqrt(self.dot(self))

    def normalize(self) -> Vector:
        """
        Normalized version of the vector

        Returns:
            Vector: normalized vector
        """
        l = self.length()
        if l == 0:
            return Vector(0, 0, 0)
        return Vector(self.x / l, self.y / l, self.z / l)


