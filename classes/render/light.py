from __future__ import annotations
from classes.math3d.vector import Vector

class Light:
    def __init__(self, intensity: float):
        self.intensity = intensity

class AmbientLight(Light):
    def __init__(self, intensity:float):
        super().__init__(intensity)

class PointLight(Light):
    def __init__(self, intensity: float, position: Vector):
        super().__init__(intensity)
        self.position = position

class DirectionalLight(Light):
    def __init__(self, intensity, direction: Vector):
        super().__init__(intensity)
        self.direction = direction.normalize()

def compute_lighting(P: Vector, N: Vector, V : Vector, s : int, lights : list[Light], tracer : "Tracer") -> float:
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

            shadow, _ = tracer.closest_intersection(P,L,1e-8,t_max)
            if shadow:
                continue
            
            n_d_l =N.dot(L)

            if n_d_l>0:
                intensity+= light.intensity * (n_d_l) / (N.length() * L.length())

            if s!= -1:
                R =N.mul(2*N.dot(L)).sub(L)

                r_d_v = R.dot(V)
                if r_d_v>0:
                    intensity += light.intensity*((r_d_v/(R.length() * V.length()))** s)
    
    return intensity