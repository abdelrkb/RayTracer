from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere

class Tracer:
    def __init__(self, spheres, background_color=(255, 255, 255)):
        self.spheres = spheres
        self.background_color = background_color

    def trace_ray(self, ray: Ray, t_min: float, t_max: float):

        closest_t = float('inf')
        closest_sphere = None

        for sphere in self.spheres:
            t1, t2 = sphere.intersect_ray_sphere(ray)

            if t_min < t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_sphere = sphere

            if t_min < t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_sphere = sphere

        if closest_sphere is None:
            return self.background_color

        return closest_sphere.color
