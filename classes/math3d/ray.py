from classes.math3d.vector import Vector
            
class Ray:       
    def __init__(self,origin :Vector, direction: Vector):  
        self.origin =origin         

        self.direction =direction.normalize() 

    def point_at(self, t :float) -> Vector:    
        return self.origin.add(self.direction.mul(t))
         