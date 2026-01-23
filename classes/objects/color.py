from __future__ import annotations

class Color:    
    def __init__(self, r: float, g: float, b: float):       
        self.r = r
        self.g = g
        self.b = b

    def mul(self, k: float) -> Color:    
        return Color(self.r * k, self.g * k, self.b * k)            

    def add(self, other) -> Color:    
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)          

    def clamp(self):     
        return Color(min(255, max(0, int(self.r))), min(255, max(0, int(self.g))), min(255, max(0, int(self.b))))           

    def to_rgb(self):           
        c = self.clamp()        
        return (c.r, c.g, c.b)          