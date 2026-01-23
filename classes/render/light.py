from __future__ import annotations
from classes.math3d.vector import Vector

class Light:
    def __init__(self, intensite_lumiere: float):
        self.intensite_lumiere = intensite_lumiere

class AmbientLight(Light):
    def __init__(self, intensite_lumiere:float):
        super().__init__(intensite_lumiere)

class PointLight(Light):
    def __init__(self, intensite_lumiere: float, position: Vector):
        super().__init__(intensite_lumiere)
        self.position = position

class DirectionalLight(Light):
    def __init__(self, intensite_lumiere, direction: Vector):
        super().__init__(intensite_lumiere)
        self.direction = direction.normaliser_le_vecteur()

def calcul_de_lumiere(P: Vector, N: Vector, V : Vector, s : int, lights : list[Light], tracer : "Tracer") -> float:
    intensite_lumiere = 0.0
    for light in lights:
        if isinstance(light, AmbientLight):
            intensite_lumiere +=light.intensite_lumiere

        else:
            if isinstance(light, PointLight):
                L = light.position.soutrait(P)
                t_max=1.0
            else:
                L= light.direction
                t_max= float('inf')

            shadow, _ = tracer.intersection_au_plus_proche(P,L,1e-8,t_max)
            if shadow:
                continue
            
            n_d_l =N.scalaire(L)

            if n_d_l>0:
                intensite_lumiere+= light.intensite_lumiere * (n_d_l) / (N.longueure() * L.longueure())

            if s!= -1:
                R =N.multiplier(2*N.scalaire(L)).soutrait(L)

                r_d_v = R.scalaire(V)
                if r_d_v>0:
                    intensite_lumiere += light.intensite_lumiere*((r_d_v/(R.longueure() * V.longueure()))** s)
    
    return intensite_lumiere