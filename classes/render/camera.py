from classes.math3d.vector import Vector
from classes.math3d.ray import Ray
from classes.render.viewport import Viewport
from classes.render.canvas import Canvas

class Camera:
    """
    Represents the camera in the raytracer.

    The camera defines:
    - the viewer's position in the scene
    - how we generate rays through the viewport

    For each pixel on the canvas, the camera generates a ray
    that starts at the camera position and passes through the
    corresponding point on the viewport.
    """
    def __init__(self, position: Vector, viewport: Viewport):
        """
        Create a camera.

        Args:
            position (Vector): position of the camera into the world space
            viewport (Viewport): viewport associated to the camera
        """
        self.position = position
        self.viewport = viewport

    def get_ray(self, canvas: Canvas, x: int, y: int) -> Ray:
        """
        Generate a ray from the camera through a canvas pixel.

        This method converts the canvas pixel (x,y) to a point on the viewport and then builds a ray from
        the camera position towards that ray

        Args:
            canvas (Canvas): canvas being rendered
            x (int): x pixel coordinate
            y (int): y pixel coordinate

        Returns:
            Ray: ray that starts at the camera and pass through the viewport
        """
        V = self.viewport.canvas_to_viewport(canvas, x, y)

        direction = V.sub(self.position)

        return Ray(self.position, direction)