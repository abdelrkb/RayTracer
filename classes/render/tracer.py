from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere
from classes.render.light import compute_lighting, Light
from classes.math3d.vector import Vector
from classes.objects.color import Color

class Tracer:
    def __init__(self, spheres :list[Sphere], lights :list[Light] ,background_color=Color(255, 255, 255)):
        self.spheres = spheres
        self.lights= lights
        self.background_color = background_color

    def closest_intersection(self, origin : Vector, direction : Vector, t_min: float, t_max: float) -> tuple[Sphere | None, float]:
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

    def trace_ray(self, ray: Ray, t_min: float, t_max: float, depth: int) -> tuple[int, int, int]:
        closest_sphere, closest_t = self.closest_intersection(ray.origin,ray.direction,t_min,t_max)
        if closest_sphere is None:
            return self.background_color.to_rgb()

        P = ray.point_at(closest_t)
        N = P.sub(closest_sphere.center).normalize()
        V = ray.direction.mul(-1)
        lighting = compute_lighting(P,N,V, closest_sphere.specular, self.lights, self)
        color = closest_sphere.color.mul(lighting)
        r = closest_sphere.reflective
        if depth <= 0 or r <= 0:
            return color.to_rgb()

        reflected_direction = N.mul(2 * N.dot(V)).sub(V)
        reflected_ray = Ray(P, reflected_direction)
        reflected_color = Color(*self.trace_ray(reflected_ray, 1e-8, float('inf'), depth - 1))

        color = color.mul(1 - r).add(reflected_color.mul(r))
        return color.to_rgb()
