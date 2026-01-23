from classes.render.canvas import Canvas
from classes.math3d.vector import Vector

class Viewport:
    def __init__(self,width: float,height: float,distance : float):
        self.width = width
        self.height = height
        self.distance = distance

    def canvas_to_viewport(self, canvas : Canvas, x : int, y : int) -> Vector:
        viewport_x = x * self.width / canvas.width
        viewport_y = y * self.height / canvas.height 
        viewport_z = self.distance

        return Vector(viewport_x, viewport_y, viewport_z)