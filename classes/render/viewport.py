from classes.render.canvas import Canvas
from classes.math3d.vector import Vector

class Viewport:
    """
    Represents the viewport (projection plane) in the raytracer.

    The viewport is a rectangle in 3D space, centered on the camera's view axis and located at a fix distance from camera.
    
    Each pixel on the canvas maps to a point on the viewport.
    """
    def __init__(self,width: float,height: float,distance : float):
        """
        Create a viewport.

        Args:
            width (float): viewport width in world units
            height (float): viewport height in world units
            distance (float): distance from the camera to the viewport
        """
        self.width = width
        self.height = height
        self.distance = distance

    def canvas_to_viewport(self, canvas : Canvas, x : int, y : int) -> Vector:
        """
        Convert canvas coordinate to viewport coordinate.

        Args:
            canvas (Canvas): canvas rendered
            x (int): x coordinate on the canvas
            y (int): y coordinate on the canvas

        Returns:
            Vector: point on the viewport in world space
        """
        viewport_x = x * self.width / canvas.width
        viewport_y = y * self.height / canvas.height
        viewport_z = self.distance

        return Vector(viewport_x, viewport_y, viewport_z)