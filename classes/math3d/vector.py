from __future__ import annotations
import math 

 
class Vector:
    def __init__(self,x : float,y : float,z:float):
        self.x = x 
        self.y = y
        self.z = z
    
    def __repr__(self ):
        return f"Vector({self.x }, {self.y }, {self.z})"

    def add(self, other : Vector) -> Vector:
        return  Vector(self.x + other.x, self.y +  other.y, self.z  + other.z)

    def sub( self, other: Vector) -> Vector:
        return Vector(self.x -  other.x, self.y- other.y,  self.z - other.z)

    def mul(self, k: float) -> Vector:
        return Vector(self.x  * k,  self.y * k,  self.z * k)

    def dot(self, other) -> float:
        return self.x * other.x +  self.y * other.y + self.z *other.z

    def length(self) -> float:
        return math.sqrt(self.dot(self))  

    def normalize(self) -> Vector: 
        l = self.length() 
        if l == 0: 
            return Vector(0, 0, 0) 
        return Vector(self.x / l, self.y / l, self.z / l) 





