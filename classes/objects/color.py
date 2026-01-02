from __future__ import annotations

class Color:
    """
    Represents an RGB color.

    Color values are stored as floats internally and
    converted to integers (0 to 255) when needed.
    """

    def __init__(self, r: float, g: float, b: float):
        self.r = r
        self.g = g
        self.b = b

    def mul(self, k: float) -> Color:
        """
        Multiply color by a scalar
        """
        return Color(self.r * k, self.g * k, self.b * k)

    def add(self, other) -> Color:
        """Add two colors together."""
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def clamp(self):
        """
        Clamp color values
        """
        return Color(min(255, max(0, int(self.r))), min(255, max(0, int(self.g))), min(255, max(0, int(self.b))))

    def to_rgb(self):
        """
        Return color as an RGB tuple.
        """
        c = self.clamp()
        return (c.r, c.g, c.b)