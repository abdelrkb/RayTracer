from classes.math3d.vector import Vector

class Ray:       
    def __init__(self,origin :Vector, direction: Vector):  
        self.origin =origin         

        self.direction =direction.normaliser_le_vecteur() 

    def point_touchee(self, t :float) -> Vector:    
        return self.origin.aditioner(self.direction.multiplier(t))
         