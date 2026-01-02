from __future__ import annotations
from classes.math3d.vector import Vector

class Light:
    """
    Base class of all light sources.

    A light is characterized by an intensity value.
    """
    def __init__(self, intensity: float):
        """
        Create a light source.

        Args:
            intensity (float): light intensity (0-1 interval)
        """
        self.intensity = intensity

class AmbientLight(Light):
    """
    Ambient light source.

    Ambient light contributes a constant amount of light to every point
    in the scene, regardless of position or orientation.
    """
    def __init__(self, intensity:float):
        """
        Create an ambient light.

        Args:
            intensity (float): light intensity (0-1 interval)
        """
        super().__init__(intensity)

class PointLight(Light):
    """
    Point light source.

    Emits light from a single position in space equally in every directions.
    """
    def __init__(self, intensity: float, position: Vector):
        """
        Create a Point light.

        Args:
            intensity (float): light intensity (0-1 interval)
            position (vector): worldspace's position of the light
        """
        super().__init__(intensity)
        self.position = position

class DirectionalLight(Light):
    """
    Directional light source.

    A light coming from an infinite distance
    with a fixed direction for example the sun.
    """
    def __init__(self, intensity, direction: Vector):
        """
        Create a Point light.

        Args:
            intensity (float): light intensity (0-1 interval)
            direction (vector): incoming ligh direction
        """
        super().__init__(intensity)
        self.direction = direction.normalize()

def compute_lighting(P: Vector, N: Vector, V : Vector, s : int, lights : list[Light], tracer : "Tracer") -> float:
    """
    Compute the illumination at a point using either ambient, diffuse or point light.

    This function implements the lightning model described by Gabriel Gambett with ambient lightning, 
    diffuse reflection, specular reflection and shadow rays.

    Args:
        P (Vector): point being shaded
        N (Vector): normalized surface at P
        V (Vector): View direction (from P to camera)
        s (int) : specular (-1 for matte)
        lights (list[Light]) : lights of the scenes
        tracer (Tracer) : tracer used to test shadows intersections

    Returns : 
       intensity (float) : light intensity
    """
    intensity = 0.0
    for light in lights:
        if isinstance(light, AmbientLight):
            intensity +=light.intensity

        else:
            if isinstance(light, PointLight):
                L = light.position.sub(P)
                t_max=1.0
            else:
                L= light.direction
                t_max= float('inf')

            shadow, _ = tracer.closest_intersection(P,L,0.001,t_max)
            if shadow : continue
            n_d_l =N.dot(L)

            if n_d_l>0:
                intensity+= light.intensity * (n_d_l) / (N.length() * L.length())

            if s!= -1:
                R =N.mul(2*N.dot(L)).sub(L)

            r_d_v = R.dot(V)
            if r_d_v>0:
                intensity += light.intensity*((r_d_v/R.length() * V.length()) ** s)
    
    return intensity