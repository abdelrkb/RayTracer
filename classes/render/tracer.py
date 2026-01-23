from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere
from classes.render.light import calcul_de_lumiere, Light
from classes.math3d.vector import Vector
from classes.objects.color import Color

class Tracer:
    def __init__(self, spheres :list[Sphere], lights :list[Light] ,background_color=Color(255, 255, 255)):
        self.spheres = spheres
        self.lights= lights
        self.background_color = background_color

    def intersection_au_plus_proche(self, origin : Vector, direction : Vector, t_min: float, t_max: float) -> tuple[Sphere | None, float]:
        closest_t = float('inf')
        closest_sphere = None
        ray = Ray(origin, direction)

        for sphere in self.spheres:
            t1, t2 = sphere.inter(ray)

            if t_min < t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_sphere = sphere

            if t_min < t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_sphere = sphere

        return closest_sphere, closest_t

    def trace_ray(self, ray: Ray, t_min: float, t_max: float, depth: int) -> tuple[int, int, int]:
        closest_sphere, closest_t = self.intersection_au_plus_proche(ray.origin,ray.direction,t_min,t_max)
        if closest_sphere is None:
            return self.background_color.en_rgb()

        P = ray.point_touchee(closest_t)
        N = P.soutrait(closest_sphere.center).normaliser_le_vecteur()
        V = ray.direction.multiplier(-1)
        lighting = calcul_de_lumiere(P,N,V, closest_sphere.specular, self.lights, self)
        color = closest_sphere.color.multiplier(lighting)
        r = closest_sphere.reflective
        if depth <= 0 or r <= 0:
            return color.en_rgb()

        reflected_direction = N.multiplier(2 * N.scalaire(V)).soutrait(V)
        reflected_ray = Ray(P, reflected_direction)
        reflected_color = Color(*self.trace_ray(reflected_ray, 1e-8, float('inf'), depth - 1))

        color = color.multiplier(1 - r).aditioner(reflected_color.multiplier(r))
        return color.en_rgb()
