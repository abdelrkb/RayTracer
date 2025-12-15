from classes.math3d.ray import Ray
import math

class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color


    def intersect_ray_sphere(self, ray: Ray):
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