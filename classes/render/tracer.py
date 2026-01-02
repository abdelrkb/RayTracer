from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere
from classes.render.light import compute_lighting, Light
from classes.math3d.vector import Vector
from classes.objects.color import Color

class Tracer:
    """
    Core RayTracing engine.

    The tracers serves purpose for finding intersections between rays ands objects, dermining is an object
    is visible or not, compute lightning and handles shadows.

    It does not generate ray itself (it's the Camera's job)
    """
    def __init__(self, spheres :list[Sphere], lights :list[Light] ,background_color=Color(255, 255, 255)):
        """
        Create a tracer.

        Args:
            spheres (list[Sphere]): objects in the scene
            lights (list[Light]): lights in the scene
            background_color (Color): RGB color used when a ray does not hit any object (white)
        """
        self.spheres = spheres
        self.lights= lights
        self.background_color = background_color

    def closest_intersection(self, origin : Vector, direction : Vector, t_min: float, t_max: float) -> tuple[Sphere | None, float]:
        """
        Find the closest intersection between a ray and an object.

        This method tests the ray against all spheres in the scene and returns the nearest intersection.

        Args: 
            origin (Vector): ray's origin
            direction (Vector): ray's direction
            t_min (float): minimum valid t value
            t_max (float): maximum valid t value  

        Returns : 
            tuple[Sphere | None, float]: the nearest intersection and the corresponding distance t
        """
        closest_t = float('inf')
        closest_sphere = None
        ray = Ray(origin, direction)

        for sphere in self.spheres:
            t1, t2 = sphere.intersect_ray_sphere(ray)

            if t_min < t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_sphere = sphere

            if t_min < t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_sphere = sphere

        return closest_sphere, closest_t

    def trace_ray(self, ray: Ray, t_min: float, t_max: float) -> tuple[int, int, int]:
        """
        Trace a ray into the scene and compute its color.

        Args:
            ray (Ray): ray to trace
            t_min (float): minimum valid t value
            t_max (float): maximum valid t value

        Returns:
            tuple[int, int, int]: final RGB color
        """
        closest_sphere, closest_t = self.closest_intersection(ray.origin,ray.direction,t_min,t_max)
        if closest_sphere is None:
            return self.background_color.to_rgb()
        
        P = ray.point_at(closest_t)
        N = P.sub(closest_sphere.center).normalize()
        V = ray.direction.mul(-1)
        lighting = compute_lighting(P,N,V, closest_sphere.specular, self.lights, self)
        color = closest_sphere.color.mul(lighting)
        return color.to_rgb()