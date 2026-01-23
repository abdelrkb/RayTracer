from __future__ import annotations
import math 

 
class Vector:
    def __init__(self,x : float,y : float,z:float):
        self.x = x 
        self.y = y
        self.z = z

    def aditioner(self, other : Vector) -> Vector:
        return  Vector(self.x + other.x, self.y +  other.y, self.z  + other.z)
    def soutrait( self, other: Vector) -> Vector:
        return Vector(self.x -  other.x, self.y- other.y,  self.z - other.z)

    def multiplier(self, k: float) -> Vector:
        return Vector(self.x  * k,  self.y * k,  self.z * k)

    def scalaire(self, other) -> float:
        return self.x * other.x +  self.y * other.y + self.z *other.z

    def longueure(self) -> float:
        return math.sqrt(self.scalaire(self))  

    def normaliser_le_vecteur(self) -> Vector: 
        l = self.longueure() 
        if l == 0: 
            return Vector(0, 0, 0) 
        return Vector(self.x / l, self.y / l, self.z / l) 





