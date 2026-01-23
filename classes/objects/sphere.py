from classes.math3d.ray import Ray
from classes.math3d.vector import Vector
from classes.objects.color import Color

import math

class Sphere:
    def __init__(self, center : Vector, radius : float, color : Color , specular= -1, reflective=0.0):
        self.center = center
        self.radius = radius
        self.color = color
        self.specular = specular
        self.reflective = reflective


    def intersect_ray_sphere(self, ray: Ray) -> tuple[float,float]:
        CO = ray.origin.sub(self.center)

        a = ray.direction.dot(ray.direction)
        b = 2 * CO.dot(ray.direction)
        c = CO.dot(CO) - self.radius * self.radius

        discriminant = b*b - 4*a*c

        if discriminant < 0:
            return float('inf'), float('inf')

        sqrt_d = math.sqrt(discriminant)
        t1 = (-b - sqrt_d) / (2*a)
        t2 = (-b + sqrt_d) / (2*a)

        return t1, t2