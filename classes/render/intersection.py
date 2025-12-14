def intersect_ray_sphere(ray, sphere):
    CO = ray.origin.sub(sphere.center)

    a = ray.direction.dot(ray.direction)
    b = 2 * CO.dot(ray.direction)
    c = CO.dot(CO) - sphere.radius * sphere.radius

    discriminant = b*b - 4*a*c

    if discriminant < 0:
        return float('inf'), float('inf')

    sqrt_d = discriminant ** 0.5
    t1 = (-b + sqrt_d) / (2*a)
    t2 = (-b - sqrt_d) / (2*a)

    return t1, t2
