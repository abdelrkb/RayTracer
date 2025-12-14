from classes.math3d.ray import Ray
from classes.objects.sphere import Sphere
from classes.render.intersection import intersect_ray_sphere
from classes.math3d.vector import Vector

def test_sphere_intersection():
    # --- Setup ---
    # Camera at the origin
    origin = Vector(0, 0, 0)

    # Sphere centered at (0, -1, 3), radius 1
    sphere = Sphere(
        center=Vector(0, -1, 3),
        radius=1,
        color=(255, 0, 0)
    )

    # Ray pointing exactly to the center of the sphere
    ray = Ray(origin, Vector(0, -1, 3))

    # --- Test intersection ---
    t1, t2 = intersect_ray_sphere(ray, sphere)

    print("Intersection tests :")
    print(f"t1 = {t1}")
    print(f"t2 = {t2}")

    # --- Basic sanity checks ---
    # There must be 2 intersections
    assert t1 != float('inf') and t2 != float('inf'), "Ray should intersect the sphere."

    # The closest intersection must be positive
    assert t1 > 0 or t2 > 0, "Intersections must be in front of the camera."

    # First intersection must be the smaller t
    assert t2 < t1, "t2 should be the entry point (smaller t value)."

    print("✓ Sphere intersection test passed!")


if __name__ == "__main__":
    test_sphere_intersection()
