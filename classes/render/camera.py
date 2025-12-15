from classes.math3d.vector import Vector
from classes.math3d.ray import Ray
from classes.render.viewport import Viewport
from classes.render.canvas import Canvas

class Camera:
    def __init__(self, position: Vector, viewport: Viewport):
        self.position = position
        self.viewport = viewport

    def get_ray(self, canvas: Canvas, x: int, y: int) -> Ray:

        V = self.viewport.canvas_to_viewport(canvas, x, y)

        direction = V.sub(self.position)

        return Ray(self.position, direction)