from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere
from classes.render.light import compute_lighting

class Tracer:
    def __init__(self, spheres, lights,background_color=(255, 255, 255)):
        self.spheres = spheres
        self.lights= lights
        self.background_color = background_color

    def closest_intersection(self, origin, direction, t_min: float, t_max: float):
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

    def trace_ray(self, ray: Ray, t_min: float, t_max: float):
        closest_sphere, closest_t = self.closest_intersection(ray.origin,ray.direction,t_min,t_max)
        if closest_sphere is None:
            return self.background_color
        
        P = ray.point_at(closest_t)
        N = P.sub(closest_sphere.center).normalize()
        V = ray.direction.mul(-1)
        lighting = compute_lighting(P,N,V, closest_sphere.specular, self.lights, self)
        R, G, B = closest_sphere.color
        return (min(int(R * lighting),255),min(int(G * lighting),255),min(int(B * lighting), 255))